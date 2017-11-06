"""
Script for concatenating multiple CSV files into a single CSV file
"""

import os
import glob
import csv
import pandas as pd
import numpy as np


def gestureMx(path,num_gesture,num_rep):
    all_files = glob.glob(os.path.join(path, "*.csv"))  # file path of all csv files

    gesture_matrix = []
    for g in xrange(num_gesture+1):
        single_gesture = []
        for f in all_files[(g * num_rep):(g * num_rep + num_rep)]:
            df = pd.read_csv(f, sep=',', header=None)
            rep = [tuple(x) for x in df.values]
            single_gesture.append(rep)

        gesture_matrix.append(single_gesture)


    return gesture_matrix


if __name__ == "__main__":
    matrix = gestureMx(path="Clean_data/Trial0", num_gesture=3, num_rep=10)
    # example: matrix[0][9] would be 0_9.csv
    print matrix[0][0][0]


