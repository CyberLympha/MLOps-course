import pickle
import pandas as pd

df = pd.read_csv("/home/stage-srv/Titanic/datasets/stage4/test.csv")
X = df.iloc[:,[1,2,3]]
y = df.iloc[:,0]

def test1():
    with open("/home/stage-srv/Titanic/models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
    score = clf.score(X, y)
    assert score > 0.75

