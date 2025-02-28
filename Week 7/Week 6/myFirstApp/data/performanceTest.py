#Before trying to create an endpoint that takes in a file
#and makes a prediction, it is a good idea to make sure that
#you have the function working OUTSIDE of the client/server communication.
#Make sure your CSV files are read properly by your model methods.

from sklearn import datasets
from joblib import load
import numpy as np
import json
from sklearn.metrics import classification_report
from flask import request, jsonify
import pandas as pd
from werkzeug.utils import secure_filename

#This function will load a model in the app directory, read in the csv
#test data provided by the upload and return a jsonified list of 
#predictions from the test data set given.
def model_accuracy(filename_x,filename_y):
    my_model = load('my_save_mdl.pkl')
    x_test = pd.read_csv(filename_x, index_col =[0])
    y_test = pd.read_csv(filename_y, index_col =[0])
    accuracy =my_model.score(x_test,y_test)
    return accuracy

print(model_accuracy("x_train3.csv","y_train3.csv"))
