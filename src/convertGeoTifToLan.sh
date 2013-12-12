import unsupervised_classification as uc
import subprocess

#path without filetype
tifFilePath = ""
subprocess.call(['/drone-landing-gis/src/convertGeoTifToLan.sh', tifFilePath])
fileName = tifFilePath + ".lan"
filePath = "test/data/" + fileName
myUnclass = uc.unclass(5, 10)
myUnclass.perform_clustering(filePath)