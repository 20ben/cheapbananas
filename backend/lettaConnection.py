from letta_client import Letta
import json


class lettaConnection:
    def __init__(self, LETTA_API_TOKEN, AGENT_ID):
        self.client = Letta(
            token=LETTA_API_TOKEN,
            project="default-project",
            timeout=180.0
        )

        try:
            self.agent_state = self.client.agents.retrieve(AGENT_ID)
            print("connected to agent")
        except Exception as e:
            print(f"Error retrieving agent {e}")

    def system_message(self, msgContent):
        response = self.client.agents.messages.create(
            agent_id=self.agent_state.id,
            message=[
                {
                    "role":"system",
                    "content":msgContent
                }
                ]
        )

        for msg in response.messages:
            if msg.message_type == "assistant_message":
                return msg.content
    

    # query letta agent to return deals for a specific restauraunt
    def query_deals(self, place_name, place_location):
        
        response = self.client.agents.messages.create(
            agent_id=self.agent_state.id,
            messages=[
        {
            "role": "system",
            "content": f"Return a list of deals for {place_name}. Deals specific to {place_name} in {place_location} should be prioritized, but all relevant and currently active deals should be returned. For each deal entry, specify the deal type, a description, the price/discount, the availability, and the source links. At the end, pass the arguments to the generate_deal_entries_json tool.",
        }])

        result = {}

        for message in response.messages:
            if message.message_type == "tool_call_message":
                last_call = message.tool_call.arguments
                
                

        print(last_call)
        args = json.loads(last_call)
            # print(message.tool_call.arguments)

        result['name'] = args['name']
        result['deals'] = args['deals']        

        return result


    