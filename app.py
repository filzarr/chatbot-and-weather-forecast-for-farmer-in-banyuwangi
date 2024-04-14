from flask import Flask
from routes import bp as main_bp
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
app = Flask(__name__)
app.register_blueprint(main_bp) 
app.run()