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
    try:
        return jsonify(chatbotcontroller.get_respon(data['question']))
    except Exception as e:
        er = {}
        er['status'] = "500"
        er['message'] = "Bad Gateway"
        er['body'] = e
        return er

@bp.route('/weather-forecast/get-data')
def about():
    return weather_forecast.get_data()