from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Practice
# url = "https://appbrewery.github.io/instant_pot/"
# Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# ====================== Add Headers to the Request ===========================


# A minimal header:

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Adding headers to the request
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# Check you are getting the actual Amazon page back and not something else:
print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)
    
# Set the price below which you would like to get a notification
BUY_PRICE = 70

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        result = connection.login(os.getenv("MY_EMAIL"), os.getenv("APP_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"),
            to_addrs=os.getenv("MY_EMAIL"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )