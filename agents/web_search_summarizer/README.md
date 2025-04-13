# Web Search Summarizer

## Use Case

The Web Search Summarizer is a tool designed to streamline the process of gathering and summarizing information from the web. It is particularly useful for users who need to quickly extract key insights from multiple web pages without manually reading through extensive content. This tool can be applied in various scenarios, such as:

- **Research and Analysis**: Summarize articles, blogs, or research papers for academic or professional purposes.
- **Content Curation**: Quickly gather and condense information for newsletters, reports, or presentations.
- **Decision Making**: Extract relevant details to make informed decisions based on web data.
- **Productivity Enhancement**: Save time by automating the summarization of lengthy web content.

Additionally, the Web Search Summarizer demonstrates how non-Gemini LLM models, such as OpenAI models, can be effectively integrated with the Google ADK. This flexibility allows developers to leverage a variety of language models to suit their specific use cases.

## Prerequisites

Before using the Web Search Summarizer, ensure the following prerequisites are met:

1. **Development Environment**:
    - A system with Python 3.8 or higher installed.
    - A code editor or IDE (e.g., Visual Studio Code, PyCharm).

2. **Dependencies**:
    - Install required Python libraries. These are typically listed in a `requirements.txt` file. Use the following command to install them:
      ```bash
      pip install -r requirements.txt
      ```

3. **API Keys**:
    - Obtain the necessary API keys for external services:
        - **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/signup/) and generate an API key from the API settings page.
        - **Google Gemini API Key**: Access the [Google AI Studio](https://ai.google/studio/) and follow the instructions to generate a Gemini API key.
    - Configure these keys securely in your environment:
        - Use environment variables (e.g., `OPENAI_API_KEY` and `GOOGLE_GEMINI_API_KEY`) to store the keys.
        - Alternatively, use a configuration file and ensure it is excluded from version control (e.g., add it to `.gitignore`).

By meeting these prerequisites, you can ensure a smooth setup and operation of the Web Search Summarizer.