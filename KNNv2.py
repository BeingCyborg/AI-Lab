import numpy as np

# load the data from iris.csv file
data = np.genfromtxt('iris.csv', delimiter=',', skip_header=1)

# extract features and labels
X = data[:, :4]  # extract the first four columns as features
# extract the fifth column as labels and convert 1 to True, 0 to False
y = (data[:, 4] == 1).astype(int)

# randomize X and y
idx = np.random.permutation(X.shape[0])
X = X[idx]
y = y[idx]

# split X and y into training and test sets
train_size = int(0.8 * X.shape[0])
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]

# k-NN algorithm for test prediction
k = 5
y_test_predicted = np.zeros(X_test.shape[0])
for i in range(len(X_test)):
    x_test = X_test[i]
    # calculate Euclidean distances between x_test and X_train
    D = np.sqrt(np.sum((X_train - x_test)**2, axis=1))
    # find indices of k nearest neighbors with the smallest distances
    min_dist_indices = np.argsort(D)[:k]
    y_neighbor = y_train[min_dist_indices]
    # predict the label that occurs most frequently in y_neighbor
    y_test_predicted[i] = np.bincount(y_neighbor).argmax()

# print the predicted labels and actual labels for the test set
y_test_predicted = y_test_predicted.astype(int)
print('Predicted labels:', y_test_predicted)
print('Actual labels:', y_test)

# calculate the accuracy of the prediction
accuracy = np.sum(y_test_predicted == y_test) / y_test.shape[0]
print(f'Accuracy: {accuracy*100}%')
