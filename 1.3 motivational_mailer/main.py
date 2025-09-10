import smtplib
import os
import random
from dotenv import load_dotenv

load_dotenv()  

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
RECEIVER = os.getenv("RECEIVER")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
quote_file_path = os.path.join(BASE_DIR, "quotes.txt")

with open(quote_file_path) as quote_file:
    quotes = quote_file.readlines()
    random_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=RECEIVER,
        msg="Subject:Motivational Quote\n\n" + random_quote
    )
print("Email sent successfully!")