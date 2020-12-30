from flask import Flask, redirect, render_template, request, url_for, Response, make_response
import numpy as np
import requests
import cv2
import base64
from Sudoku_Solver_Python.Solver import solver

app = Flask(__name__)
sol_res = None

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return "Check"

@app.route("/get-solved-res")
def get_solved_img():
    global sol_res
    res = sol_res
    resp = {'resp': res}
    return resp

@app.route("/",methods=['POST'])
def solve_puzzle():
    global sol_res
    puzzle_img = cv2.imdecode(np.fromstring(request.files['user-file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    solved_img = solver(puzzle_img)
    img,buffer = cv2.imencode('.jpeg',solved_img)
    encoded_img_data = base64.b64encode(buffer)

    orig_img,orig_buffer= cv2.imencode('.jpeg',puzzle_img)
    encoded_orig_data = base64.b64encode(orig_buffer)
    
    sol_res = encoded_img_data.decode('utf-8')
    org_res = encoded_orig_data.decode('utf-8')

    return render_template('index.html', solved_image = sol_res, orig_image = org_res)

if __name__ == "__main__":
    app.run( debug=True)
    