import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
print(digits.data)
print(digits.target)

# digits.target is the actual label we've assigned to the digits data. 
# Now that we've got the data ready, we're ready to do the machine learning.
# First, we specify the classifier:
# If you want, you can just leave parameters blank and use the defaults, like this:
# clf = svm.SVC()
# clf = svm.SVC(gamma=0.001, C=100)
# clf = svm.SVC(gamma=0.01, C=100)
clf = svm.SVC(gamma=0.0001, C=100)

X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)
print(clf.predict(digits.data[-5]))
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
