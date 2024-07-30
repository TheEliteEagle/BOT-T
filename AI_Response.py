# install needed google API with: pip install google-generativeai
import sys
import os
import google.generativeai as genai # type: ignore

#-------------------------------------------------------------------------
# function to get response from API

def getResponse(newText, API):

    return newText #replace later




#------------------------------------------------------------------------
# main

#read API from file
api_key = ""
if os.path.exists('api.txt'):
    with open('api.txt', 'r') as file:
        api_key = file.read().strip()
else: #create file if first time running 
    with open('api.txt', 'w') as file:
        pass
#check user has replaced inside of file, exit if still default
if api_key == "" or api_key == "add your API key here":
    print("please open api.txt and enter your API key")
    sys.exit()

# TODO get user input

# TODO pass both into response function
getResponse("Tmp", api_key)

# TODO return new string