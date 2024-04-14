import pandas as pd
import json
from datetime import datetime, timedelta
class weather_forecast:
    def get_data():
        responses ={}
        try:
            with open("model/weather-forecast/data-prediksi.json") as data_file:
                data = json.load(data_file)  
            
            responses['status'] = 200
            responses['message'] = "Success"
            responses['body'] = data  
        except Exception as e:
            responses['status'] = 500
            responses['message'] = "Bad Gateway"
            responses['body'] = e 
        return responses