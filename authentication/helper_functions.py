import random
import os
import smtplib
from dotenv import load_dotenv
# helper functions for authentication app to help keep views.py clean

#function to send email to user
def send_email(recipient, message):
    load_dotenv()
    s = smtplib.SMTP('smtp.gmail.com', 587) # will change if not using gmail
    s.starttls()
    try:
        s.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    except smtplib.SMTPAuthenticationError:
        return False
    try:
        s.sendmail(os.getenv("EMAIL"), recipient, message)
    except smtplib.SMTPException:
        return False
    s.quit()
    return True

#function to generate random string for verification
def create_verification_url():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    result = ""
    for i in range (30):
        result += chars[random.randint(0, len(chars)-1)]
    return result

def gen_password():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "*", "(", ")"]
    result = ""
    for i in range (12):
        result += chars[random.randint(0, len(chars)-1)]
    return result