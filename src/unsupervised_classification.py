from spectral import *
import pylab

class unclass:
    def __init__(self, numClusters, numIterations):
        self.numClusters = numClusters
        self.numIterations = numIterations
        
    def perform_clustering(self, filePath):
        img = open_image(filePath).load()
        (self.map, self.clusters) = kmeans(img, self.numClusters, self.numIterations)
        
    def displayMap(self):
        pylab.figure()
        pylab.hold(1)
        for i in range(self.clusters.shape[0]):
            pylab.plot(self.clusters[i])
        pylab.show()