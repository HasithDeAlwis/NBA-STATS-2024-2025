from flask import make_response, jsonify
import joblib
import json
import os
import pandas as pd

def getPredictors(stat):
    all_predictors = {
        "ast": ['GS', 'MP', 'FG', 'FGA', '3PA', '2P', '2PA', 'FT', 'FTA', 'AST', 'STL',
        'TOV', 'PTS', 'MP_total', 'FGA_36', 'FT_36', 'AST_36', 'TOV_36',
        'PTS_36', 'FGA_100', 'AST_100', 'TOV_100', 'PTS_100', 'AST%', 'USG%',
        'OWS', 'WS', 'OBPM', 'BPM', 'VORP'],
        
        "pts": ['GS', 'MP', 'FG', 'FGA', '2P', '2PA', 'FT', 'FTA', 'AST', 'STL', 'TOV',
        'PTS', 'MP_total', 'FG_36', 'FGA_36', 'FT_36', 'FTA_36', 'PTS_36',
        'FG_100', 'FGA_100', 'FT_100', 'FTA_100', 'PTS_100', 'PER', 'USG%',
        'OWS', 'WS', 'OBPM', 'BPM', 'VORP'],
        
        "trb": ['GS', 'MP', 'FG', '2P', '2PA', 'FTA', 'ORB', 'DRB', 'TRB', 'BLK', 'PF',
        'PTS', 'FG%_36', '2P_36', 'ORB_36', 'DRB_36', 'TRB_36', 'FG%_100',
        '2P_100', 'ORB_100', 'DRB_100', 'TRB_100', 'PER', 'ORB%', 'DRB%%',
        'TRB%', 'OWS', 'DWS', 'WS', 'VORP'],
        
        "stl": ['GS', 'MP', 'FG', 'FGA', '3PA', '2P', '2PA', 'FT', 'FTA', 'AST', 'STL',
        'TOV', 'PTS', 'MP_total', 'AST_36', 'STL_36', 'FT_100', 'AST_100',
        'STL_100', 'PTS_100', 'PER', 'AST%', 'STL%%', 'USG%', 'OWS', 'DWS',
        'WS', 'OBPM', 'BPM', 'VORP'],
        "blk": ['FG%', '2P', 'ORB', 'DRB', 'TRB', 'BLK', 'PF', 'FG%_36', '3PA_36',
        '2P_36', 'ORB_36', 'DRB_36', 'TRB_36', 'BLK_36', 'FG%_100', '3PA_100',
        '2P_100', 'ORB_100', 'DRB_100', 'TRB_100', 'BLK_100', 'DRtg', 'PER',
        '3PAr', 'ORB%', 'DRB%%', 'TRB%', 'BLK%', 'DWS', 'WS'],
        "fgp": ['FG%', '2P%', 'eFG%', 'ORB', 'DRB', 'TRB', 'BLK', 'FG%_36', '2P%_36',
        'ORB_36', 'DRB_36', 'TRB_36', 'BLK_36', 'FG%_100', '2P%_100', 'ORB_100',
        'DRB_100', 'TRB_100', 'BLK_100', 'ORtg', 'PER', 'TS%', 'ORB%', 'DRB%%',
        'TRB%', 'BLK%', 'WS', 'WS/48', 'BPM', 'teamPPG'],
        "3pp": ['3P', '3PA', '3P%', 'FT%', 'ORB', '3P_36', '3PA_36', '3P%_36', 'FT%_36',
        'ORB_36', 'DRB_36', 'TRB_36', 'BLK_36', 'PF_36', 'FG%_100', '3P_100',
        '3PA_100', '3P%_100', 'FT%_100', 'ORB_100', 'DRB_100', 'TRB_100',
        'BLK_100', 'PF_100', '3PAr', 'FTr', 'ORB%', 'DRB%%', 'TRB%', 'BLK%']
    }
    return all_predictors[stat]

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

def getPredictions(input_df):
    
    df = loadData()
    scaler = importScaler()
    models = importModels()
    stats = ["ast", "pts", "blk", "trb", "stl", "3pp", "fgp"]
    
    for stat in stats:
        predict_stats(stat, scaler, models, df, input_df)
    return "attempted"

def predict_stats(stat, scaler, models, df, input_df):
    predictors = getPredictors(stat)
    for column in df.columns:
        print(column)
    df = df[predictors]
    merged = pd.concat([df, input_df[predictors]], axis=0)
    df_scaled = scaler.fit_transform(merged).copy()
    df_scaled = pd.DataFrame(df_scaled, columns=predictors)
    scaled_input = df_scaled.tail(1)   
    print(scaled_input)
    models[stat].predict(scaled_input)
    