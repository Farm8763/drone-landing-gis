#!/usr/bin/python
import unsupervised_classification as uc
import subprocess

projectDirectory = '/home/ryan/geoworkspace/git/gis-files/'
tifFilePathNoFileType = projectDirectory + 'test/data/015029_0100_991101_l7_743_lcc00'
print "convertGeoTifToLan.sh file path: " + projectDirectory + 'src/convertGeoTifToLan.sh'
print ".tif image file path: " + tifFilePathNoFileType
subprocess.call([projectDirectory + 'src/convertGeoTifToLan.sh', tifFilePathNoFileType])
lanFilePath = tifFilePathNoFileType + ".lan"
myUnclass = uc.unclass(5, 10)
print ".lan image file path: " + lanFilePath
myUnclass.perform_clustering(lanFilePath)
myUnclass.saveKmeansMap(tifFilePathNoFileType)
myUnclass.performNDVI(lanFilePath)