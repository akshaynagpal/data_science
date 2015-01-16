from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX, dataSet, labels, k):
	# inX - input vector to classify
	# dataSet - training examples
	# labels - vector of lables
	# k - no.of nearest neghbours to use 
	dataSetSize = dataSet.shape[0] #shape[0] gives no. of rows
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	#numpy.tile(A, reps)
	#Construct an array by repeating A the number of times given by reps.
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	print distances
	sortedDistIndices = distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	print classCount
	print sortedClassCount
	return sortedClassCount[0][0]


"""
argsort() : returns sorted indices of an array
>>> x=array([3,1,2])
>>> x.argsort()
array([1, 2, 0], dtype=int64)
"""
def file2matrix(filename):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	fr = open(filename)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat,classLabelVector


"""
>>> import kNN
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111)
>>> datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
>>> ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
<matplotlib.collections.PathCollection object at 0x0000000008788278>
>>> plt.show()
"""


def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect