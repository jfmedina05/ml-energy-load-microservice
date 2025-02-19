import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

def txtfile(filename):
    with open(filename) as readfile:
     words = readfile.read().split()
    return words

