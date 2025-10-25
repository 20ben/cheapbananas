from letta_client import Letta

# connect to a local server
client = Letta(base_url="http://localhost:8283")

# connect to Letta Cloud
client = Letta(
    token="sk-let-ZWEzYTQ5MmYtZGJhOS00NmI3LTgzMTUtZjNmODQxYWRkZGYxOjkwZWFkZjNlLWMzMmItNDk1YS04MjU4LWFiNzM0MTliODBlMg==",
    project="hackathon",
)
