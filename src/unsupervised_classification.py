from spectral import *

class unclass:
    def perform_clustering(self, file, numClusters, numIterations):
        img = open_image(file).load()
        (m, c) = kmeans(img, numClusters, numIterations)
        