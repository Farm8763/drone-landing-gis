import subprocess
def convertGeoTifToLan(tifFilePathNoFileType):
    print ".tif image file path: " + tifFilePathNoFileType
    subprocess.call(['/home/ryan/geoworkspace/git/gis-files/src/convertGeoTifToLan.sh', tifFilePathNoFileType])
    lanFilePath = tifFilePathNoFileType + ".lan"
    return lanFilePath