import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ...again'

if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)    ##this allows changes to be picked up by browser, will also producr bug reports in the event of a bug##

            