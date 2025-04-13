from google.adk.agents import LlmAgent
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search
from . import prompt
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

APP_NAME="web_search_summarization_agent"
USER_ID="user-1234"
SESSION_ID="session-1234"

# Google search tool is not supported for model openai/gpt-4o-mini, therefore using sub-agent for it.
# The sub-agent is a pre-built agent that can perform Google searches and return results.
basic_search_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)

# --- Example Agent using OpenAI's GPT-4o ---
# (Requires OPENAI_API_KEY)
root_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4o-mini"), # LiteLLM model string format
    name="openai_web_search_summarization_agent",
    description= "This agent is an advanced AI orchestrator that accepts a user’s query, delegates it to a sub-agent for web searching, and returns a concise summary. It clarifies ambiguities by highlighting conflicting information and prompts the user for details. By leveraging automated search and synthesis, the agent provides contextually relevant answers while maintaining transparency about uncertainties.",
    instruction=prompt.SUMMARIZATION_INSTR,
    tools=[agent_tool.AgentTool(agent=basic_search_agent)],
)

# Session and Runner
session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

# Agent Interaction
def call_agent(query):
    """
    Helper function to call the agent with a query.
    """
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

# call_agent("What is quantum computing?")