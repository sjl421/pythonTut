from numpy import *

def loadSimpData():
    dataMat = matrix([[1.,2.1],
                      [2., 1.1],
                      [1.3, 1.],
                      [1., 1.],
                      [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataMat, classLabels

def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0],1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] =  -1.0
    return retArray

def buildStump(dataArr, classLabels , D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0;bestStump = {}; bestClassEst = mat(zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max();
        stepSize = (rangeMax - rangeMin)/ numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predicatedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m,1)))
                errArr[predicatedVals == labelMat] = 0
                weightedError = D.T*errArr
                if weightedError < minError:
                    minError = weightedError
                    bestClassEst = predicatedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst


dataMat, classLabels = loadSimpData()
D = mat(ones((5,1))/5)
bestStump , minError, bestClassEst = buildStump(dataMat, classLabels, D)
print bestStump
print minError
print bestClassEst
