import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("datasets", "stage3", "train.csv")
os.makedirs(os.path.join("datasets", "stage3"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_survived = []
    arr_pclass = []
    arr_sex = []
    arr_age = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_survived.append(line[0])
        arr_pclass.append(line[1])
        arr_sex.append(line[2])
        arr_age.append(line[3])

    for i in range(len(arr_sex)):
        if arr_sex[i] == 'male':
            arr_sex[i] = 1
        else:
            arr_sex[i] = 0

    for p_survived, p_pclass, p_sex, p_age in zip(arr_survived, arr_pclass, arr_sex, arr_age):
        fd_out.write("{},{},{},{}\n".format(p_survived, p_pclass, p_sex, p_age))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)

        