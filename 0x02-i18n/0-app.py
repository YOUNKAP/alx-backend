#!/usr/bin/python3
""" Basic Flask app """
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
