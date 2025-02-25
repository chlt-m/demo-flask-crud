import os
from flask import Flask , render_template ,request
from .crud import add_note, get_note, delete_note, update_note

# กรณีแยก path templates
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # หาตำแหน่งของไฟล์ app.py
# TEMPLATE_DIR = os.path.join(BASE_DIR,'..','templates')  # ระบุ path ไปยัง templates/

app =  Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/add_note',methods=['POST'])
def route_add_note():
    data = request.get_json()
    result = add_note(data)
    return result

@app.route('/get_note',methods=['GET'])
def route_get_note():
    notes = get_note()
    return notes

@app.route('/delete_note/<id>',methods=['DELETE'])  
def route_delete_note(id):
    result = delete_note(id)
    return result  

@app.route('/update_note/<id>',methods=['PUT'])
def route_update_note(id):
    data = request.get_json()
    result = update_note(id,data)
    return result

