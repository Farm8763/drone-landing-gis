import unsupervised_classification as uc
import subprocess

tifFilePath = ""
subprocess.call(['test.sh', tifFilePath])
fileName = tifFilePath + ".lan"
filePath = "test/data/" + fileName
myUnclass = uc.unclass(5, 10)
myUnclass.perform_clustering(filePath)