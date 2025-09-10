import requests
from bs4 import BeautifulSoup

# Ask user for date (year + month)
year = input("Enter the year (YYYY): ")
month = input("Enter the month (MM): ")

# Default day = 01
date = f"{year}-{month}-01"
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website_html = response.text

# Parse HTML (important: use website_html, not URL)
soup = BeautifulSoup(website_html, "html.parser")

# Extract songs and artists with current Billboard structure
songs = [song.get_text(strip=True) for song in soup.select("li ul li h3")]
artists = [artist.get_text(strip=True) for artist in soup.select("li ul li span")]

# Print results
print(f"\nBillboard Hot 100 for {date}\n")
for i, (song, artist) in enumerate(zip(songs, artists), start=1):
    print(f"{i}. {song} — {artist}")

print(f"✅ Done top songs in {year}-{month}-01")
