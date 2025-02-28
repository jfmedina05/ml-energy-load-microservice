from sklearn import datasets
from joblib import load
import numpy as np
import json
import matplotlib.pyplot as plt
from flask import Flask, send_file, render_template
import os
import io
from flask import request, jsonify
import pandas as pd
import matplotlib
matplotlib.use('Agg')

UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

def gen_plot(name):
    #test_data = pd.read_csv(name)#, index_col=[0])
    #fig = test_data.plot(kind='hist').get_figure()
    #bytes_image = io.BytesIO()
    #fig.savefig(bytes_image, format = 'png')
    #bytes_image.seek(0)
    #return bytes_image
    try:
        #my_model = load('rfr.pkl')
        name = request.args.get('name')
        if not name:
            return jsonify({"error": "Invalid Input"}), 405
    # HARD CODED test in here so when I upload I must name my file test
        test_data = pd.read_csv(name, index_col= False)
        test_data.plot(kind='hist').get_figure()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format = 'png')
        bytes_image.seek(0)
        return bytes_image
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

def disp_plot(name):
    plot = gen_plot(name)
    #plot.savefig(os.path.join('static', 'images', 'plot_test.png'))
    #return render_template('test.html')
    return send_file(plot, mimetype='image/png')

def html(name):
    test_data = pd.read_csv(name, index_col = False)
    plot = test_data.plot(kind='hist').get_figure()
    plot.savefig(os.path.join('static', 'images', 'plot_test.png'))
    return render_template('new.html')

def html_hello():
    return render_template('hello_template.html')
