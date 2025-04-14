from dotenv import load_dotenv
import os

from google.adk.tools import ToolContext
from github import (
    Auth,
    Github,
    GithubIntegration
)

load_dotenv()
username = os.getenv("GH_USERNAME")
login_email=os.getenv("GH_EMAIL")
password = os.getenv("GH_PASSWORD")

def authenticate():
    auth = Auth.Login(
        login=login_email,
        password=password
    )

    gh = Github(auth=auth)
    login_test = gh.get_user().login
    print(login_test)

def commits(commit_id: str ,tool_context: ToolContext):
    pass

def pull_requests(pull_requests_id: str ,tool_context: ToolContext):
    pass

def main():
    authenticate()

if __name__ == "__main__":
    main()