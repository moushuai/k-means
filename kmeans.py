import numpy as np
from data_generator import DataGenerator
import matplotlib.pyplot as plt


def kmeans(X, K, iter=100):

    centroids = [X[i] for i in range(K)]
    #centroids = [X[0], X[50], X[98]]
    print "init:", centroids
    for _ in range(iter):
        if _ > 0:
            # recompute the centriods
            for i in range(len(clusters)):
                min_sum_dist = float("inf")
                for c in clusters[i]:
                    dist = 0
                    for x in clusters[i]:
                        dist += np.linalg.norm(c-x)
                    if dist < min_sum_dist:
                        centroids[i] = c
                        min_sum_dist = dist

        clusters = [[] for i in range(K)]
        # compute the clusters
        for x in X:
            index = -1
            min_dist = float("inf")
            for i in range(len(centroids)):
                dist = np.linalg.norm(x-centroids[i])
                if dist < min_dist:
                    index = i
                    min_dist = dist
            clusters[index].append(x)
        print centroids
    return centroids, clusters





if __name__ == '__main__':
    generator = DataGenerator(1000, 2, 5, supervised=False)
    X = generator.generate_data()
    centroids, clusters = kmeans(X, 5, 10)
    # print clusters[0]
    # Draw data set
    fig = plt.figure(1)
    plt.subplot(211)
    plt.scatter(X[:,0],  X[:,1])
    plt.show()
    #print (X)
