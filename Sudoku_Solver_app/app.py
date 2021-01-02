from flask import Flask, render_template, request
import numpy as np
import cv2
import base64
from Sudoku_Solver_Python.Solver import solver

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get-solved-res")
def solve_puzzle():
    resp = request.args.get('jsdata')
    start_index = resp.find(',')
    if resp:
        im_bytes = base64.b64decode(resp[start_index+1:])
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
        puzzle_img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

        solved_img = solver(puzzle_img)
        if solved_img == 'No Puzzle Found':
            return 'No Puzzle Found, please use proper sudoku puzzle image'
        if solved_img == 'No Solution Found':
            return 'No Solution Found'            
        img,buffer = cv2.imencode('.jpeg',solved_img)

        encoded_img_data = base64.b64encode(buffer)    
        sol_res = encoded_img_data.decode('utf-8')
        return render_template('result.html', solved_image = sol_res)
    else:
        return "No response"

if __name__ == "__main__":
    app.run( debug=False)