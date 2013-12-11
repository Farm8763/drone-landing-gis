from drone-landing-gis import unsupervised_classification as uc

fileName = ""
filePath = "test/data/" + fileName
myUnclass = uc.unclass(5, 10)
myUnclass.perform_clustering(filePath)