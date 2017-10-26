"""
    Script for creating feature matrix
"""

import numpy as np
import csv
import pandas as pd
from featureSelection import featureExtraction

if __name__ == "__main__":

    # load the data
    filePath = "data/Trial1/Trial1.csv"
    rawData = []
    with open(filePath) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            rawData.append(row)
    rawData = np.asarray(rawData)

    df = pd.read_csv(filePath, sep=',')
    mean = df.mean(axis=0)
    print mean

    # #TODO include code for labels
    #
    # featMX = []
    # print np.mean(rawData, axis=0)
    # # Extract selected features
    # features = featureExtraction
    # mean = features.mean
    # print mean
    # std = features.std
    # length = features.length
    #
    # # concatenate all features into one feature matrix
    # featMX = np.c_[featMX, mean, std, length
