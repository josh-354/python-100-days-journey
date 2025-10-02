from flask import Flask, render_template, request
import smtplib
import requests
import os
from dotenv import load_dotenv  # To load environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Your blog data (from npoint API)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# ⚠️ Keep these safe, don’t upload to GitHub with credentials inside
OWN_EMAIL = os.getenv("MY_EMAIL")
OWN_PASSWORD = os.getenv("APP_PASSWORD")   # Your Gmail App Password (not normal password)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = (
        f"Subject: New Message from Blog Contact Form\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Message: {message}"
    )
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            # Send email back to yourself (receiver = OWN_EMAIL)
            connection.sendmail(
                from_addr=OWN_EMAIL,
                to_addrs=[OWN_EMAIL],
                msg=email_message.encode("utf-8")
            )
    except Exception as e:
        print("Error sending email:", e)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post

    if requested_post is None:
        return "Post not found", 404

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
