from sklearn import datasets
from joblib import load
import numpy as np
import json
from flask import request, jsonify
import pandas as pd
from sklearn.metrics import classification_report

#This will return a string with information about this model
def model_info():
    return 'This model is a Random Forest Regression Model to an Energy Efficiency Dataset'

UPLOAD_FOLDER = '.'

#This will allow a file to be uploaded (it is used in file_predict)
def upload(file_key):
    if file_key not in request.files:
        raise KeyError(f"The File Key '{file_key}' was not found in request.files"
    f = request.files[file_key]
    filename = f.filename
    filepath = f"{UPLOAD_FOLDER}/{filename}"
    f.save(filepath)
    return filepath

#This function will load a model in the app directory, read in the csv
#test data provided by the upload and return a jsonified list of 
#predictions from the test data set given.
def file_predict(filename):
    try:

        my_model = load('rfr.pkl')

        name = upload(filename)
        test_data = pd.read_csv(name, index_col =[0])
        test_np = test_data.to_numpy()
        pred = my_model.predict(test_np)
        pred_list = pred.tolist()
        json_str = json.dumps(pred_list)
        return json_str
    except KeyError as e:
        return jasonify({"error": str(e)}), 400

def predict_only(filename):
    try:
        

        name = request.args.get('filename')
        if not filename:
            return jsonify({"error": "Invalid input"}), 405

        my_model = load('rfr.pkl')
        test_data = pd.read_csv(name, index_col = [0])
        test_np = test_data.to.numpy()
        pred = my_model.predict(test_np)
        pred_list = pred.tolist()
        json_str = json.dumps(pred_list)
        return json_str
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

def model_accuracy():
    try:
        name_x = upload('file_x')
        name_y = upload('file_y')

        my_model = load('rfr.pkl')
        x_test = pd.read_csv(name_x, index_col=[0])
        x_test_np = x_test.to_numpy()
        y_test = pd.read_csv(name_y, index_col[0])
        y_test_np = y_test.to_numpy()

        accuracy = my_model.score(x_test_np, y_test_np_

        return jsonify(({"accuracy": accuracy}), 200

    except KeyError as e:
        return jsonify({"error": str(e)}), 400
