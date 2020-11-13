import numpy as np
import pandas as pd
import teradata
from datetime import date

# Append Git Branch Name to table (if not master branch)
git_branch = open("current_branch.txt", "r", encoding="utf-8")
git_branch = git_branch.read()
git_branch = git_branch.strip()

if git_branch == 'master':
    git_branch = ''
else:
    git_branch = str('_' + git_branch)

print(git_branch)

# Row Count Test Query
query = str('select count(*) Row_Count from db.table'+git_branch)
row_count_test = pd.read_sql_query(query, session)

table_rows = row_count_test['Row_Count'].max()


# Duplicates Test Query
query = str(f'''select xyz , count(xyz) XYZ
            from db.table{git_branch} group by 1 having xyz >= 2 ''')
cases_dup_test = pd.read_sql_query(query, session)

cases_dups = cases_dup_test['xyz'].sum()

print(cases_dups)

print('Build Test Results:')
print(' ')

# Table Populated Test
if table_rows > 0:
    True
    print('**************************')
    print('Table Populated Test: PASS')
    print('table is not empty')
    print(' ')

else:
    False
    print('Table Populated Test: FAIL')
    exit(1)
