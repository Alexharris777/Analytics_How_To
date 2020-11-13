import pandas as pd
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import tree
from sklearn.svm import SVC
from sklearn.metrics import r2_score
import random
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek

os.chdir(r'')
cursor = cnxn.cursor()
query = open(r'')
resoverall = query.read()
dataset = pd.read_sql_query(resoverall, cnxn)
dataset = dataset.fillna(0)
dataset = pd.get_dummies(dataset)
print('Training Data Transformed')

array = dataset.values
X = array[:,1:]
Y = array[:,0]

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=.2, shuffle=True)
smote = SMOTE(ratio='minority')
x_train, y_train = smote.fit_sample(x_train, y_train)
print('Training Data Smoted')

print('Begin Modeling')
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print('Accuracy',accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
