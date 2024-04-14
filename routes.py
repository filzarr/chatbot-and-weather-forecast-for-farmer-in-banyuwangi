from flask import Blueprint
from flask import render_template,request,jsonify
from controllers import *
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/get-answer', methods=['POST'])
def get_answer():
    data = request.json
    return jsonify(chatbotcontroller.get_respon(data['question']))

@bp.route('/about')
def about():
    return 'Ini adalah halaman about'