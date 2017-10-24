"""
Script for creating feature matrix from imported accelerometer data
"""
import numpy as np

#-----------------------------------------------------------------
#  Class FeatureExtraction
#-----------------------------------------------------------------

class featureExtraction:

    def __init__(self, X ,Y):
        '''
        Constructor
        '''

        self.X = X  # raw accelerometer data
        self.Y = Y  # gesture label


    def mean(self,X):
        return np.mean(X, axis=1)

    def std(self, X):
        return np.std(X, axis=0)

    def length(self, X, fs):
        return len(X) * 1/fs



if __name__ == "__main__":

    # load the data
    filePath = "data/raw_accelerometer.dat"
    file = open(filePath, 'r')
    allData = np.loadtxt(file, delimiter=',')

