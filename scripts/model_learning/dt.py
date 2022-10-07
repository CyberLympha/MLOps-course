import sys
import os
import io
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]

df = pd.read_csv(f_input)

X = df.iloc[:,[1,2,3]]
y = df.iloc[:,0]

model = DecisionTreeClassifier()
model.fit(X, y)
