# ipython --pylab
from spectral import kmeans, open_image, ndvi, view, view_indexed, cluster
import pylab
import matplotlib.pyplot as plt

class unclass:
    def __init__(self, numClusters, numIterations):
        self.numClusters = numClusters
        self.numIterations = numIterations
        
    def perform_kmeans_clustering(self, filePath):
        img = open_image(filePath).load()
        (self.kmeans_map, self.kmeans_clusters) = kmeans(img, self.numClusters, self.numIterations)
        
    def saveKmeans(self, filePathNoType):
        pylab.figure()
        pylab.hold(1)
        for i in range(self.kmeans_clusters.shape[0]):
            pylab.plot(self.kmeans_clusters[i])
        print "Saving kmeans graph"
        pylab.savefig(filePathNoType + "_kmeans_graph.png")
        print "Saving kmeans map"
        plt.imshow(self.kmeans_map) #Needs to be in row,col order
        plt.savefig(filePathNoType + "_kmeans_map.png")
        
    def saveSinglePassMap(self, filePathNoType):
        pylab.figure()
        pylab.hold(1)
        for i in range(self.single_pass_clusters.shape[0]):
            pylab.plot(self.single_pass_clusters[i])
        pylab.savefig(filePathNoType + "_singlepass.png")
                
    def performNDVI(self, filePath):
        ndviMap = ndvi(filePath, 21, 43)
        view(ndviMap)
    
    def displayMap(self):
        view_indexed(self.map)
    
    def displayLan(self, filePath):
        img = open_image(filePath)
        view(img)
        
    def perform_single_pass_clustering(self, filePath):
        img = open_image(filePath).load()
        (self.single_pass_map, self.single_pass_clusters) = cluster(img, self.numClusters)