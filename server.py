# to start server, type python server.py into command line
from flask import Flask, render_template, request, jsonify  # type: ignore
import AI_Response

app = Flask(__name__)

history = [] #probably a better way to store than globally? May copy across tabs..

@app.route('/', methods=['GET', 'POST'])
def initialise():
    global history

    if request.method == 'GET':
        response = AI_Response.getResponse("In two sentances or less, introduce yourself as  BOT-T, who will answer and questions about Max or his cv in plain text") #test basic ai response
        history = response['history']
        return render_template('home.html', response=response['text'])
    
    if request.method == 'POST':
        print("###################################################################")
        print(request.form['input'])
        response = AI_Response.getResponse(request.form['input'], history) #answer user question
        history = response['history']
        #return render_template('home.html', response=response['text'])
        return jsonify({'response': response['text']})

if __name__ == '__main__':
    app.run(host='localhost', port = 80) #use port 80 to make link "localhost"