#!/usr/bin/python
import unsupervised_classification as uc
import subprocess

projectDirectory = '/home/ryan/geoworkspace/git/gis-files/'
tifFilePath = projectDirectory + 'test/data/015029_0100_991101_l7_743_lcc00'
print projectDirectory + 'src/convertGeoTifToLan.sh'
print tifFilePath
subprocess.call([projectDirectory + 'src/convertGeoTifToLan.sh', tifFilePath])
#lanFileName = tifFilePath + ".lan"
#lanFilePath = projectDirectory + "test/data/" + lanFileName
#myUnclass = uc.unclass(5, 10)
#myUnclass.perform_clustering(lanFilePath)