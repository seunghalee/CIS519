# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:59:59 2017

@author: Adam
"""

import numpy as np
import matplotlib.pyplot as plt

f = plt.figure
num_trials = 3
num_gestures = 4
num_reps = 10
X = []
Y = []
for t in range(num_trials):
    for g in range(num_gestures):
        for r in range(num_reps):
            filename = 'Clean_Data/Trial' + str(t) + '/' + str(g) + '_' + str(r) + '.csv'
            raw = np.array(np.loadtxt(filename, delimiter=','))
            N, D = raw.shape
            x = raw[:,0]
            y = raw[:,1]
            z = raw[:,2]
            
            stddev_x = np.std(x)
            stddev_y = np.std(y)
            stddev_z = np.std(z)
            
            part_total = np.sum(np.power(x,2)) + np.sum(np.power(y,2)) + np.sum(np.power(z,2))
            part_x = np.sum(np.power(x,2))/part_total
            part_y = np.sum(np.power(y,2))/part_total
            part_z = np.sum(np.power(z,2))/part_total
            
            max_x = np.max(x)
            max_y = np.max(y)
            max_z = np.max(z)
            
            min_x = np.min(x)
            min_y = np.min(y)
            min_z = np.min(z)
            
            f = np.array([stddev_x, stddev_y, stddev_z, part_x, part_y, part_z, max_x, max_y, max_z, min_x, min_y, min_z])
            X.append(f)
            Y.append(g)
X = (X - np.mean(X, axis=0))/np.std(X, axis=0)
np.savetxt("train.csv", np.c_[X, Y], delimiter=",")