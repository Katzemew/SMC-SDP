# -*- coding: utf-8 -*-
"""SDP asnmt4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BI9wanh-xcQ640v6_f4c8oFTsfpz6FLX

**Getting Started**
"""

import pandas as pd

data = pd.read_csv("/content/exams.csv")

data

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

data['gender'] = le.fit_transform(data['gender'])
data['race/ethnicity'] = le.fit_transform(data['race/ethnicity'])
data['parental level of education'] = le.fit_transform(data['parental level of education'])
data['lunch'] = le.fit_transform(data['lunch'])
data['test preparation course'] = le.fit_transform(data['test preparation course'])

data.dtypes

from sklearn import preprocessing
le=preprocessing.LabelEncoder()

data['writing score'].mean()

data['writing score'].fillna(67.744744,inplace=True)

data['reading score'].mean()

data['reading score'].fillna(69.048289,inplace=True)

data.isna().sum()

"""**Decision Tree Classifier**

"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = data.drop(columns=['test preparation course'])
y = data['test preparation course']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=40)

classifier = DecisionTreeClassifier(max_depth=5, criterion='gini')

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

y_test

y_pred

y

from sklearn.metrics import confusion_matrix

cm= confusion_matrix(y_test, y_pred)

print("Confusion matrix :")
print(cm)

import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(cm ,annot=True, fmt="d" , cmap="Reds" ,xticklabels=data['test preparation course'].unique(), yticklabels=data['test preparation course'].unique())

plt.show()

feature_values = []
for feature_name in X.columns:
    value = input(f"Enter value for {feature_name}: ")
    feature_values.append(float(value))

predicted_target = classifier.predict([feature_values])

print("Predicted target variable: ",predicted_target[0])

from sklearn.svm import SVC

classifier_svm = SVC(kernel ='rbf')

classifier_svm.fit(X_train,y_train)

y_pred_svm= classifier_svm.predict(X_test)

accuracy_svm= accuracy_score(y_test, y_pred_svm)
print("SVM Classifier accuracy: ",accuracy_svm)

"""KNN classifier"""

from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

classifier = KNeighborsClassifier(n_neighbors=5)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

y_pred

y_test

