from dotenv import load_dotenv
import os
from letta_client import Letta

# load Letta API key from from .env and check validity
load_dotenv()
LETTA_API_KEY = os.environ.get('LETTA_API_KEY')
if LETTA_API_KEY is None:
    raise ValueError("LETTA_API_KEY environment variable not set")

# # connect to a local server
# client = Letta(token=LETTA_API_KEY)

client = Letta(token=LETTA_API_KEY)

# connect to Letta Cloud
client = Letta(
    token="sk-let-ZWEzYTQ5MmYtZGJhOS00NmI3LTgzMTUtZjNmODQxYWRkZGYxOjkwZWFkZjNlLWMzMmItNDk1YS04MjU4LWFiNzM0MTliODBlMg==",
    project="hackathon",
)
