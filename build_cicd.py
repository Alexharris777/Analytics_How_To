import pandas as pd
import os
import teradata
import datetime
import io
import requests
import time

udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc",system=prod, username=username,
password=password, driver="Teradata Database ODBC Driver 16.20", dbs_port="1025")

# Append Git Branch Name to table (if not master branch)
git_branch = open("current_branch.txt", "r", encoding="utf-8")
git_branch = git_branch.read()
git_branch = git_branch.strip()

if git_branch == 'master':
    git_branch = ''
else:
    git_branch = str('_' + git_branch)
print(git_branch)

print('Building Table')
session.execute(file='xyz/xyz.sql', delimiter=';', continueOnError = True)
build_cases = str('CREATE TABLE db.table' + git_branch + ' ' + 'AS final_cases_temp  WITH DATA primary index (x,y,z);')
session.execute(build_cases, delimiter=';', continueOnError = True)
