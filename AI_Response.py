# install needed google API with: pip install google-generativeai
import sys
import os
import google.generativeai as genai # type: ignore

#-------------------------------------------------------------------------
# function to get response from API

def getResponse(newText, history=[]):

    genai.configure(api_key= getAPIkey())

    settings = { #model settings
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 150,
    }

    model = genai.GenerativeModel(model_name= "gemini-1.0-pro", generation_config= settings, safety_settings=[])
    
    chat = model.start_chat(history = history)
    chat.send_message(newText)

    return {'text':chat.last.text, 'history':chat.history}


#------------------------------------------------------------------------
# get API key function

def getAPIkey():
    #read API key from file
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
    return api_key


#===============================================================================================================
# MAIN
#===============================================================================================================


# make an example request with no history
response = getResponse("Hello Bob")
sys.exit(response['text'])