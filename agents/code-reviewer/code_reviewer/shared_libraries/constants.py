import os
from dotenv import load_dotenv

load_dotenv()

ROOT_AGENT_NAME = "code_reviewer"
DESCRIPTION = "Review code from a especific repository"
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "EMPTY")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
MODEL = os.getenv("MODEL", "gemini-2.0-flash-001")
GH_PAT = os.getenv("GH_PAT", "EMPTY")
