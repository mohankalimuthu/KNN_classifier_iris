from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

#model = pickle.load(open("Knn_model.pkl","rb"))

@app.route('/')
def home():
    return render_template("Iris.html")

@app.route('/predict',methods=['POST'])
def predict():


if __name__ == "__main__":
    app.run(debug=True)