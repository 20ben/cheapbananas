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


MINION_ID1 = os.environ.get('MINION_ID1')
if MINION_ID1 is None:
    raise ValueError("MINION_ID1 environment variable not set")
MINION_ID2 = os.environ.get('MINION_ID2')
if MINION_ID2 is None:
    raise ValueError("MINION_ID2 environment variable not set")


READER_ID = os.environ.get('READER_ID')
if READER_ID is None:
    raise ValueError("READER_ID environment variable not set")

async def main():
    print("started!")
    minionConnection1 = AsyncLettaMinion(LETTA_API_TOKEN, MINION_ID1)
    await minionConnection1.connect_agent()
    minionConnection2 = AsyncLettaMinion(LETTA_API_TOKEN, MINION_ID2)
    await minionConnection2.connect_agent()

    




asyncio.run(main())