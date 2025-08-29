import requests
import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz

# Load environment variables
load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("APP_PASSWORD")
RECEIVER = os.getenv("RECEIVER")

# Get API key
api_key = os.getenv("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Cebu, Philippines
latitude = 10.3167
longitude = 123.9105

# Forecast hours = cnt × 3h
cnt = 4
forecast_hours = cnt * 3

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric",
    "cnt": cnt
}

# Request weather data
response = requests.get(OWM_endpoint, params=weather_params)
weather_data = response.json()

will_rain = False

# Timezone setup
tz = pytz.timezone("Asia/Manila")
local_time = datetime.now(tz)
forecast_end = local_time + timedelta(hours=forecast_hours)

# Check if API returned valid forecast
if "list" not in weather_data:
    print(" API Error:", weather_data.get("message", "Unknown error"))
else:
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]

        # Only check for rain/snow/drizzle/thunderstorm
        if int(condition_code) < 700:
            will_rain = True
            break

# Message body
# Message body
if will_rain:
    body = (
        f"Rain is expected in the next {forecast_hours} hours.\n"
        f"Bring an umbrella if you go out.\n\n"
        f"Period: {local_time.strftime('%B %d, %I %p')} to {forecast_end.strftime('%B %d, %I %p')}"
    )
else:
    body = (
        f"No rain expected in the next {forecast_hours} hours.\n"
        f"Weather looks clear.\n\n"
        f"Period: {local_time.strftime('%B %d, %I %p')} to {forecast_end.strftime('%B %d, %I %p')}"
    )


# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=RECEIVER,
        msg=f"Subject:Weather Forecast\n\n{body}"
    )

print("Email sent successfully!")
print(body)
