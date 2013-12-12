import unsupervised_classification as uc
import subprocess

projectDirectory = "/root/git/drone-landing-gis/"
tifFilePath = projectDirectory + "test/data/015029_0100_991101_l7_743_lcc00.tif"
subprocess.call([projectDirectory + 'src/convertGeoTifToLan.sh', tifFilePath])
lanFileName = tifFilePath + ".lan"
lanFilePath = projectDirectory + "test/data/" + lanFileName
myUnclass = uc.unclass(5, 10)
myUnclass.perform_clustering(lanFilePath)