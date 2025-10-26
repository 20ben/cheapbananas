from dotenv import load_dotenv
import os
from letta_client import Letta
import json

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
            "role": "system",
            "content": " Return a list of Insomnia Cookies deal entries based ONLY on your current memory. For each deal entry, specify the deal type, a description, the price/discount, the availability, and the source links. Do not scrape the web for any information this time. At the end, pass the arguments to the generate_deal_entries_json tool",
        }
    ]
)


result = {}

for message in response.messages:
    if message.message_type == "tool_call_message":
        print(type(message.tool_call.arguments))
        
        args = json.loads(message.tool_call.arguments)
        # print(message.tool_call.arguments)

        result['name'] = args['name']
        result['deals'] = args['deals']        

        print(result['deals'][0]['deal_type'])

        print(args)

        
print("end")

# def response_to_json(arguments):
#     result = {}
#     result['name']=arguments.name
    
#     deal_type_arr = arguments.deal_types

#     for i in range(result.len()):
#         result['Deal Type'] = arguments.deal_types[i]
#         result['Description'] = arguments.descriptions[i]
#         result['Price/Discount'] = arguments.price_discounts[i]
#         result['Availability'] = arguments.availabilities[i]
#         result['Source'] = arguments.sources[]
