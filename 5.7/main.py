import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("VALORANT_API_KEY")

# Player info
region = "ap"
name = "buldak"
tag = "0530"

# API endpoint for player MMR (rank)
url = f"https://api.henrikdev.xyz/valorant/v1/mmr/ap/{name}/{tag}"

headers = {"Authorization": API_KEY}

# Send request
response = requests.get(url, headers=headers)

# Check response
if response.status_code == 200:
    data = response.json()
    mmr_data = data.get("data", {})
    current_tier = mmr_data.get("currenttierpatched", "Unknown")
    ranking = mmr_data.get("ranking_in_tier", 0)
    rr = mmr_data.get("elo", 0)

    print(f"{name}#{tag}'s Rank Info:")
    print(f"Rank: {current_tier}")
    print(f"RR in Tier: {ranking}")
    print(f"Elo: {rr}")
else:
    print(f"Error {response.status_code}: {response.text}")
