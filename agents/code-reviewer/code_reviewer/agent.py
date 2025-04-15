from google.adk.agents.llm_agent import Agent
from .shared_libraries import constants
from .tools import commit
from . import prompt

root_agent = Agent(
    model=constants.MODEL,
    name=constants.ROOT_AGENT_NAME,
    description=constants.DESCRIPTION,
    instruction=prompt.ROOT_AGENT,
    tools=[
        commit.get_commit_tool,
    ],
)