<<<<<<< HEAD
from re import M
from flask import *
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model2.pkl', 'rb'))

app = Flask(__name__)
=======
from flask import flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = flask(__name__)
>>>>>>> 2b3d670a56ebad3eb2217685c3b871c1ab95beac

@app.route('/')
def main():
    return render_template('formfilling.html')


<<<<<<< HEAD
@app.route('/predict', methods=['GET','POST'])
def predict():
    data1 = request.form['dur']
    data2 = request.form['dif']
    data3 = request.form['rew']
    data4 = request.form['tot']
    data5 = request.form['age']
    data6 = request.form['sex']
    age = [0,0,0,0,0,0,0,0,0,0]
    sex = [0,0,0]
    if(data5 == "10"):
        age = [1,0,0,0,0,0,0,0,0,0]
    elif(data5 == "20"):
        age = [0,1,0,0,0,0,0,0,0,0]
    elif(data5 == "30"):
        age = [0,0,1,0,0,0,0,0,0,0]
    elif(data5 == "40"):
        age = [0,0,0,1,0,0,0,0,0,0]
    elif(data5 == "50"):
        age = [0,0,0,0,1,0,0,0,0,0]
    elif(data5 == "60"):
        age = [0,0,0,0,0,1,0,0,0,0]
    elif(data5 == "70"):
        age = [0,0,0,0,0,0,1,0,0,0]
    elif(data5 == "80"):
        age = [0,0,0,0,0,0,0,1,0,0]
    elif(data5 == "90"):
        age = [0,0,0,0,0,0,0,0,1,0]
    elif(data5 == "100"):
        age = [0,0,0,0,0,0,0,0,0,1]

   
    if(data6 == "m"):
        sex = [1,0,0]
    elif(data6 == "f"):
        sex = [0,1,0]
    else:
        sex = [0,0,1]
    arr = []
    arr.extend(sex)
    arr.extend(age)
    arr.extend([data2, data1, data3, data4])
   # arr.reshape(1,-1)

    input_values = pd.DataFrame([arr],columns=['F','M','O','age_10s','age_20s','age_30s','age_40s','age_50s','age_60s','age_70s','age_80s','age_90s','age_100s','difficulty','duration','reward','total_amount'])

    pred = model.predict(input_values)[0]
=======
@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['dur']
    data2 = request.form['def']
    data3 = request.form['rew']
    data4 = request.form['tot']
    data5 = request.form['age']
    data6 = request.form['mal']
    arr = np.array({[data1, data2, data3, data4, data5, data6]})
    pred = model.predict(arr)
>>>>>>> 2b3d670a56ebad3eb2217685c3b871c1ab95beac
    return render_template('after.html', data = pred)

if __name__ == "__main__":
    app.run(debug=True)