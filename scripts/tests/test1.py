import os
import sys
import pickle
import json

import pandas as pd


#df = pd.read_csv("./datasets/stage4")
#X = df.iloc[:,[1,2,3]]
#y = df.iloc[:,0]

def check1():
    with open("./models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
    score = clf.score()
    assert score > 0.8

