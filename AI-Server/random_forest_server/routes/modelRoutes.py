import json
from flask import Blueprint, jsonify, request, abort, Response, session, redirect, url_for, make_response
from ..controller.modelController import importModels, importScaler, loadData, getPredictions
import joblib
import pandas as pd
model = Blueprint('model', __name__)




@model.route("/predict", methods=["POST"])
def testModel():
    data = request.get_json()
    data = data["stats"]
    
    
    models = importModels()
    scaler = importScaler()
    
    input_df = pd.DataFrame([data])
    
    
    df = loadData()
    
    predictions = getPredictions()
    return make_response(jsonify({'result': predictions}))
    
    
