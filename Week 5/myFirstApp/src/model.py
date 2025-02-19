from sklearn import datasets
from joblib import load
import numpy as np
import json

from flask import request, jsonify
import pandas as pd
UPLOAD_FOLDER='.'

#This will return a string with information about this model
def model_info():
    return 'This model is a Random Forest Regression Model to an Energy Efficiency Dataset'

#This will allow a file to be uploaded (it is used in file_predict)
def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

#This function will load a model in the app directory, read in the csv
#test data provided by the upload and return a jsonified list of 
#predictions from the test data set given.
def file_predict(filename):
    my_model = load('logs_heart_mdl.pkl')
    name = upload(filename)
    test_data = pd.read_csv(name, index_col =[0])
    test_np = test_data.to_numpy()
    pred = my_model.predict(test_np)
    pred_list = pred.tolist()
    json_str = json.dumps(pred_list)
    return json_str
