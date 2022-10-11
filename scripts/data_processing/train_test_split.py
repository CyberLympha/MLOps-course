import yaml
import sys
import os

import pandas as pd
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))["split"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 train_test_split.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output_train = os.path.join("datasets", "stage4", "train.csv")
os.makedirs(os.path.join("datasets", "stage4"), exist_ok=True)
f_output_test = os.path.join("datasets", "stage4", "test.csv")
os.makedirs(os.path.join("datasets", "stage4"), exist_ok=True)

p_split_ratio = params["split_ratio"]

df = pd.read_csv(f_input)
X = df.iloc[:,[1,2,3]]
y = df.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=p_split_ratio, stratify=y)

pd.concat([X_train, y_train], axis=1).to_csv(f_output_train, header=None, index=None)
pd.concat([X_test, y_test], axis=1).to_csv(f_output_test, header=None, index=None)
