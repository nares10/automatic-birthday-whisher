import datetime as dt
import csv
import random

import smtplib
SMTP_INFORMATION_PROTOCALL = "smtp.gmail.com"

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
sender_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")

# Get the current date and time
now = dt.datetime.now()
today = now.day # Get the current day and month
this_month = now.month

# Open the CSV file containing birthday information
with open("birthdays.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    try: 
        # Set up the SMTP connection
        connection = smtplib.SMTP(SMTP_INFORMATION_PROTOCALL, 587)
        connection.starttls()
        connection.login(sender_email, password)
        for row in reader:
            receiver_email = row["email"]
            name = row["name"]
            birth_month = int(row["birth_month"])
            birth_day = int(row["birth_day"])
            # Check if today is the person's birthday
            if birth_month == this_month and birth_day == today:
                letter_number = random.randint(1, 4)  # Get a random letter template
                try:
                    # Read the selected letter template with UTF-8 encoding
                    with open(f"./letter{letter_number}.txt", "r", encoding="utf-8") as letter:
                        letter_content = letter.read()
                        
                        # Personalize the letter with the person's name
                        personalised_letter = letter_content.replace("{name}", name)

                        # Send the email
                        connection.sendmail(from_addr=sender_email,
                                            to_addrs=receiver_email,
                                            msg=f"Subject: Happy Birthday {name}\n\n{personalised_letter}")
                        print("Email sent successfully!")
                except FileNotFoundError:
                    print(f"Letter template letter{letter_number}.txt not found.")
                except UnicodeEncodeError as e:
                    print(f"Unicode encoding error: {e}")
                except Exception as e:
                    print(f"An error occurred while reading the letter template: {e}")

    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email address and password.")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the server. Check your network connection and SMTP server address.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        try:
            connection.quit()  # Terminate the SMTP session
        except NameError:
            print("Failed to establish connection, nothing to close.")
        except Exception as e:
            print(f"Error while closing the connection: {e}")
