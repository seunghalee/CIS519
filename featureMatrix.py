"""
    Script for creating feature matrix
"""

import numpy as np

if __name__ == "__main__":

    # load the data
    filePath = "data/raw_accelerometer.dat" #TODO change filename
    file = open(filePath, 'r')
    allData = np.loadtxt(file, delimiter=',')

    X = allData
    #TODO include code for labels

    featMX = []

    # Extract selected features
    features = featureExtraction
    mean = features.mean
    std = features.std
    length = features.length

    # concatenate all features into one feature matrix
    featMX = np.c_[featMX, mean, std, length]
