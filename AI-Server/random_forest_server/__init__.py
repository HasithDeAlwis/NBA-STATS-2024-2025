from flask import Flask, jsonify, make_response
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

#set up flask app
app = Flask(__name__)
CORS(app)

#arbritary secrete key 
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")