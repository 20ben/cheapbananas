import brightdata
from brightdata import bdclient

BRIGHTDATA_API_TOKEN = "f3987c7467b89ac36fd35946cda889bcb797d20ec548c7089f5a1a2ae6b3777d"
client = bdclient(api_token=BRIGHTDATA_API_TOKEN) # can also be defined as BRIGHTDATA_API_TOKEN in your .env file

# # Simple single query search
# result = client.search("pizza restaurants")

# # Try using multiple queries (parallel processing), with custom configuration
# queries = ["restaurant deals"]
# results = client.search(
#     queries,
#     search_engine="google",
# )

# Basic extraction (URL in query)
result = client.search("Find deals for Insommia Cookies in Berkeley")

print(result)
print(client.parse_content(result))  # Returns structured JSON matching the schema