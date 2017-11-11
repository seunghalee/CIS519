"""

Adam Engelson

"""
print(__doc__)

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import cross_val_score

# load the train data set
filename = 'train.csv'
data = np.array(np.loadtxt(filename, delimiter=','))

N,D = data.shape
# shuffle the data
idx = np.arange(N)
np.random.seed(13)
np.random.shuffle(idx)
data = data[idx]

#train on 70% of the data
Xtrain = data[:N*7/10, :-1]
ytrain = data[:N*7/10, -1]
Xtest = data[N*7/10:,:-1]
ytest = data[N*7/10:,-1]

model = svm.SVC(C = 1000, kernel='rbf', gamma=0.005)
model.fit(Xtrain, ytrain)

#classify
ypred = model.predict(Xtest)
#score = np.mean(cross_val_score(model, Xtest, ytest, cv = 5))
score = accuracy_score(ytest, model.predict(Xtest))

for i in range(len(ytest)):
    print(ytest[i], ypred[i])

print(score)