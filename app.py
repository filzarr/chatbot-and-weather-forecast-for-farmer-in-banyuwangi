from flask import Flask, render_template, request
import tensorflow as tf
import pandas as pd
import numpy as np 
from tensorflow.keras.preprocessing.sequence import pad_sequences 
import random
import json
import string
import pickle
app = Flask(__name__)
app.static_folder = 'static'
model = tf.keras.models.load_model('model/chatbot/models.h5') 

with open("model/chatbot/data-chatbot.json") as data_file:
    data1 = json.load(data_file) 
text_input = []
intents = []
responses={}

for intent in data1['intents']:
    responses[intent['tag']] = intent['responses']
for pattern in intent['patterns']:
    text_input.append(pattern)
    intents.append(intent['tag'])

df = pd.DataFrame({'text_input': text_input,
                    'intents': intents})
print(responses['sapaan'])
with open('model/chatbot/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('model/chatbot/label_encoder.pickle', 'rb') as label:
    le = pickle.load(label)     

@app.route("/")
def home():  

    while True: 

            texts_p = []
            prediction_input = input('You : ') 
            print(prediction_input)
            prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
            print(prediction_input)
            prediction_input = ''.join(prediction_input)
            print(prediction_input)
            texts_p.append(prediction_input)
            print(prediction_input)
            prediction_input = tokenizer.texts_to_sequences(texts_p)
            print(prediction_input)

            prediction_input = tokenizer.texts_to_sequences(texts_p)
            print(prediction_input)
            prediction_input = np.array(prediction_input).reshape(-1)
            print(prediction_input)
            prediction_input = pad_sequences([prediction_input], maxlen=10,
                                    padding='post', truncating='post')
            
            output = model.predict(prediction_input)
            output = output.argmax()    
            response_tag = le.inverse_transform([output])[0]
            # output = model.predict(texts_p)
            print("Dokter AI : ",random.choice(responses[response_tag]))
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()