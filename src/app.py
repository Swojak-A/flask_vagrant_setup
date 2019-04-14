#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
# app.debug = True

@app.route("/")
def hello():
    return "<h1 style='color:darkcyan;'>Hellix There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
