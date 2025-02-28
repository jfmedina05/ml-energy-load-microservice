from sklearn import datasets
from joblib import load
import numpy as np
import json
from flask import Flask, send_file, render_template
import os
import io
from flask import request, jsonify
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt

# Functions in this file assume there is a file available in directory on the server
# to provide images.

# This function takes in the name of the file to be read (input as a query parameter)
# This file should be present on the server.
# It then reads a CSV file, generates a histogram plot from the data, and saves the plot
# as a PNG image in a BytesIO object. The image is then returned as a BytesIO object.
# A BytesIO object is a binary stream that allows data transmission to be more efficient.
def gen_plot(filename):
    try:
        # This will look for a file ALREADY on the server
        # with the name entered in the query parameter - called filename.
        name = request.args.get('filename') # this is the name of the query parameter
        if not name:
            return jsonify({"error": "Invalid input"}), 405
        test_data = pd.read_csv(name, index_col =[0])
        test_data.plot(kind='hist').get_figure()    #Change this if you want!
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format = 'png')
        bytes_image.seek(0)
        return bytes_image
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

# This function takes in the name of the file to be read (input as a query parameter)
# This file should be present on the server.
# This function generates a plot using the gen_plot function and returns the image as a response
# with MIME (Multipurpose Internet Mail Extensions ) type 'image/png'.
# Example of MIME types are 
# text/html: HTML document 
# image/jpeg: JPEG image
# application/json: JSON data
# application/pdf: PDF document
# JSON is usually text while BINARY FILES are usually for images (Flask send_file)
# Hence, it returns a Flask response object containing the image data with MIME type 'image/png'.
def disp_plot(filename):
    plot = gen_plot(filename)
    return send_file(plot, mimetype='image/png')

# This function takes in the name of the file to be read (input as a query parameter)
# This file should be present on the server.
# This function reads a CSV file, generates a histogram plot from the data, saves the plot as a PNG
# image in the 'static/images' directory, and renders the 'new.html' template to display the image.
# Then, it returns a Flask response object rendering the 'new.html' template.
def html(filename):
    try:
        # This will look for a file ALREADY on the server
        # with the name entered in the query parameter - called filename.
        name = request.args.get('filename')  # this is the name of the query parameter
        if not name:
            return jsonify({"error": "Invalid input"}), 400
        
        test_data = pd.read_csv(name, index_col=[0])
        plot = test_data.plot(kind='hist').get_figure()
        plot_path = os.path.join('static', 'images', 'plot.png')    #Change this if you want!
        plot.savefig(plot_path)
        return render_template('new.html')
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 400
    

#This function returns a Flask response object rendering 
# the 'hello_template.html' template.
def html_hello():
    return render_template('hello_template.html')
