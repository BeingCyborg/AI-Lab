import numpy as np
import matplotlib.pyplot as plt

# Load data
X = np.loadtxt("jain_feats.txt")
centroid_old = np.loadtxt("jain_centers.txt")
centroid_new = np.zeros_like(centroid_old)


# K-Means algorithm
for e in range(1000):

    # Assign points to centroids
    label = np.zeros(X.shape[0], dtype=int)
    for i in range(X.shape[0]):
        dist = np.zeros(centroid_old.shape[0])
        for j in range(centroid_old.shape[0]):
            dist[j] = np.linalg.norm(X[i, :] - centroid_old[j, :])
        label[i] = np.argmin(dist)

    # Update centroids
    for j in range(centroid_new.shape[0]):
        centroid_new[j, :] = np.mean(X[label == j, :], axis=0)

    # Stop condition check
    diff = np.max(np.abs(centroid_new - centroid_old))
    if diff < 1E-7:
        break

    # Move to next iteration
    centroid_old = centroid_new.copy()

# Plot final centroids and data
plt.scatter(X[:, 0], X[:, 1], c=label)
plt.scatter(centroid_old[:, 0], centroid_old[:, 1], c='red', marker='*', s=200)
plt.show()
