from flask import Flask, jsonify, make_response, request, session
import os
from dotenv import load_dotenv
from flask_cors import CORS
from .routes.modelRoutes import model
from .controller.modelController import importModels

load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

#set up flask app
app = Flask(__name__)
CORS(app)

app.register_blueprint(model, url_prefix="/api/model")


#arbritary secrete key 
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")