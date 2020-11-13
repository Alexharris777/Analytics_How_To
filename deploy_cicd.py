import pandas as pd
import os
import teradata
import datetime
import io
import requests

# Append Git Branch Name to table (if not master branch)
git_branch = open("current_branch.txt", "r", encoding="utf-8")
git_branch = git_branch.read()
git_branch = git_branch.strip()

if git_branch == 'master':
    git_branch = ''
else:
    git_branch = str('_' + git_branch)

print('Deploy Table')
build_cases = str('CREATE TABLE db.table' + git_branch + ' ' +
                     'AS db.table' + git_branch + ' '
                     + 'WITH DATA primary index (x,y,z);')

session.execute(build_cases, delimiter=';', continueOnError=True)
