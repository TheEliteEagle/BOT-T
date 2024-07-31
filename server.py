# to start server, type python server.py into command line
from flask import Flask, render_template, request  # type: ignore
import AI_Response

app = Flask(__name__)

@app.route('/')
def initialise():
    response = AI_Response.getResponse("In two sentances or less, introduce yourself as  BOT-T, who will answer and questions about Max or his cv in plain text") #test basic ai response
    return render_template('home.html', response=response['text'])

@app.route('/', methods=['POST'])
def respond():
    response = AI_Response.getResponse(request.form['input']) #answer user question
    return render_template('home.html', response=response['text'])

if __name__ == '__main__':
    app.run(host='localhost', port = 80) #use port 80 to make link "localhost"