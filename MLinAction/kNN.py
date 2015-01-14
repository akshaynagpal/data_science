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
	sortedDistIndices = distances.argsort()
	classCount={}

	for i in range(k):
		voteIlabel = labels[sortedDistIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

