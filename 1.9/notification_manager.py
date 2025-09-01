import os
import smtplib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class NotificationManager:

    def __init__(self):
        # Load email + password (app password if Gmail/Outlook)
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["APP_PASSWORD"]
        self.smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.environ.get("SMTP_PORT", 587))
        self.to_email = os.environ["RECEIVER_EMAIL"]

    def send_email(self, subject, message_body):
        """
        Sends an email using SMTP.
        Parameters:
        - subject (str): The subject line of the email.
        - message_body (str): The content of the email.
        """
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as connection:
            connection.starttls()  # Secure the connection
            connection.login(self.email, self.password)

            msg = f"Subject:{subject}\n\n{message_body}"
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.to_email,
                msg=msg.encode("utf-8")
            )
        print("✅ Email sent successfully!")
