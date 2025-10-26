from dotenv import load_dotenv
from asyncLettaConnection import asynclettaConnection
import os
import asyncio # You need to import asyncio
# Assuming 'lettaConnection' now uses 'AsyncLetta' and has 'async def' methods

# load Letta API key and agent ID from from .env and check validity
load_dotenv()
LETTA_API_TOKEN = os.environ.get('LETTA_API_TOKEN')
if LETTA_API_TOKEN is None:
    raise ValueError("LETTA_API_TOKEN environment variable not set")
AGENT_ID = os.environ.get('AGENT_ID')
if AGENT_ID is None:
    raise ValueError("AGENT_ID environment variable not set")

# 1. Define an asynchronous function to run your code
async def main():
    connection = asynclettaConnection(LETTA_API_TOKEN, AGENT_ID)
    
    # You MUST await the connection method
    await connection.connect_agent()

    # 2. You MUST await the call to the async method query_deals
    insomnia_deals = await connection.query_deals("Insomnia Cookies", "362 Kearny St.")
    print(insomnia_deals)

    # 3. You MUST await the second call as well
    penelopes_deals = await connection.query_deals("Penelope's Coffee & Tea", "121 Spear St Suite B12")
    print(penelopes_deals)

# 4. Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())