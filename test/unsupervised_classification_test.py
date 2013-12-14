#!/usr/bin/python
# ipython --pylab

import unsupervised_classification as uc
import convertGeoTifToLan as convert

projectDirectory = '/home/ryan/geoworkspace/git/gis-files/'
tifFilePathNoFileType = projectDirectory + 'test/data/016028_0100_010825_l7_743_lcc00'
lanFilePath = convert.convertGeoTifToLan(tifFilePathNoFileType)
print "convertGeoTifToLan.sh file path: " + projectDirectory + 'src/convertGeoTifToLan.sh'
myUnclass = uc.unclass(5, 20)
print ".lan image file path: " + lanFilePath
#myUnclass.displayLan(lanFilePath)
myUnclass.perform_kmeans_clustering(lanFilePath)
#myUnclass.perform_single_pass_clustering(lanFilePath)
myUnclass.saveKmeans(tifFilePathNoFileType)
#myUnclass.saveSinglePassMap(tifFilePathNoFileType)
#myUnclass.displayMap()
#myUnclass.performNDVI(lanFilePath)