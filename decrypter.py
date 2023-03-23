from cryptography.fernet import Fernet
from getpass import getpass
import json
from base64 import urlsafe_b64encode as encoder
import pyperclip

service = input("Type the service to retrieve password: \n")

password = None

with open("passwords.json", "r") as file:
    try:
        password = json.loads(file.read()).get(service)
        if password == None:
            print(f'No password saved for service "{service}"')
            quit()
    except:
        print("Error trying to get the data")
        quit()

key = getpass("Enter the decryption key: \n")

key = (key * 32)[:32]

fernet = Fernet(encoder(key.encode()))

decPass = fernet.decrypt(password).decode()

pyperclip.copy(decPass)
