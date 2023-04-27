from flask import Flask, render_template, request
from chatbot import getResponse, predictClass

intents = json.loads(open('intents.json').read())
app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        # ints = predictClass(message)
        # res = getResponse(ints, intents)
        # return render_template('index,html', message=message, response=res)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
