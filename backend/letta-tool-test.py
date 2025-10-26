from letta_client import Letta



# Create client (Letta Cloud)
client = Letta(token="YWJjYzM3OWYtYWYwYS00ZTg5LTgzOTUtNDVkOWVlMTRlOTY0OjY5YjBiMTg5LTA2MGMtNGU5OC1iZjJhLWM5YjdkZmM1MDE0ZA==")

# Or for self-hosted
# client = Letta(base_url="http://localhost:8283")

def generate_rank(rank: int, reason: str):
    """Generate a ranking with explanation.

    Args:
        rank (int): The numerical rank from 1-10.
        reason (str): The reasoning behind the rank.
    """
    print("Rank generated")
    return

# Create the tool
tool = client.tools.create(func=generate_rank)

# Create agent with the structured generation tool
agent_state = client.agents.create(
    model="openai/gpt-4o-mini",
    embedding="openai/text-embedding-3-small",
    memory_blocks=[
        {
            "label": "human",
            "value": "The human's name is Chad. They are a food enthusiast who enjoys trying different cuisines."
        },
        {
            "label": "persona",
            "value": "I am a helpful food critic assistant. I provide detailed rankings and reviews of different foods and restaurants."
        }
    ],
    tool_ids=[tool.id]
)

# Send message and instruct agent to use the tool
response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "How do you rank sushi as a food? Please use the generate_rank tool to provide your response."
        }
    ]
)

# Extract structured data from tool call
for message in response.messages:
    if message.message_type == "tool_call_message":
        import json
        args = json.loads(message.tool_call.arguments)
        rank = args["rank"]
        reason = args["reason"]
        print(f"Rank: {rank}")
        print(f"Reason: {reason}")

