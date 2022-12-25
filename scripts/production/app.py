from flask import Flask, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello from Flask!")

@app.route("/predict/<int:pclass>/<int:sex>/<int:age>")
def predict(pclass, sex, age):
    with open("/home/prod-srv-admin/Titanic/models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
    prediction = int(clf.predict([[pclass, sex, age]])[0])
    return(jsonify({"survived": prediction}))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=55555)
