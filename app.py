from flask import Flask,render_template,url_for,request

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 


import pickle

app = Flask(__name__)

random = pickle.load(open('random_fake.pkl','rb'))
clf_gini = pickle.load(open('decision_fake.pkl','rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset)
        return render_template("preview.html",df_view = df)


@app.route('/prediction')
def prediction():
    return render_template("prediction.html")

@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        Profile = request.form['Profile']
        Length_Username = request.form['Length_Username']
        Fullname = request.form['Fullname']
        Length_Fullname = request.form['Length_Fullname']
        Name = request.form['Name==Username'] 
        Description_Length = request.form['Description_Length']
        External_URL = request.form['External_URL']
        Account_Private = request.form['Account_Private']
        Total_Posts = request.form['Total_Posts']
        Total_Followers = request.form['Total_Followers']
        Total_Follows = request.form['Total_Follows']
        
        
        model = request.form['model']
        
		# Clean the data by convert from unicode to float 
        
        sample_data = [Profile,Length_Username,Fullname,Length_Fullname,Name,Description_Length,External_URL,Account_Private,Total_Posts,Total_Followers,Total_Follows]
        # clean_data = [float(i) for i in sample_data]
        # int_feature = [x for x in sample_data]
        int_feature = [float(i) for i in sample_data]
        print(int_feature)
    

		# Reshape the Data as a Sample not Individual Features
        
        ex1 = np.array(int_feature).reshape(1,-1)
        print(ex1)
		# ex1 = np.array([6.2,3.4,5.4,2.3]).reshape(1,-1)

        # Reloading the Model
        if model == 'RandomForestClassifier':
           result_prediction = random.predict(ex1)
           
            
        elif model == 'DecisionTreeClassifier':
          result_prediction = clf_gini.predict(ex1)
           
           
        
        if result_prediction ==1:
            result = 'Fake'
        else:
            result = 'Real'    

          

    return render_template('prediction.html', prediction_text= result, model = model)

@app.route('/performance')
def performance():
    return render_template("performance.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")    

if __name__ == '__main__':
	app.run(debug=True)
