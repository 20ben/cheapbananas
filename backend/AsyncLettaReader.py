from letta_client import AsyncLetta
import json
import asyncio # You'll need this for running the async code, typically

class AsyncLettaReader:
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
            print("connected to reader")
        except Exception as e:
            print(f"Error retrieving reader {e}")

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


    
    # Define method as asynchronous
    async def read_deals(self, place_names, place_locations):
        name_location2D = [[place_names[i], place_locations[i]] for i in range(len(place_names))]

        
        # Use await for the asynchronous client call
        response = await self.client.agents.messages.create(
            agent_id=self.AGENT_ID,
            messages=[
        {
            "role": "system",
            "content": f"For every restauraunt location in {name_location2D} Return a list of deals for each restauraunt based solely on the restauraunt's memory block. Deals specific to the restauraunt's specific location should be prioritized, but all relevant and currently active deals should be returned. For each deal entry, specify the deal type, a description, the price/discount, the availability, and the source links. Call the generate_deal_entries_json tool for each restauraunt and pass their parameters to the tool. Pass them to the tool in the order they appeared in the list."
            # "content": f"Return a list of deals for {place_name} based solely on the restauraunt's memory block. Deals specific to {place_name} in {place_location} should be prioritized, but all relevant and currently active deals should be returned. For each deal entry, specify the deal type, a description, the price/discount, the availability, and the source links. At the end, pass the arguments to the generate_deal_entries_json tool."
        }])

        calls = []
        

        i = 0
        for message in response.messages:
            if message.message_type == "tool_call_message":
                # Ensure we handle the possibility of multiple tool calls and take the last one
                currdict = json.loads(message.tool_call.arguments)
                if 'deals' in currdict:
                    currdict['name'] = place_names[i]
                    calls.append(currdict)
                    i += 1
                 
                
        return calls
            # This is still synchronous and safe to use
        # args = json.loads(last_call)
            
        # result['name'] = place_name
        # result['deals'] = args['deals']
            
        # return result
        
        # Return an empty dict if no tool call message was found
        # return {}