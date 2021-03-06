# -*- coding: utf-8 -*-
"""
Script for comparing different classifiers

Author: Seungha Lee
"""
import numpy as np
#from hmmlearn import hmm
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_recall_fscore_support

if __name__ == "__main__":

    # load the training data
    filename = 'training_normalized.csv'
    allData = np.array(np.loadtxt(filename, delimiter=','))

    X = np.matrix(allData[:, :-1])
    y = allData[:, -1]

    # standardize the data
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X = (X - mean) / std

    n, d = X.shape

    # generate indices for shuffling the training data
    idx = np.arange(n)
    np.random.seed(13)

    # run pca or lasso for feature reduction if needed

    # train the model - svc, rf

    # ================== COMPUTE EXPECTED ACCURACY =============================
    # 10 trials of 10-fold cross validation
    k = 10  # k-fold CV
    num_trials = 10
    sample_size = int(k * num_trials)  # number of total models

    c_svc = 200  # regularization term for SVC
    c_logreg = 1000  # regularization term for logistic regression
    gamma_svc = 0.0065
    tolerance = 1e-06
    
    accuracy_list_SVC = []
    accuracy_list_NBgaussian = []
    accuracy_list_logreg = []

    precision_svc = np.zeros((k,4))
    precision_nb  = np.zeros((k,4))
    precision_logreg = np.zeros((k,4))
    recall_svc = np.zeros((k,4))
    recall_nb  = np.zeros((k,4))
    recall_logreg = np.zeros((k,4))
    
    precision_recall_svc =[]
    precision_recall_nb  = []
    precision_recall_logreg = []
     
    trial = 1
    while trial <= num_trials:
        # shuffle full data set at the start of each trial
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # train classifiers
        clf_svc = SVC(C=c_svc, kernel='rbf', gamma=gamma_svc,tol = tolerance)
        clf_NBgaussian = GaussianNB()
        clf_logreg = LogisticRegression(C=c_logreg)  # c value was found using GridSearchCV

        # compute training accuracy of each model
        accuracy_SVC = cross_val_score(clf_svc, X, y, cv=k, scoring='accuracy')
        accuracy_gaussian = cross_val_score(clf_NBgaussian, X, y, cv=k, scoring='accuracy')
        accuracy_logreg = cross_val_score(clf_logreg, X, y, cv=k, scoring='accuracy')

        # create list of accuracies of all trials
        accuracy_list_SVC.append(accuracy_SVC)
        accuracy_list_NBgaussian.append(accuracy_gaussian)
        accuracy_list_logreg.append(accuracy_logreg)
        
        #
        prediction_SVC = cross_val_predict(clf_svc, X,y, cv = k)
        prediction_NB  = cross_val_predict(clf_NBgaussian , X,y, cv=k)
        prediction_logreg = cross_val_predict(clf_logreg,X,y,cv=k)
        
        #
        precision_recall_svc.append(precision_recall_fscore_support(y,prediction_SVC))
        precision_recall_nb.append( precision_recall_fscore_support(y,prediction_NB))
        precision_recall_logreg.append(precision_recall_fscore_support(y,prediction_logreg))
         
        
        trial += 1

    # compute mean accuracy
    mean_acc_SVC = np.mean(accuracy_list_SVC)
    mean_acc_gaussian = np.mean(accuracy_list_NBgaussian)
    mean_acc_logreg = np.mean(accuracy_list_logreg)

    # compute standard error of accuracies
    SE_SVC = np.std(accuracy_list_SVC) / np.sqrt(sample_size)
    SE_gaussian = np.std(accuracy_list_NBgaussian) / np.sqrt(sample_size)
    SE_logreg = np.std(accuracy_list_logreg) / np.sqrt(sample_size)

    for i in np.arange(10):
        precision_svc[i,:] = precision_recall_svc[i][0]
        recall_svc[i,:] = precision_recall_svc[i][1]
        precision_nb[i,:] = precision_recall_nb[i][0]
        recall_nb[i,:] = precision_recall_nb[i][1]
        precision_logreg[i,:] = precision_recall_logreg[i][0]
        recall_logreg[i,:] = precision_recall_logreg[i][1]
        
    print np.mean(precision_logreg,axis = 0)
    print np.mean(precision_nb,axis = 0)
    print np.mean(precision_svc,axis = 0)
    print np.mean(recall_logreg,axis = 0)
    print np.mean(recall_svc,axis = 0)
    print np.mean(recall_nb,axis = 0)
    
    # print accuracy mean and standard error
    print "SVC Accuracy = " + str(mean_acc_SVC)
    print "SVC Standard Error = " + str(SE_SVC)
    print " "
    print "NB Gaussian Accuracy = " + str(mean_acc_gaussian)
    print "NB Gaussian Standard Error = " + str(SE_gaussian)
    print " "
    print "Logreg Accuracy = " + str(mean_acc_logreg)
    print "Logreg Standard Error =" + str(SE_logreg)

# 10 trials of 10-fold CV
# NB Gaussian Accuracy = 0.8025
# NB Gaussian Standard Error = 0.0115863305475
