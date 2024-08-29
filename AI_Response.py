# install needed google API with: pip install google-generativeai
import sys
import os
import google.generativeai as genai # type: ignore

#-------------------------------------------------------------------------
# function to get response from API

def getResponse(newText, history=[]):

    cvText = "CV document: [" + "INSERT CV TEXT HERE" + "] "
    flavourText = "Instructions: [You are BOT-T, and will answer questions about Max, his CV and convince users to hire Max.] Rules:[If the user talks about other topics not related to hiring Max and his CV, you are to return the conversation to hiring Max and his CV. Any response you give must be under 2 sentances unless the user asks for longer responses.] "
    finalText = flavourText + cvText + "User message: " + newText + "]"

    genai.configure(api_key= getAPIkey())

    settings = { #model settings
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 150,
    }

    model = genai.GenerativeModel(model_name= "gemini-1.0-pro", generation_config= settings, safety_settings=[])
    
    chat = model.start_chat(history = history)
    chat.send_message(finalText)

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
# MAIN      usage: <text input (optional)> <history (optional)>
#===============================================================================================================

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # make example request using only user text
        response = getResponse(sys.argv[1])    
    elif len(sys.argv) == 3:
        # make example request using user text and user history
        response = getResponse(sys.argv[1],sys.argv[2]) 
    else:
        # make an example request using default text and history as no command line input
        response = getResponse("count from 1 to 10")
        response = getResponse("what did i just ask you to do", response['history'])

    sys.exit(response['text'])    