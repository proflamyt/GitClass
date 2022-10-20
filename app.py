from flask import Flask, session, request
app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return {
            "message": "Go back to a Post requst"
        }
    username = request.json['username']
    password = request.json['password']

    session['username'] = username

    return {
        "message": "you are already registered"
    }


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return {
            "message": "Go back to a post requst"
        }
    # username = request.json['username']
    # password = request.json['password']

    return {
        "message": session['username']
    }

