import shutil
import os
import re

phonebook = []

for folder, sub_folders, files in os.walk(os.getcwd()):
    for each_fol in sub_folders:
        print('\n'+each_fol)
    for file in files:
        with open(os.path.join(folder, file),'r') as f:
            content = f.read()
        phonenumber =  re.findall(r"\d{3}-\d{3}-\d{4}",content)
        if not phonenumber == []:
            phonebook.extend(phonenumber)

print(phonebook)