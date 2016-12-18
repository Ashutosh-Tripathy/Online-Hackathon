
def ReplaceCharAndInsert(tempList,sourceIndex,targetIndex):
    global combinationSet,numberOfCombination
    # tempList=list(inputList)
    tempList[sourceIndex]=tempList[targetIndex]
    tempString=''.join(tempList)
    if(tempString in combinationSet):
        return
    numberOfCombination+=1
    # print(tempString)
    combinationSet.add(tempString)
    
def SwapCharAndInsert(tempList,sourceIndex,targetIndex):
    global combinationSet,numberOfCombination
    # tempList=list(inputList)
    temp=tempList[sourceIndex]
    tempList[sourceIndex]=tempList[targetIndex]
    tempList[targetIndex]=temp
    tempString=''.join(tempList)
    if(tempString in combinationSet):
        return
    # print(tempString)
    numberOfCombination+=1
    combinationSet.add(tempString)

def InsertStringAsItIs(tempList,sourceIndex,targetIndex):
    global combinationSet,numberOfCombination
    # # tempList=list(inputList)
    # temp=tempList[sourceIndex]
    # tempList[sourceIndex]=tempList[targetIndex]
    # tempList[targetIndex]=temp
    tempString=''.join(tempList)
    if(tempString in combinationSet):
        return
    print(tempString)
    numberOfCombination+=1
    combinationSet.add(tempString)
 
def CheckAndInsertInList(inputList,sourceIndex,targetIndex):
    if(targetIndex<0 or targetIndex> len(inputList)-1):
        return
    if(inputList[sourceIndex]==inputList[targetIndex]):
        return
    ReplaceCharAndInsert(list(inputList),sourceIndex,targetIndex)      
    SwapCharAndInsert(list(inputList),sourceIndex,targetIndex)      

def GetNumberOfPossibleCombination(inputList):
    global numberOfCombinationList,numberOfCombination
    for i in range(len(inputList)):
        numberOfCombination=0
        CheckAndInsertInList(inputList,i,i-1)
        # InsertStringAsItIs(inputList,i,i)
        CheckAndInsertInList(inputList,i,i+1)   
        # print(numberOfCombination)    
        numberOfCombinationList.append(numberOfCombination)     


global combinationSet,numberOfCombination,numberOfCombinationList
numberOfTestCase=int(input())
for i in range(numberOfTestCase):
    result=1
    numberOfCombinationList=[]
    inputString=input()
    combinationSet=set()
    # combinationSet.add(inputString)
    inputList=list(inputString)
    GetNumberOfPossibleCombination(inputList)
    for j in range(len(numberOfCombinationList)):
            if(numberOfCombinationList[-j-1]!=0):
                numberOfCombinationList[-j-1]+=1
                break
    # print(numberOfCombinationList)
    for j in range(len(numberOfCombinationList)):
            if(numberOfCombinationList[j]==0):
                continue
            result=result*numberOfCombinationList[j]
    # result=result*numberOfCombinationList[0]  
    # lenCombinationSet=len(combinationSet)
    if(result>=1000000007):
        result=result % 1000000007
    print("Case #"+str(i+1)+": "+str(result))