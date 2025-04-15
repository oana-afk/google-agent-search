import os
from dotenv import load_dotenv
import logging

from google.adk.tools import ToolContext
from github import (
    Auth,
    Github,
    Repository,
    Commit
)

from github.GithubException import (
    BadCredentialsException,
    UnknownObjectException
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
load_dotenv()

class GithubHandler:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.pat = os.getenv("GH_PAT")
        if not self.pat:
            raise ValueError("GitHub token not found. Check the .env file")

    def authenticate(self) -> Github:
        try:
            auth = Auth.Token(self.pat)
            gh = Github(auth=auth)
            status = gh.get_user().login

            logging.info("Username authenticated: %s", status)
            print("---")
            return gh
        except BadCredentialsException as auth_error:
            logging.error(f"Authenticate error: {auth_error}")


    def get_repository(self, lazy = False) -> Repository:
        try:
            gh = self.authenticate()
            repo =  gh.get_repo(
                full_name_or_id=self.repo_name,
                lazy=lazy
            )
            logging.info(f"Repository: {self.repo_name}")
            return repo
        except UnknownObjectException as repo_error:
            logging.error(f"Repository error: {repo_error}")


    def get_commit(self, sha: str) -> Commit:
        try:
            repo = self.get_repository()
            commit = repo.get_commit(sha=sha)
            logging.info(f"Commit Author: {commit.commit.author}")
            return commit
        except UnknownObjectException as get_commit_error:
            logging.error(f"Get commit error: {get_commit_error}")

    def create_pr(self, title: str, body:str, base="main", head="preprod"):
        try:
            repo = self.get_repository()

            pr = repo.create_pull(
                base=base,
                head=head,
                title=title,
                body=body,
            )
            logging.info(f"PR: {pr}")
            return pr.get_commits()
        except UnknownObjectException as create_pr_error:
            logging.error(f"Create PR Error: {create_pr_error}")
        
    def get_pr(self, pr_number: int):
        try:
            repo = self.get_repository()
            pr = repo.get_pull(pr_number)
            logging.info(f"PR Number: {pr_number}")
            return pr
        except UnknownObjectException as get_pr_error:
            logging.error(f"PR number error: {get_pr_error}")


def main():
    gh = GithubHandler("ju4nv1e1r4/real-estate-dl")

    repo = gh.get_repository()
    print(repo)
    print("---")

    gh.get_commit("4993a0317dc4efa0b33bb317082dee1621cc62eb")
    print("---")

    gh.create_pr(
        "This is title created by automation",
        "This is an example of PR created by automation",
        base="main",
        head="dev"
    )
    print("---")

    gh.get_pr(1)

if __name__ == "__main__":
    main()