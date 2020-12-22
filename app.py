from flask import Flask, render_template
from func import *

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/')
def home():
    """
    Get user details for the current user
    :return:
    """
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def api():
    """
    Store user details into a csv file

    :return:
    """
    return render()


@app.route('/login')
def login():
    """
    Get login details from the new user
    :return:
    """
    return render_template("login.html")


@app.route('/login/check', methods=['GET', 'POST'])
def logged():
    """
    Check the new user details with the stored csv file
    :return:
    """
    return check()


if __name__ == '__main__':
    app.run()
