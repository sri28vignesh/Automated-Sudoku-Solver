from flask import Flask, render_template, request,jsonify
import numpy as np
import cv2
import base64
from Sudoku_Solver_Python.Solver import solver

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/solve_puzzle", methods=['POST'])
def solve_puzzle():
    if request.method == "POST":    
        resp = request.get_json('img_res')
        resp = resp['img_res']
        start_index = resp.find(',')
        if resp:
            im_bytes = base64.b64decode(resp[start_index+1:])
            im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
            puzzle_img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

            solved_img = solver(puzzle_img)
            if solved_img == 'No Puzzle Found':
                return jsonify(res='No Puzzle Found, please use proper sudoku puzzle image')
            if solved_img == 'No Solution Found':
                return jsonify(res='No Solution Found')            
            img,buffer = cv2.imencode('.jpeg',solved_img)

            encoded_img_data = base64.b64encode(buffer)    
            sol_res = encoded_img_data.decode('utf-8')
            return jsonify(res=sol_res)
        else:
            return "No response"

if __name__ == "__main__":
    app.run(debug=True)