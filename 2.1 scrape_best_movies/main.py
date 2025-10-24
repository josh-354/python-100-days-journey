import requests
from bs4 import BeautifulSoup
import os
from tkinter import *
from tkinter import messagebox

# Constants
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
BASE_DIR = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(BASE_DIR, "movies.txt")

def scrape_movies():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Check for HTTP errors
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")
        all_movies = soup.find_all(name="h3", class_="title")

        # Scrape only the first 3 movies
        top_movies = [movie.get_text() for movie in all_movies[:3]]

        # Display in UI
        result_text.delete(1.0, END)  # Clear previous results
        for i, movie in enumerate(top_movies, start=1):
            result_text.insert(END, f"{i}. {movie}\n")

        # Optionally save to file
        with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
            for movie in top_movies:
                file.write(f"{movie}\n")

        messagebox.showinfo("Success", f"Scraped and saved {len(top_movies)} movies to movies.txt")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
window = Tk()
window.title("Top Movies Scraper")
window.geometry("600x400")
window.config(padx=30, pady=30, bg="#f0f0f0")

# Main frame
main_frame = Frame(window, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

# Title label
title_label = Label(main_frame, text="Top 3 Movies from Empire Online", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# Scrape button
scrape_button = Button(main_frame, text="Scrape Movies", command=scrape_movies, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", padx=20, pady=5)
scrape_button.grid(column=0, row=1, columnspan=2, pady=(0, 20))

# Result text area
result_label = Label(main_frame, text="Movies will appear here:", font=("Arial", 14), bg="#f0f0f0")
result_label.grid(column=0, row=2, sticky="w")

result_text = Text(main_frame, height=10, width=50, font=("Arial", 12), bg="#e0e0e0", relief="sunken")
result_text.grid(column=0, row=3, columnspan=2, pady=(10, 0))

window.mainloop()
