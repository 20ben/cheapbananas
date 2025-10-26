from dotenv import load_dotenv
import os
from letta_client import Letta
from AsyncLettaMinion import AsyncLettaMinion
from AsyncLettaReader import AsyncLettaReader
import asyncio

# load Letta API key and agent ID from from .env and check validity
load_dotenv()
LETTA_API_TOKEN = os.environ.get('LETTA_API_TOKEN')
if LETTA_API_TOKEN is None:
    raise ValueError("LETTA_API_TOKEN environment variable not set")

READER_ID = os.environ.get('READER_ID')
if READER_ID is None:
    raise ValueError("READER_ID environment variable not set")

async def main():
    print("started!")

    readerConnection = AsyncLettaReader(LETTA_API_TOKEN, READER_ID)
    await readerConnection.connect_agent()

    deals = await readerConnection.read_deals(["Elaichi Co.", "Blue Bell Coffee"], ["Berkeley", "Berkeley"])

    print(deals)

asyncio.run(main())