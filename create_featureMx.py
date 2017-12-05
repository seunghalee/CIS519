"""
Script for importing all data from a given folder name and generating a feature matrix

Author: Seungha Lee
"""

import os
import glob
import pandas as pd
import numpy as np
from statsmodels import robust

def getpath(folder_name):

    '''
    :param folder_name: This is the folder that contains all the files
    :return: a list that contains all the csv file path
    '''

    if folder_name == "":
        return []

    if folder_name[-1] != '/':
        folder_name = folder_name + '/'

    sub_folder = os.listdir(folder_name)

    # remove hidden files
    for item in sub_folder:
        if item.startswith('.'):
            sub_folder.remove(item)

    num_trials = np.size(sub_folder)
    file_path = []

    for i in np.arange(num_trials):
        file_path.extend(sorted(glob.glob(os.path.join(folder_name + sub_folder[i], "*.csv"))))

    return file_path


if __name__ == "__main__":
    file_name = "Clean_data"

    all_trials = getpath(file_name)
    labels = []
    featuresMx = []

    for f in all_trials:
        # f = "Clean_data/Trial0/0_0.csv"
        df = pd.read_csv(f, sep=',', header=None)
        rep = [tuple(x) for x in df.values]

        # labels
        if f[19] != '_':
            label = int(f[18:20])
        else:
            label = int(f[18])
        labels.append(label)
        
        
        # ===================== features ===========================
        mean = np.mean(rep, axis=0)
        std = np.std(rep, axis=0)
        max_val = np.amax(rep, axis=0)
        min_val = np.amin(rep, axis=0)
        power = np.sum(np.power(rep,2), axis=0)/np.sum(np.power(rep,2))
        median = np.median(rep,axis=0)
        MAD = robust.mad(rep,axis = 0)
        # ==========================================================

        #features = np.array([median, std, max_val, min_val, power]).ravel()
        features = np.array([median, std, max_val, min_val, power]).ravel()
        featuresMx.append(features)

    featuresMx = np.asarray(featuresMx)
    labels = np.asarray(labels)

    # normalize features
    norm_featuresMx = (featuresMx - np.mean(featuresMx, axis=0)) / np.std(featuresMx, axis=0)

    np.savetxt("training.csv", np.c_[featuresMx, labels], delimiter=",")
    np.savetxt("training_normalized.csv", np.c_[norm_featuresMx, labels], delimiter=",")
