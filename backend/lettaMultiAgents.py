# install letta_client with `pip install letta-client`
from letta_client import Letta

# create a client to connect to Letta
client = Letta(token="YWJjYzM3OWYtYWYwYS00ZTg5LTgzOTUtNDVkOWVlMTRlOTY0OjY5YjBiMTg5LTA2MGMtNGU5OC1iZjJhLWM5YjdkZmM1MDE0ZA==")

# create a shared memory block
shared_block = client.blocks.create(
    label="organization",
    description="Shared information between all agents within the organization.",
    value="Nothing here yet, we should update this over time."
)

# create a supervisor agent
supervisor_agent = client.agents.create(
    model="anthropic/claude-3-5-sonnet-20241022",
    embedding="openai/text-embedding-3-small",
    # blocks created for this agent
    memory_blocks=[{"label": "persona", "value": "I am a supervisor"}],
    # pre-existing shared block that is "attached" to this agent
    block_ids=["block-0bfed65e-2899-4b2f-a660-ad5b582c07a9"],
)

# create a worker agent
worker_agent = client.agents.create(
    model="anthropic/claude-3-5-sonnet-20241022",
    embedding="openai/text-embedding-3-small",
    # blocks created for this agent
    memory_blocks=[{"label": "persona", "value": "I am a worker"}],
    # pre-existing shared block that is "attached" to this agent
    block_ids=["block-0bfed65e-2899-4b2f-a660-ad5b582c07a9"],
)


