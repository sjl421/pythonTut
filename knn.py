from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)	
    distance = sqDistances**0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
    	votelabel = labels[sortedDistIndicies[i]]
    	classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]	

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector    

#datingDataMat,datingLabelVector = file2matrix('datingTestSet2.txt')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabelVector),15.0*array(datingLabelVector))
# plt.show()

# def autoNorm(dataSet):
# 	minVals=dataSet.min(0)
# 	maxVals=dataSet.max(0)
# 	ranges=maxVals-minVals
# 	normDataSet=zeros(shape(dataSet))
#     m=dataSet.shape[0]
#     normDataSet=dataSet-tile(minVals,(m,1))
#     normDataSet=normDataSet/tile(ranges,(m,1))
#     return normDataSet,ranges,minVals
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

def datingClassTest():
	hoRatio=0.10
	datingDataMat,datingLabelVector=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestVecs=int(m*hoRatio)
	errorCount=0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabelVector[numTestVecs:m],3)
		print "the classifier came back with:%d,the real answer is :%d" %(classifierResult,datingLabelVector[i])
		if(classifierResult != datingLabelVector[i]):
			errorCount+=1.0
	print "the total error rate is :%f" % (errorCount/float(numTestVecs))		

def classifyPerson():
	resultList=['not at all','in small does','in large does']
	percentTats=float(raw_input("percent of time playing video games:"))
	ffMiles=float(raw_input("frequent files miles per year"))
	iceCream=float(raw_input("ice cream of year"))
	datingDataMat,datingLabelVector=file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr=array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabelVector,3)
	print "you will like this person:",resultList[classifierResult - 1]