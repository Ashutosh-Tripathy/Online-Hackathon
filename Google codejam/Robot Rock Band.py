with open('output2.txt') as f:
    content = f.readlines()
for item in content:
    if(": 12" in item):
        print(item, end="")


# for i in range(55):
#   print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#   print("Current number is: "+str(i))
#   for j in range(55):
#       for k in range(55):
#           for l in range(55):
#               xorElement=i^j^k^l
#               print (str("{0:b}".format(i)) +" "+str("{0:b}".format(j))+" "+ str("{0:b}".format(k))+" "+str("{0:b}".format(l))+" is: "+str(xorElement) +" : "+str("{0:b}".format(xorElement)))

# with open('input.txt') as f:
#     content = f.readlines()

# print(content.pop(0))  
#------------------------------------------------

# with open('input.txt') as f:
#     content = f.readlines()
# def CreateAllCombination(robotListForEachPosition):
#   global resultNeeded
#   count=0
#   breakLoop3=False
#   index=1
#   for item1 in robotListForEachPosition[0]:
#       for item2 in robotListForEachPosition[1]:
#           print(index)
#           xorItem12=item1^item2
#           for item3 in robotListForEachPosition[2]:
#               xorItem123=xorItem12^item3
#               for item4 in robotListForEachPosition[3]:
#                   xorItem1234=xorItem123^item4
#                   if(xorItem123==resultNeeded):
#                       count+=1
#                       break
#               index+=1
#   return count

# tempObj,tempObj={},{}
# resultNeeded=0
# numberOfTestCase=int(content.pop(0))
# for x in range(numberOfTestCase):
#   resultNeeded=int(list(content.pop(0).split(' '))[1])
#   robotListForEachPosition=[]
#   for y in range(4):
#       robotListForEachPosition.append([int(z) for z in content.pop(0).split(" ")])
#   print(CreateAllCombination(robotListForEachPosition))




#------------------------------------------------
# def CreateAllCombination(robotListForEachPosition):
#   global tempObj
#   for item in robotListForEachPosition[0]:
#       if item in tempObj:
#           tempObj[item]+=1
#       else:
#           tempObj[item]=1
#   newObj={}
#   index=1
#   while index<len(robotListForEachPosition):
#       for key in tempObj.keys():
#           for item in robotListForEachPosition[index]:
#               xorItem= key^item
#               if xorItem in newObj:
#                   newObj[xorItem]+=tempObj[key]
#               else:
#                   newObj[xorItem]=tempObj[key]
#       tempObj=newObj
#       newObj={}
#       index+=1

# tempObj,tempObj={},{}
# numberOfTestCase=int(content.pop(0))
# for x in range(numberOfTestCase):
#   resultNeeded=int(list(content.pop(0).split(' '))[1])
#   robotListForEachPosition=[]
#   for y in range(4):
#       robotListForEachPosition.append([int(z) for z in content.pop(0).split(" ")])
#   CreateAllCombination(robotListForEachPosition)
#   if(resultNeeded in tempObj):
#       result=str(tempObj[resultNeeded])
#   else:
#       result="0"
#   print("Case #"+str(x+1)+": "+result)
#   tempObj={}


# def ReplaceCharAndInsert(tempList,sourceIndex,targetIndex):
#   global combinationSet,numberOfCombination
#   # tempList=list(inputList)
#   tempList[sourceIndex]=tempList[targetIndex]
#   tempString=''.join(tempList)
#   if(tempString in combinationSet):
#       return
#   numberOfCombination+=1
#   # print(tempString)
#   combinationSet.add(tempString)

# def SwapCharAndInsert(tempList,sourceIndex,targetIndex):
#   global combinationSet,numberOfCombination
#   # tempList=list(inputList)
#   temp=tempList[sourceIndex]
#   tempList[sourceIndex]=tempList[targetIndex]
#   tempList[targetIndex]=temp
#   tempString=''.join(tempList)
#   if(tempString in combinationSet):
#       return
#   # print(tempString)
#   numberOfCombination+=1
#   combinationSet.add(tempString)

# def InsertStringAsItIs(tempList,sourceIndex,targetIndex):
#   global combinationSet,numberOfCombination
#   # # tempList=list(inputList)
#   # temp=tempList[sourceIndex]
#   # tempList[sourceIndex]=tempList[targetIndex]
#   # tempList[targetIndex]=temp
#   tempString=''.join(tempList)
#   if(tempString in combinationSet):
#       return
#   print(tempString)
#   numberOfCombination+=1
#   combinationSet.add(tempString)

# def CheckAndInsertInList(inputList,sourceIndex,targetIndex):
#   if(targetIndex<0 or targetIndex> len(inputList)-1):
#       return
#   if(inputList[sourceIndex]==inputList[targetIndex]):
#       return
#   ReplaceCharAndInsert(list(inputList),sourceIndex,targetIndex)      
#   SwapCharAndInsert(list(inputList),sourceIndex,targetIndex)      

# def GetNumberOfPossibleCombination(inputList):
#   global numberOfCombinationList,numberOfCombination
#   for i in range(len(inputList)):
#       numberOfCombination=0
#       CheckAndInsertInList(inputList,i,i-1)
#       # InsertStringAsItIs(inputList,i,i)
#       CheckAndInsertInList(inputList,i,i+1)   
#       # print(numberOfCombination)    
#       numberOfCombinationList.append(numberOfCombination)     


# global combinationSet,numberOfCombination,numberOfCombinationList
# numberOfTestCase=int(input())
# for i in range(numberOfTestCase):
#   result=1
#   numberOfCombinationList=[]
#   inputString=input()
#   combinationSet=set()
#   # combinationSet.add(inputString)
#   inputList=list(inputString)
#   GetNumberOfPossibleCombination(inputList)
#   for j in range(len(numberOfCombinationList)):
#           if(numberOfCombinationList[-j-1]!=0):
#               numberOfCombinationList[-j-1]+=1
#               break
#   # print(numberOfCombinationList)
#   for j in range(len(numberOfCombinationList)):
#           if(numberOfCombinationList[j]==0):
#               continue
#           result=result*numberOfCombinationList[j]
#   # result=result*numberOfCombinationList[0]  
#   # lenCombinationSet=len(combinationSet)
#   if(result>=1000000007):
#       result=result % 1000000007
#   print("Case #"+str(i+1)+": "+str(result))