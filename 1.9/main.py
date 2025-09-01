import time
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

# ==================== Set up ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

flight_search = FlightSearch()

# ==================== Fill missing IATA codes ====================
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # slow down requests to avoid rate limit

print("\n✅ Updated sheet_data:")
pprint(sheet_data)

# ==================== Push updates back to Sheety ====================
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()
