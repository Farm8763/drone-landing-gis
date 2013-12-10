#!/usr/bin/python

import sys, os, numpy, argparse
import grass.script as g
import grass.script.setup as gsetup

'''
http://code.google.com/p/postgis-grass-r-py/wiki/0003_01_PythonForGrassGis

Wrapper of "python.setup.init" defined in GRASS python.
Initialize system variables to run scripts without starting GRASS explicitly.
                
@param dbBase: path to GRASS database (default: '').
@param location: location name (default: '').
@param mapset: mapset within given location (default: 'PERMANENT')

@return: Path to gisrc file.
'''
class grassConnector():
        def __init__(self, dbBase="", location="", mapset="PERMANENT"):
            self.gisbase = os.environ['GISBASE']
            self.gisdb = dbBase
            self.loc = location
            self.mapset = mapset
            gsetup.init(self.gisbase, self.gisdb, self.loc, self.mapset)
        
        def getDbInfo(self):
            dbinfo = g.parse_command('db.connect',flags="p")
            dbstat = {}
            for i in range(len(dbinfo)):
                info = dict.keys(dbinfo)[i].split(":")[0]
                if info == "driver":
                    e_key = dict.keys(dbinfo)[i].split(":")[0]
                    e_val = dict.keys(dbinfo)[i].split(":")[1]
                    driver=None
                    if e_val == "pg":
                        driver="postgres"
                    dbstat[e_key] = driver
            for i in range(len(dbinfo)):
                if not dict.values(dbinfo)[i] == None:
                    elems = dict.values(dbinfo)[i].split(",")
                    for elem in elems:
                        if len(elem.split('=')) > 1:
                            e_key = elem.split('=')[0]
                            e_val = elem.split('=')[1]
                            dbstat[e_key] = e_val
            return(dbstat)
        
        def getFeatName(self, FeatNam, colname):
            nams = g.parse_command('v.db.select',map=FeatNam,columns=colname,quiet=True)
        
        def getColums(self, FeatNam):
            desc = g.parse_command('db.describe', flags='c', table=FeatNam)
            return(dict.keys(desc))
        
        def getVectorMap():
            # Parse the command and get results from the GRASS module.
            parse = dict.keys(g.parse_command("g.list", _type="vect"))[3].split(" ")
            # Create a null object to store names of vector maps.
            result = []
            # Add a name of vector map when the value is not empty.
            for i in range(len(parse)):
                if not parse[i] == "":
                    result.append(parse[i])
            # Finally return the results.
            return result
        