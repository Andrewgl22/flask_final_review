from flask import Flask
# creates our flask app
app = Flask(__name__)
# the secret key is required for session to work
app.secret_key = "shhhhh"