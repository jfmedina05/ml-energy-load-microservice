from sklearn import datasets
from joblib import load
import numpy as np
import json
from sklearn.metrics import classification_report
from flask import request, jsonify
import pandas as pd

# This function returns a string with model information.
def model_info():
    return 'This service uses a random forest regressor.'

UPLOAD_FOLDER = '.'

#UPDATES: This will allow you to be flexible with your uploads
#The old upload() function was tied closely to the file_predict()
#This function looks at the file_key (the name of the file in the request body)
# in the yml file. For example, filename in the /prediction endpoint
# and file_x and file_y in the /performance endpoint.
def upload(file_key):
    if file_key not in request.files:
        raise KeyError(f"File key '{file_key}' not found in request.files")
    f = request.files[file_key]
    filename = f.filename
    filepath = f"{UPLOAD_FOLDER}/{filename}"
    f.save(filepath)
    return filepath

#DEPRECATED: This will allow a file to be uploaded (it is used in file_predict)
#It looks at the request body (file key) to the get contents and names
# it whatever the query parameter was (filename). Note this function
# requires a post with a query parameter and multipart/form data in the request body
#def upload_old(filename):
    #f = request.files[file_key]
    #filename = f.filename
    #f.save(filename)
    #return filename

#This function will load a model in the app directory, read in the csv
#test data provided by the upload and return a jsonified list of 
#predictions from the test data set given.
#UPDATES: Note that the query parameters from the yml file have been 
# removed from the /prediction endpoint. Instead, it will look only
# at the name of the file that is selected for upload (and communicated
# as part of the request body - it is called 'file'). Hence, they have
#have been commented below.
def file_predict():
    try:
        #filename = request.args.get('filename')
        #if not filename:
        #    return jsonify({"error": "Invalid input"}), 405

        my_model = load('rfr.pkl')
        name = upload('file') #this is the name of the object in the request body
        test_data = pd.read_csv(name, index_col =False)
        test_np = test_data.to_numpy()
        pred = my_model.predict(test_np)
        pred_list = pred.tolist()
        json_str = json.dumps(pred_list)
        return json_str
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

#This function will load a model in the app directory, read in x and y test
# data. Once performing the evaluation, it will return the accuracy.
#Note that the filename_x and filename_y query parameters ARE REMOVED from the
#endpoint in the yml file. Hence, they have been commented out below.
def model_accuracy():
    try:
        #filename_x = request.args.get('filename_x')
        #filename_y = request.args.get('filename_y')
        
        #if not filename_x or not filename_y:
        #    return jsonify({"error": "Invalid input"}), 405
        
        name_x = upload('file_x') #this is the name of the object in the request body
        name_y = upload('file_y') #this is the name of the object in the request body
        
        my_model = load('rfr.pkl')
        x_test = pd.read_csv(name_x, index_col= False)
        x_test_np = x_test.to_numpy()
        y_test = pd.read_csv(name_y, index_col= False)
        y_test_np = y_test.to_numpy()
        
        accuracy = my_model.score(x_test_np, y_test_np)

        return jsonify({"accuracy": accuracy}), 200
    
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
   
# This function will take an existing file uploaded to the server and
# run it through the current model, producing a list of predictions.
# This does not require an upload UNLESS there is no data files on the server.
def predict_only(filename):
    try:
        # This will look for a file ALREADY on the server
        # with the name entered in the query parameter - called filename.
        name = request.args.get('filename') # this is the name of the query parameter
        if not filename:
            return jsonify({"error": "Invalid input"}), 405
        
        my_model = load('rfr.pkl')
        test_data = pd.read_csv(name, index_col = False)
        test_np = test_data.to_numpy()
        pred = my_model.predict(test_np)
        pred_list = pred.tolist()
        json_str = json.dumps(pred_list)
        return json_str
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

def html(filename):
    try:
        name = request.args.get('filename')
        if not name:
            return jsonify({"error": "Invalid Input"}), 405
        test_data = pd.read_csv(name, index_col= False)
        plot = test_data.plot(kind='hist').get_figure()
        plot_path = os.path.join('static', 'image', 'plot.png')
        plot.savefig(plot_path)
        return render_template('new.html')
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

def html_hello():
    return render_template("Hello_template.html")
        
