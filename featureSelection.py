"""
Script for creating feature matrix from imported accelerometer data
"""
import numpy as np

#-----------------------------------------------------------------
#  Class FeatureExtraction
#-----------------------------------------------------------------

class featureExtraction:

    def __init__(self):
        '''
        Constructor
        '''

    def mean(self,X):
        return np.mean(X, axis=1)

    def std(self, X):
        return np.std(X, axis=0)

    def length(self, X, fs):
        return len(X) * 1/fs

    def max(self,X):
        return np.ndarray.max(axis=0)

    def min(self,X):
        return np.ndarray.min(axis=0)


