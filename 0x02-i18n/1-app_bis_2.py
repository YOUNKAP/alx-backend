#Badel config from file
from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
#app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    '''default route'''
    return render_template("1-index.html",)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
