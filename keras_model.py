import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
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
from sklearn.decomposition import PCA
import featuretools as ft
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.regularizers import l2
import tensorflow
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from keras.models import model_from_json
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
t2 = time.time()
print(t2-t1)

array = dataset.values
X = array[:,1:]
Y = array[:,0]

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=.2, shuffle=True)

smote = SMOTE(ratio='minority')
x_train, y_train = smote.fit_sample(x_train, y_train)

model = Sequential()
model.add(Dense(100, input_dim=x_train.shape[1], activation='relu', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
model.add(Dense(75, activation='tanh'))
model.add(Dropout(.2))
model.add(Dense(50, activation='softmax'))
model.add(Dropout(.2))
model.add(Dense(25, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(10, activation='tanh'))
model.add(Dense(5, activation='softmax'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=50, batch_size=10)

scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
accuracy = model.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], accuracy[1]*100))

predictions = model.predict(x_test)
predictions = np.round(predictions)
cm = confusion_matrix(y_test, predictions)
cr = classification_report(y_test, predictions)
print(cm,cr)
