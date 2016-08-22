from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    print "dataSetSize:",dataSetSize
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    print "diffMat:",diffMat
    sqDiffMat = diffMat**2
    print "sqDiffMat:",sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)	
    print "sqDistances:",sqDistances
    distance = sqDistances**0.5
    print "distance:",distance
    sortedDistIndicies = distance.argsort()
    print "sortedDistIndicies:",sortedDistIndicies
    classCount = {}
    for i in range(k):
    	votelabel = labels[sortedDistIndicies[i]]
    	classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    print "sortedClassCount:",sortedClassCount
    return sortedClassCount[0][0]	

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    print 'returnMat:',returnMat
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector    