from dotenv import load_dotenv
import os
from letta_client import Letta

# load Letta API key and agent ID from from .env and check validity
load_dotenv()
LETTA_API_TOKEN = os.environ.get('LETTA_API_TOKEN')
if LETTA_API_TOKEN is None:
    raise ValueError("LETTA_API_TOKEN environment variable not set")
AGENT_ID = os.environ.get('AGENT_ID')
if AGENT_ID is None:
    raise ValueError("AGENT_ID environment variable not set")

# connect to Letta Cloud
client = Letta(
    token=LETTA_API_TOKEN,
    project="default-project",
)

try:
    agent_state = client.agents.retrieve(AGENT_ID)
    print("connected to agent")
except Exception as e:
    print(f"Error retrieveing agent {e}")

response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "What's the last thing you remember I told you?",
        }
    ]
)

for message in response.messages:
    if message.message_type == "assistant_message":
        print("This is the Assistant Message")
        print(message.content)

print("end")