from numpy import *


def loadDataSet():
  postingList = [['my', 'dog', 'has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']
                 ]
  classVec = [0,1,0,1,0,1]
  return postingList,classVec

def createVocabList(dataSet):
  vocabSet = set([])
  for doc in dataSet:
    vocabSet = vocabSet | set(doc)
  return list(vocabSet)

def setOfWord2Vec(vocabList,inputSet):
  returnVec = [0]*len(vocabList)
  for word in inputSet:
    if word in vocabList:
      returnVec[vocabList.index(word)] = 1
    else:print "the word :%s is not in my Vocabulary" % word
  return  returnVec

def trainNB0(trainMatrix,trainCategory):
  numTrainDocs = len(trainMatrix)
  numWords = len(trainMatrix[0])
  pAbusive = sum(trainCategory)/float(numTrainDocs)
  p0Num = ones(numWords);p1Num = ones(numWords)
  p0Denom = 2.0;p1Denom = 2.0
  for i in range(numTrainDocs):
    if trainCategory[i] == 1:
      p1Num += trainMatrix[i]
      p1Denom += sum(trainMatrix[i])
    else:
      p0Num += trainMatrix[i]
      p0Denom += sum(trainMatrix[i])
  p0Vet = log(p0Num/p0Denom)
  p1Vet = log(p1Num/p1Denom)

  return p0Vet,p1Vet,pAbusive

def  classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
  p1 = sum(vec2Classify*p1Vec) + log(pClass1)
  p0 = sum(vec2Classify*p0Vec) + log(1.0 - pClass1)
  if p1 > p0:
    return 1
  else:
    return 0




listOfPosts,listOfClasses = loadDataSet()
print listOfPosts
print listOfClasses
vocSet = createVocabList(listOfPosts)
print vocSet
print setOfWord2Vec(vocSet,listOfPosts[0])
print setOfWord2Vec(vocSet,listOfPosts[1])
trainMat = []
for postDoc in listOfPosts:
  trainMat.append(setOfWord2Vec(vocSet,postDoc))
p0V,p1V,pAb = trainNB0(trainMat,listOfClasses)
print p0V
print p1V
print pAb
testEntry = ['stupid','garbage','dalmation']
thisDoc = array(setOfWord2Vec(vocSet,testEntry))
print testEntry,'classifyas :',classifyNB(thisDoc,p0V,p1V,pAb)
