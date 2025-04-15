from google.adk.tools import ToolContext
from .github_ops import GithubHandler

import re

def get_commit_tool(tool_context: ToolContext) -> dict[str, str]:

    sha_match = re.search(r"([0-9a-f]{6,40})", tool_context.user_content.parts[0].text)
    if not sha_match:
        return {"status": "error", "message": "No valid SHA found in user input."}

    sha = sha_match.group(1)

    # repo = tool_context.user_content.parts[0].text
    gh = GithubHandler(repo_name="ju4nv1e1r4/agents-with-adk")

    try:
        commit = gh.get_commit(sha=sha)
        return {
            "status": "ok",
            "author": commit.commit.author.name,
            "message": commit.commit.message,
            "date": commit.commit.author.date.isoformat(),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}