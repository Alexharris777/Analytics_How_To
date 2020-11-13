import pandas as pd
import os
import teradata

#Teradata Log In
udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc",system=prod, username=username,
password=password, driver="Teradata Database ODBC Driver 16.20", dbs_port="1025")

#Teradata Log In with LDAP
udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc",system=prod, username=username,
password=password, driver="Teradata Database ODBC Driver 16.20", dbs_port="1025",authentication='LDAP')

#Batch Up Load to Teradata
batchsize = 5000
for num in range(0, len(dataset), batchsize):
    session.executemany("insert into db.table values (?,?,?,?,?,?,?,?)",
    dataset[num:num+batchsize], batch=True)
