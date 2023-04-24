from flask import Flask, render_template

app = Flask()

@app.route('/')
def chat():
        print("Hello World!")



if __name__ == __main__:
        app.run(debug=True)