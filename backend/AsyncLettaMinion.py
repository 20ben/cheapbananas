from letta_client import AsyncLetta
import json
import asyncio # You'll need this for running the async code, typically

class AsyncLettaMinion:
    # Use the asynchronous client in the constructor
    def __init__(self, LETTA_API_TOKEN, AGENT_ID):
        self.client = AsyncLetta(
            token=LETTA_API_TOKEN,
            project="default-project",
            timeout=180.0
        )
        self.AGENT_ID = AGENT_ID
        self.agent_state = None

    # The __init__ method itself is still synchronous, but we'll move the
    # API call to an async method or handle the connection outside.
    # For a clean asynchronous class, it's best to have a separate
    # async connection/initialization method.
    async def connect_agent(self):
        try:
            # Use await for the asynchronous client call
            self.agent_state = await self.client.agents.retrieve(self.AGENT_ID)
            print("connected to minion")
        except Exception as e:
            print(f"Error retrieving minion {e}")

    # Define method as asynchronous
    async def system_message(self, msgContent):
        # Use await for the asynchronous client call
        response = await self.client.agents.messages.create(
            agent_id=self.agent_state.id,
            messages=[ # Note: using 'messages' instead of 'message' as per the 'query_deals' method
                {
                    "role":"system",
                    "content":msgContent
                }
            ]
        )

        for msg in response.messages:
            if msg.message_type == "assistant_message":
                return msg.content
        return None # Return None if no assistant message is found


    async def save_deals(self, place_name, place_location):
        
        try:
            response = await self.client.agents.messages.create(
                agent_id=self.agent_state.id,
                messages=[
            {
                "role": "system",
                "content": f"Save a list of deals entries for {place_name} to a memory block or update it if it already exists. Deals specific to {place_name} in {place_location} should be prioritized, but all relevant and currently active deals should be returned. For each deal entry, specify the deal type, a description, the price/discount, the availability, and the source links. If there is no relevant info for this {place_name} {place_location} then do not write to memory.",
            }])
            print("save complete")
        except Exception as e:
            print("error 524 timeout")


