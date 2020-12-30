from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import cv2
from io import BytesIO
import base64
import matplotlib.pyplot as plt
'''import sys
sys.path.append("./../Sudoku_Solver_Python")'''
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
    figfile = BytesIO()
    #plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png
    return render_template('test.html',solved_shape = result)
    
if __name__ == "__main__":
    app.run(debug=True)