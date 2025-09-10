import requests
from bs4 import BeautifulSoup
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ask user for date (year + month)
year = input("Enter the year (YYYY): ")
month = input("Enter the month (MM): ")
day = input("Enter the day (DD) ")

# Default day = 01
date = f"{year}-{month}-{day}"
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website_html = response.text

# Parse HTML
soup = BeautifulSoup(website_html, "html.parser")
songs = [song.get_text(strip=True) for song in soup.select("li ul li h3")]
artists = [artist.get_text(strip=True) for artist in soup.select("li ul li span")]

print(f"\nBillboard Hot 100 for {date} (Top 3)\n")

# Only take top 3
for i, (song, artist) in enumerate(zip(songs, artists), start=1):
    if i > 3: # change this number to download more songs
        break
    search_query = f"{song} {artist}"
    print(f"{i}. Downloading {search_query} ...")

    # Build full path inside current folder
    output_path = os.path.join(BASE_DIR, f"{i:02d} - {song} - {artist}.%(ext)s")
    
    # Use yt-dlp to download best audio as mp3
    subprocess.run([
        "yt-dlp",
        f"ytsearch1:{search_query}",  # search YouTube, take 1st result
        "-x", "--audio-format", "mp3",  # extract audio as MP3
        "-o", output_path
    ])

print("\n✅ Done! Top 3 songs downloaded to your script's folder.")
