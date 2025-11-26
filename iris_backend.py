from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Correct model loading
model = joblib.load("C:\\Users\\hp\\PyCharmMiscProject\\git\\KNN_classifier_iris\\Knn_model.pkl")

@app.route('/')
def home():
    return render_template("Iris.html")

@app.route('/predict', methods=['POST'])
def predict():
    f1 = float(request.form['f1'])
    f2 = float(request.form['f2'])
    f3 = float(request.form['f3'])
    f4 = float(request.form['f4'])

    df = pd.DataFrame([[f1, f2, f3, f4]],
                      columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)'])

    output = model.predict(df)[0]

    return render_template("Iris.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)






'''
from flask import Flask,render_template,request
import joblib


app = Flask(__name__)

model = joblib.load("C:\\Users\\hp\\PyCharmMiscProject\\git\\KNN_classifier_iris\\Knn_model.pkl","rb")

@app.route('/')
def home():
    return render_template("Iris.html")

@app.route('/predict',methods=['POST'])
def predict():
    f1 = float(request.form['f1'])
    f2 = float(request.form['f2'])
    f3 = float(request.form['f3'])
    f4 = float(request.form['f4'])

    input_data = [[f1,f2,f3,f4]]
    output = model.predict(input_data)[0]

    return render_template("Iris.html",result=output)


if __name__ == "__main__":
    app.run(debug=True)
'''