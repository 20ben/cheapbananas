from dotenv import load_dotenv
import os
from letta_client import Letta
from AsyncLettaMinion import AsyncLettaMinion
from AsyncLettaReader import AsyncLettaReader
import asyncio
import threading
import time

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


async def run_minion_async(minion_id, data):
    minion = AsyncLettaMinion(LETTA_API_TOKEN, minion_id)
    await minion.connect_agent()
    await minion.save_deals(*data)  # <- await it!

def run_minion_thread(minion_id, data):
    # Each thread runs its own asyncio event loop
    asyncio.run(run_minion_async(minion_id, data))

MINION_IDS = [os.environ[f"MINION_ID{i}"] for i in range(1, 9)]

FAKE_DATA = [
    ["TP Tea", "Berkeley"],
    ["Sharetea", "Berkeley"],
    ["Boba Guys", "Berkeley"],
    ["Quickly", "Berkeley"],
    ["Gong Cha", "Berkeley"],
    ["Happy Lemon", "Berkeley"],
    ["Tea Era", "Berkeley"],
    ["Tiger Sugar", "Berkeley"]
]

# Async function for one minion
async def run_minion_async(minion_id, data):
    minion = AsyncLettaMinion(LETTA_API_TOKEN, minion_id)
    await minion.connect_agent()
    await minion.save_deals(*data)

# Thread wrapper
def run_minion_thread(minion_id, data):
    asyncio.run(run_minion_async(minion_id, data))

# Create and start threads
threads = []
for minion_id, data in zip(MINION_IDS, FAKE_DATA):
    t = threading.Thread(target=run_minion_thread, args=(minion_id, data))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

reader = AsyncLettaMinion(LETTA_API_TOKEN, READER_ID)
print(reader.)

print("All 8 minions connected and data saved!")