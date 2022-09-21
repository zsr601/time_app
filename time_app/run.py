import time
from flask import Flask
app = Flask(__name__)

@app.route('/time')
def t():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

@app.route('/')
def hello_world():
    return 'Hello world!'

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
