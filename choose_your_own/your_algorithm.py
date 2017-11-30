#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

print '-------------- K nearest neighbors --------------'

from sklearn.neighbors import KNeighborsClassifier
from time import time

n = 3
print 'create clf with n_neighbors = ', n
clf = KNeighborsClassifier(n_neighbors = n)

t = time()
clf.fit(features_train, labels_train)
print 'training time: ', round(time() - t, 3), 's'

t = time()
pred = clf.predict(features_test)
print 'predict time: ', round(time() - t, 3), 's'

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)

print 'accuracy: ', acc

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

print '-------------- Ada boost --------------'

from sklearn.ensemble import AdaBoostClassifier
from time import time

n = 75
print 'create clf with n_estimators = ', n
clf = AdaBoostClassifier(n_estimators = n)

t = time()
clf = clf.fit(features_train, labels_train)
print 'training time: ', round(time() - t, 3), 's'

t = time()
pred = clf.predict(features_test)
print 'predict time: ', round(time() - t, 3), 's'

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)

print 'accuracy: ', acc

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

print '-------------- Random forest --------------'

from sklearn.ensemble import RandomForestClassifier
from time import time

n = 2
print 'create clf with min_samples_split = ', n
clf = RandomForestClassifier(min_samples_split = 2)

t = time()
clf.fit(features_train, labels_train)
print 'training time: ', round(time() - t, 3), 's'

t = time()
pred = clf.predict(features_test)
print 'predict time: ', round(time() - t, 3), 's'

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)

print 'accuracy: ', acc

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass






