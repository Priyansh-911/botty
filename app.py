import json
from flask import Flask, render_template, request
from chatbot import getResponse, predictClass

intents = json.loads(open('intents.json').read())
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot2.html')
def index():
    return render_template('chatbot2.html')

@app.route('/get-response', methods=['GET', 'POST'])
def chat():
    message = request.form['msg']
    ints = predictClass(message)
    res = getResponse(ints, intents)
    return res

@app.route('/about-us')
def us():
    return render_template('ABOUT US.html')



if __name__ == '__main__':
    app.run()
