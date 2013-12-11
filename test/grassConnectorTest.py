#!/usr/bin/python

import sys
# Add the path for the "grasswrapper.py";
sys.path.append('/root/git/drone-landing-gis/src')

# And Import the wrapper as following.
from grassConnector import grassConnector as grassGis

grass = grassGis()
grass.printNum()
#grass.getVectorMap()
print grass.getDbInfo()
