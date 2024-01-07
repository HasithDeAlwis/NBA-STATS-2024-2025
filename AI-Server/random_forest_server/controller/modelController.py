from flask import make_response, jsonify
import joblib
import json
import os
import pandas as pd

def getFolderPath():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'Models')
    return folder_path

def importModels():
    folder_path = getFolderPath()
    models = {}
    file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    for file in file_names:
        key = file[:3]
        models[key] = loadModel(folder_path, file)
    return models

def importScaler():
    folder_path = getFolderPath()
    scaler_path = os.path.join(folder_path, 'scaler.joblib')
    return joblib.load(scaler_path)

def loadData():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(folder_path, "all_players_stats.csv")
    data = pd.read_csv(data_path)
    return data

def loadModel(folder_path, file):
    model_path = os.path.join(folder_path, file)
    model = joblib.load(model_path)
    return model

def getPredictions():
    
    
    predictors_ast = ['GS', 'MP', 'FG', 'FGA', '3PA', '2P', '2PA', 'FT', 'FTA', 'AST', 'STL',
                'TOV', 'PTS', 'MP_total', 'FGA_36', 'FT_36', 'AST_36', 'TOV_36',
                'PTS_36', 'FGA_100', 'AST_100', 'TOV_100', 'PTS_100', 'AST%', 'USG%',
                'OWS', 'WS', 'OBPM', 'BPM', 'VORP']
    
    
    
    df = df[predictors_ast]
    
    df = pd.concat([df, input_df], ignore_index = True)
    max, min = df['AST'].max(), df['AST'].min()

    df_scaled = pd.DataFrame(scaler.fit_transform(df).copy())

    prediction = models["ast"].predict(df_scaled.tail(1))
    return {"ast": prediction[0] * (max - min) + min}