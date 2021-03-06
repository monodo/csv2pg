﻿# Incremental loading into PostGres DataBase of meteo data
# SITN 2013
import os, sys, shutil, csv, psycopg2, uuid
from datetime import datetime as dt
from matching_dictionnary import Combilog
from matching_dictionnary import SwissMetNet
from application_params import *

def importCombilog(fileList):    

    conn = psycopg2.connect(host=connParams['host'], database=connParams['database'], user=connParams['user'], password=connParams['password'])
    cur = conn.cursor()

    # START Combilog Data
    nbFile = len(fileList)
    k = 0
    maxImport = 145 # ugly data => ugly cleaning
    for item in fileList:
        filename = item[0]
        isFileModified = item[1]
        if isFileModified:
            sql = "delete from stations_air.meteo_log where sourcefile_name = '" + filename + "';" 
            cur.execute(sql)
   
        station_id =filename[0:3]
        k+=1
        print 'loading file : ' + filename
        filePath = targetDir + 'Combilog/' + filename
        f = open(filePath)
        csv.register_dialect('Combilog', delimiter=';', skipinitialspace=1)
        reader = csv.reader(f, dialect='Combilog')
        # get headers
        headers = reader.next()
        targetFields = ''
        for header in headers:
            targetFields += Combilog[header] +','
        targetFields = 'idobj, station_id, '+ targetFields[0:-1]
        targetFields += ',sourcefile_name'
        # insert each row into table
        rowImportNumber = 0
        for row in reader:
            rowImportNumber+=1
            if rowImportNumber <= maxImport:
                idobj = str(uuid.uuid4())
                 # replace dummy/empty values
                for i in range(0,len(row)):
                    if row[i].strip()=='-':
                        row[i]='-9999'
                sql = "insert into stations_air.meteo_log ("
                sql += targetFields + ") VALUES ('"+ idobj + "','" + station_id +  "'," + str(row)[1 : -1]                     
                sql += ",'" + filename + "');"
                cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print 'loading of Combilog data successfull, ' + str(k) + ' files loaded into the database'
    f = open('log.txt', 'a')
    f.write('\nloading of Combilog data successfull, ' + str(k) + ' files loaded into the database')
    f.close()
