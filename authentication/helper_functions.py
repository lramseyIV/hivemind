import random
# helper functions for authentication app to help keep views.py clean

#function to send email to user

#function to generate random string for verification
def create_verification_url():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    result = ""
    for i in range (30):
        result += chars[random.randint(0, len(chars)-1)]
    return result

    
