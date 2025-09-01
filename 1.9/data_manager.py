import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        """Get all data from Sheety and return it as a list of dicts"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        print("DEBUG Response JSON:", data)  # 👈 See what key to use

        # ⚠️ Change "prices" to match your sheet tab name in Google Sheets
        # Example: if tab is "Sheet1", use data["sheet1"]
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update Google Sheet with new IATA codes"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(f"Updated row {city['id']}: {response.text}")
