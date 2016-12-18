from decimal import *
getcontext().prec = 14
result=Decimal(0)
with open('C-large-practice.in') as f:
    content = f.readlines()


def AddIntoNewObj(item,probability,prevProbability):
	global newObj
	# item=item*probability
	if item in newObj:
		newObj[item]=Decimal(newObj[item]+(prevProbability*probability))
	else:
		newObj[item]=Decimal(probability*prevProbability)

for i in range(int(content.pop(0))):
	result=Decimal(0)	
	oldObj,newObj={},{}
	line=content.pop(0).split(" ")
	maxIndex,num,bitWiseNum,andProbability,orProbability,xorProbability=int(line[0]),int(line[1]),int(line[2]),Decimal(int(line[3])/100),Decimal(int(line[4])/100),Decimal(int(line[5])/100)
	oldObj[num]=1
	index=1
	keys=list(oldObj.keys())
	while(len(keys)>0):
		item=keys.pop()
		# print(item)
		andItem=item & bitWiseNum
		orItem=item | bitWiseNum	
		xorItem=item ^bitWiseNum
		AddIntoNewObj(andItem,andProbability,oldObj[item])	
		AddIntoNewObj(orItem,orProbability,oldObj[item])	
		AddIntoNewObj(xorItem,xorProbability,oldObj[item])	
		if(len(keys)==0):
			oldObj	=newObj	
			keys=list(oldObj.keys())
			newObj	={}
			# print(oldObj)
			# print(index	)
			index+=1
		if(index>maxIndex):
			break
	for a in oldObj.keys():
		result+=a*oldObj[a]
	print("Case #"+str(i+1)+": "+str(result))