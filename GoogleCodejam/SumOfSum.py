import collections

with open('D-large-practice.in') as f:
	content = f.readlines()

def GetSumAndPrint(od, startIndex,endIndex):
	result=0
	startIndex-=1
	diff=endIndex-startIndex
	keys=[item for item in od]
	while (True):
		key=keys.pop(0)
		if(startIndex-od[key]<0):
			result+=(od[key]-startIndex)*key
			diff=diff-od[key]+startIndex
			break
		else:
			startIndex-=od[key]
	# startIndex+=diff
	while (len(keys)>0):
		key=keys.pop(0)
		if(diff-od[key]<0):
			result+=(diff)*key
			break
		result+=od[key]*key
		diff-=od[key]
	# result+=od[keys.pop()]*startIndex
	print(result)

def AddIntoDict(dict,item):
	if(item in dict):
		dict[item]+=1
	else:
		dict[item]=1

numOfTestCase=int(content.pop(0))

for i in range(numOfTestCase):
	numberOfQueries=int(content.pop(0).split(" ")[1])
	inputArr=[int(z) for z in content.pop(0).split(" ")]
	numberOfPossibleSubArray=0
	sumArray={}
	oldList,newList={},{}
	AddIntoDict(oldList,inputArr[0])
	for x in range(1,len(inputArr)):
		AddIntoDict(newList,inputArr[x])
		for item in oldList:
			AddIntoDict(sumArray, item)
			AddIntoDict(newList, item+ inputArr[x])
		oldList=newList
		newList={}

	for item in oldList:
		AddIntoDict(sumArray,item)
	# print(sumArray)
	od = collections.OrderedDict(sorted(sumArray.items()))
	# print(od)
	sumArray={}
	oldList={}
	print("Case #"+str(i+1)+": ")
	# print(len(sumArray))
	for j in range(numberOfQueries):
		indexString=content.pop(0).split(" ")
		startIndex,endIndex=int(indexString[0]),int(indexString[1])
		GetSumAndPrint(od, startIndex,endIndex)	
		# print(str(i)+" query compltd: "+str(j))
	od={}
	# print(sumArray)

