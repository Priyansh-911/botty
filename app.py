import json
from flask import Flask, render_template, request
from chatbot import getResponse, predictClass

intents = json.loads(open('intents.json').read())
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot2.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        ints = predictClass(message)
        res = getResponse(ints, intents)
        return render_template('chatbot2.html', message=message, response=res)

    else:
        return render_template('chatbot2.html')


if __name__ == '__main__':
    app.run()
