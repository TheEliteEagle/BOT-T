# to start server, type python server.py into command line
from flask import Flask  # type: ignore
import AI_Response

app = Flask(__name__)

@app.route('/')
def initialise():
    response = AI_Response.getResponse("You are to repeat back, it works!") #test basic ai response
    return response['text']

if __name__ == '__main__':
    app.run(host='localhost', port = 80) #use port 80 to make link "localhost"