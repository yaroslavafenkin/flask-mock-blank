from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '{"ping":"pong"}'

@app.route('/post', methods = ['POST'])
def howToPost():
    return 'Handle agrs like https://stackoverflow.com/a/25268170'
