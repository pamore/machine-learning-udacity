#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)#,min_samples_split=50)
print "created Decision tree"
print '# of features=',len(features_train[0])
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
from sklearn.metrics import accuracy_score
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"
print 'accuracy =',round(accuracy_score(pred, labels_test),5);
# With Entropy - accuracy = 0.993174061433
# With Gini -    accuracy = 0.990329920364
#########################################################
#OUTPUT with 1% features
# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# created Decision tree
# # of features= 379
# training time: 4.868 s
# predicting time: 0.0 s
# accuracy = 0.96701
#########################################################


