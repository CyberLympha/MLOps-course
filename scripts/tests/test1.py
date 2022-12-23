import os
import sys
import pickle
import json

import pandas as pd

df = pd.read_csv("../datasets/stage4/test.csv")
X = df.iloc[:,[0,1,2]]
y = df.iloc[:,3]

def check1():
    with open("../models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
    score = clf.score(X, y)
    assert score > 0.75

