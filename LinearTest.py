
# coding: utf-8

# In[1]:


import pandas
import numpy


# In[2]:


data = pandas.read_csv('F:\Anaconda\iris.csv')


# In[3]:


X = numpy.array(data[['x1', 'x2']])
y = numpy.array(data['y'])

#check check labeled data 
print(X)

#check label
print(y)

# Fit data by using Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X,y)

# Fit data by using Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X,y)


# In[8]:

Fit data by using suport vector machine
from sklearn.svm import SVC
classifier=SVC(kernel='rbf',degree=300)
classifier.fit(X,y)


# In[9]:


#Fit data by using Gradient Boosting Classifier
from sklearn.ensemble import GradientBoostingClassifier
classifier=GradientBoostingClassifier()
classifier.fit(X,y)

