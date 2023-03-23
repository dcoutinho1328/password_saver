from cryptography.fernet import Fernet
from getpass import getpass
import json
from base64 import urlsafe_b64encode as encoder

service = input("Type the service to save password: \n")

password = getpass("Type the password: \n")

key = getpass("Enter the decryption key: \n")

key = (key * 32)[:32]

fernet = Fernet(encoder(key.encode()))

encPass = fernet.encrypt(password.encode())

content = {}

with open("passwords.json", "r") as file:
    try:
        content = json.loads(file.read())
    except:
        print("Error retrieving data")
        quit()

with open("passwords.json", "w") as file:
    try:
        content[service] = encPass.decode()
        file.write(json.dumps(content))
    except:
        print("Error trying to save the data")
        quit()
