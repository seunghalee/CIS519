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
for t in range(num_trials):
    for g in range(num_gestures):
        for r in range(num_reps):
            filename = 'Raw_Data/Trial' + str(t) + '/' + str(g) + '_' + str(r) + '.csv'
            raw = np.array(np.loadtxt(filename, delimiter=','))[1:,:]
            N,D = raw.shape
            data = np.array(raw)
            mean = np.mean(data, axis=0)
            power_data = np.power(data - mean,2)
            std = np.std(power_data, axis=0)
            k = 4
            for n in range(N):
                if (power_data[n,0] > k*std[0]):
                    if n==0:
                        data[n,0] = data[n+1,0]
                    elif n == N-1:
                        data[n,0] = data[n-1,0]
                    else:
                        data[n,0] = (data[n-1,0] + data[n+1,0])/2
                if (power_data[n,1] > k*std[1]):
                    if n==0:
                        data[n,1] = data[n+1,1]
                    elif n == N-1:
                        data[n,1] = data[n-1,1]
                    else:
                        data[n,1] = (data[n-1,1] + data[n+1,1])/2
                if (power_data[n,2] > k*std[2]):
                    if n==0:
                        data[n,2] = data[n+1,2]
                    elif n == N-1:
                        data[n,2] = data[n-1,2]
                    else:
                        data[n,2] = (data[n-1,2] + data[n+1,2])/2
            window_size = N/10
            for n in range(N-window_size):
                window = data[n:n+window_size, :]
                mean_window = np.mean(window, axis=0)
                std_window = np.std(window, axis=0)
                k = 2
                spike = 0
                for s in range(window_size):
                    if (abs(window[s,0] - mean_window[0]) > k*std_window[0] or abs(window[s,1] - mean_window[1]) > k*std_window[1] or abs(window[s,2] - mean_window[2]) > k*std_window[2]):
                        spike = n + s
                        break
                if spike > 0:
                    break
            trimmed_data = data[spike:,:] - np.mean(data[spike:,:],axis=0)
            #np.savetxt('Clean_Data/Trial' + str(t) + '/' + str(g)+"_"+str(r)+".csv", trimmed_data, delimiter=",")  #save rep into file
            print(str(data.shape[0]) + ' -> ' + str(trimmed_data.shape[0]))
            f, (ax1,ax2,ax3) = plt.subplots(1,3, sharey=True)
            ax1.set_title('Raw')
            ax1.plot(raw[:,0])
            ax1.plot(raw[:,1])
            ax1.plot(raw[:,2])
            ax2.set_title('S&P Noise Removal')
            ax2.plot(data[:,0])
            ax2.plot(data[:,1])
            ax2.plot(data[:,2])
            ax3.set_title('Spike Detection')
            ax3.plot(trimmed_data[:,0])
            ax3.plot(trimmed_data[:,1])
            ax3.plot(trimmed_data[:,2])
            plt.pause(1)
            plt.close()