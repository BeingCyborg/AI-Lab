from functools import cmp_to_key
from numpy import genfromtxt
import numpy as np
data = np.genfromtxt('iris.csv', delimiter=',',
                     usecols=(0, 1, 2, 3, 5), skip_header=1)

np.random.shuffle(data)

X = data[:, :4]
y = data[:, 4:5]

train_size = int(len(X)*.8)
test_size = int(len(X)*.2)

X_train = X[:train_size]
y_train = y[:train_size]
X_test = X[train_size:]
y_test = y[train_size:]

y_test_predicted = np.array([None]*test_size)
k = 5


def comp(w, r):
    return w[1]-r[1]


for i in range(len(X_test)):
    x_test = X_test[i]
    D = []
    for j in range(len(X_train)):
        dist = np.linalg.norm(x_test - X_train[j])
        D.append([j, dist])
    D = sorted(D, key=cmp_to_key(comp))
    D = D[:k]
    y_neighbor = []
    for min_id in D:
        y_neighbor.append(y_train[min_id[0]])
    count_1 = 0
    for yt in y_neighbor:
        if yt == 1:
            count_1 += 1
    count_0 = len(y_neighbor)-count_1
    if count_0 < count_1:
        y_test_predicted[i] = 1
    else:
        y_test_predicted[i] = 0

correct = 0
for i in range(len(y_test)):
    if y_test[i][0] == y_test_predicted[i]:
        correct += 1
print("Test Set : [", end="")
for x in y_test:
    print(int(x[0]), end=" ")
print(']')
print(f'Prediction : {y_test_predicted}')
accuaracy = (correct/len(y_test))*100
print(f'Accuracy : {accuaracy}%')
