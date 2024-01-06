require 'rubypython'
RubyPython.start(:python_exe => '/Library/Frameworks/Python.framework/Versions/3.11/bin/python3') # Specify the correct path to your Python interpreter

# Define a Python function to load the model
python_code = <<-PYTHON
import joblib

def model_pts(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/pts_model.joblib'
    pts_model = joblib.load(path)
    models['PTS'] = pts_model
    return models 

def model_ast(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/ast_model.joblib'
    ast_model = joblib.load(path)
    models['AST'] = ast_model
    return models 

def model_trb(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/trb_model.joblib'
    trb_model = joblib.load(path)
    models['TRB'] = trb_model
    return models 

def model_stl(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/stl_model.joblib'
    stl_model = joblib.load(path)
    models['STL'] = stl_model
    return models 

def model_blk(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/blk_model.joblib'
    blk_model = joblib.load(path)
    models['BLK'] = blk_model 
    return models

def model_3p(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/3_point_percentage_model.joblib'
    fg_3_model = joblib.load(path)
    models['FG3'] = fg_3_model 
    return models

def model_2p(models):
    path = '/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/Projects/NBA_2024_2025/NBA-STATS-2024-2025/Rails_App/app/controllers/Models/2_point_percentage_model.joblib'
    fg_model = joblib.load(path)
    models['FG'] = 2_point_model
    return models
 

def load_all_models():
    models = {}
    models = model_pts(models)
    models = model_ast(models)
    models = model_trb(models)
    models = model_blk(models)
    models = model_stl(models)
    models = model_2p(models)
    models = model_3p(models)
    return models
PYTHON

#Load all the models into a dictionary
models_dict = RubyPython.eval('load_all_models')

#save the models into a global variable
$nba_models = models_dict

at_exit do
    RubyPython.stop
end

