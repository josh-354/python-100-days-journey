import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        response.raise_for_status()
        token_data = response.json()
        print(f"✅ Got Amadeus token (expires in {token_data['expires_in']}s)")
        return token_data['access_token']

    def get_destination_code(self, city_name):
        """Get IATA code for a city using Amadeus API"""
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        print(f"Lookup {city_name} → {response.status_code}: {response.text}")

        try:
            return response.json()["data"][0]["iataCode"]
        except (IndexError, KeyError):
            print(f"⚠️ No IATA code found for {city_name}")
            return "N/A"
