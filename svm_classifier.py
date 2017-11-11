# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 17:41:42 2017

@author: Adam
"""

import numpy as np

sigma = 1   #RBF falloff
theta = []  #Model

def myGaussianKernel(X1, X2):
    '''
    Arguments:
        X1 - an n1-by-d numpy array of instances
        X2 - an n2-by-d numpy array of instances
    Returns:
        An n1-by-n2 numpy array representing the Kernel (Gram) matrix
    '''
    n1,d = X1.shape
    n2,d = X2.shape
    K = np.zeros((n1,n2))
    for i in range(n1):
        for j in range(n2):
            K[i,j] = np.exp(-np.sum(np.power((X1[i,:] - X2[j,:]), 2))/(2*sigma**2))
    return K


def fit(self, X, y):
    '''
    Arguments:
        X - n-by-d numpy array for training 
    Returns:
        d-by-1 numpy array of representing model, theta
    '''
    J = np.sum(a) - 1/2*
    return self.theta
    
    
def predict(self, X):
    # J(theta) for classification
    np.argmax(self.theta.T.dot(X) + b)
    return y