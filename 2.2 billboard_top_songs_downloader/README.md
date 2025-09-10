🎵 Billboard Hot 100 Downloader

A Python script that scrapes the Billboard Hot 100 chart for any given date and downloads the top songs as MP3 files using yt-dlp.

Easily relive the music hits of any day in history 🎶

✨ Features

📅 Choose any date (Year, Month, Day).

🎧 Downloads songs as MP3 from YouTube.

🔢 Option to download Top N songs (default: 3).

📂 Files saved in a clean format:

01 - Song Title - Artist.mp3

🛠️ Requirements

Install dependencies before running:

pip install requests beautifulsoup4 yt-dlp

▶️ Usage

Run the script:

python billboard_top_songs_downloader.py


You’ll be prompted:

Enter the year (YYYY): 2020
Enter the month (MM): 07
Enter the day (DD): 04


The script fetches the Billboard Hot 100 for that date and downloads the top tracks.

🔧 Change Download Quantity

By default, the script downloads the Top 3 songs.
You can easily change this in the for loop:

# Only take top 3
for i, (song, artist) in enumerate(zip(songs, artists), start=1):
    if i > 3:  # 👈 Change this number to download more songs
        break


Examples:

if i > 10: → downloads Top 10 songs.

Remove the line → downloads all 100 songs.

📂 Project Structure
billboard-downloader/
│── billboard_top_songs_downloader.py
│── README.md
│── requirements.txt
│── .gitignore

📝 Example Output
Billboard Hot 100 for 2020-07-04 (Top 3)

1. Downloading Rockstar DaBaby Featuring Roddy Ricch ...
2. Downloading Savage Megan Thee Stallion Featuring Beyoncé ...
3. Downloading Blinding Lights The Weeknd ...

✅ Done! Top 3 songs downloaded to your script's folder.