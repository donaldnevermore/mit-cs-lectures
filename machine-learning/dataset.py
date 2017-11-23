from sklearn import datasets
from sklearn import svm


def divider():
    '''prints a line that divides multiple results
    so that you can see them clearer
    '''
    print('-' * 79)


iris = datasets.load_iris()
digits = datasets.load_digits()

# uncomment it to see results
# print(digits.data)
# divider()
# print(digits.target)
# divider()
# print(digits.images[0])


clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])
