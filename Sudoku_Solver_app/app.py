from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import cv2
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
from Sudoku_Solver_Python.Solver import solver

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return "Check"

@app.route("/",methods=['POST'])
def solve_puzzle():
    puzzle_img = cv2.imdecode(np.fromstring(request.files['user-file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    solved_img = solver(puzzle_img)
    im = Image.fromarray(solved_img)
    data = BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template('test.html',solved_shape =encoded_img_data.decode('utf-8'))
    
if __name__ == "__main__":
    app.run(debug=True)