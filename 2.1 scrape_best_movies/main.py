import requests
from bs4 import BeautifulSoup
import os

BASE_DIR = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(BASE_DIR, "movies.txt")

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

for movie in all_movies:
    print(movie.get_text())

with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
    for title in all_movies:
        file.write(f"{title.get_text()}\n")

print("✅ Saved", len(all_movies), "movies to movies.txt")