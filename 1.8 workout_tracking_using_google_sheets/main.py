import requests
from datetime import datetime
import json
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, 'config.json')

# ----------------- Load credentials from JSON -----------------
with open(json_path) as f:
    config = json.load(f)

APP_ID = config["ENV_NIX_APP_ID"]
API_KEY = config["ENV_NIX_API_KEY"]
sheet_endpoint = config["ENV_SHEETY_ENDPOINT"]
SHEETY_TOKEN = config["ENV_SHEETY_TOKEN"]

# ----------------- Personal Data -----------------
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

# ----------------- API Endpoints -----------------
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# ----------------- User Input -----------------
exercise_text = input("Tell me which exercises you did: ")

# ----------------- Nutritionix Request -----------------
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

# ----------------- Date & Time -----------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# ----------------- Sheety Request -----------------
bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    sheet_response.raise_for_status()
    print(sheet_response.text)
