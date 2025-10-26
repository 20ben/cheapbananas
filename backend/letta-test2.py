from dotenv import load_dotenv
import os
from letta_client import Letta
from lettaConnection import lettaConnection


# load Letta API key and agent ID from from .env and check validity
load_dotenv()
LETTA_API_TOKEN = os.environ.get('LETTA_API_TOKEN')
if LETTA_API_TOKEN is None:
    raise ValueError("LETTA_API_TOKEN environment variable not set")
AGENT_ID = os.environ.get('AGENT_ID')
if AGENT_ID is None:
    raise ValueError("AGENT_ID environment variable not set")

connection = lettaConnection(LETTA_API_TOKEN, AGENT_ID)

print(connection.query_deals("Insomnia Cookies", "362 Kearny St."))
print(connection.query_deals("Penelope's Coffee & Tea", "121 Spear St Suite B12"))