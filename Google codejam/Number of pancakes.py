import collections
import math
with open('B-small-practice (1).in') as f:
	content = f.readlines()

numOfTestCase=int(content.pop(0))
avg=0
def ModifyElement(numberOfPenCackesOnPlates):
	global avg
	numberOfPenCackesOnPlates.append(math.floor(numberOfPenCackesOnPlates[0]/2))
	numberOfPenCackesOnPlates[0]=math.ceil(numberOfPenCackesOnPlates[0]/2)
	# newAvg=((avg*len(numberOfPenCackesOnPlates)) -numberOfPenCackesOnPlates[0]+newMaxIndexValue)/len(numberOfPenCackesOnPlates)
	# numberOfPenCackesOnPlates[0]=newMaxIndexValue
	# avg=newAvg
	numberOfPenCackesOnPlates.sort(reverse=True)

def FindMaxPanCakeIndex(numberOfPenCackesOnPlates):
	for x in range(len(numberOfPenCackesOnPlates)-1):
		if(numberOfPenCackesOnPlates[x]>=numberOfPenCackesOnPlates[x+1]):
			return x
	# print(numberOfPenCackesOnPlates)
	return 0
previousValue=0
def IsSpecialMinuteNeeded(numberOfPenCackesOnPlates):
	global previousValue,avg
	if(previousValue==0):
		previousValue=numberOfPenCackesOnPlates[0]
	else:
		if(previousValue==numberOfPenCackesOnPlates[0]):
			counter=0
			previousValue==numberOfPenCackesOnPlates[0]
			numberOfPenCackesOnPlatesLength=len(numberOfPenCackesOnPlates)
			global avg
			avgWhenTakingSpecialMinute=(avg*numberOfPenCackesOnPlatesLength+math.ceil(numberOfPenCackesOnPlates[0]/2)+math.floor(numberOfPenCackesOnPlates[0]/2)-numberOfPenCackesOnPlates[0])/(numberOfPenCackesOnPlatesLength+1)
			avgWhenNotTakingSpecailMinute=(avg*numberOfPenCackesOnPlatesLength-numberOfPenCackesOnPlatesLength)/numberOfPenCackesOnPlatesLength
			# print("avgWhenTakingSpecialMinute :"+str(avgWhenTakingSpecialMinute))
			# print("avgWhenNotTakingSpecailMinute :"+str(avgWhenNotTakingSpecailMinute))
			avg=avgWhenTakingSpecialMinute
			return True

	counter=0
	previousValue==numberOfPenCackesOnPlates[0]
	numberOfPenCackesOnPlatesLength=len(numberOfPenCackesOnPlates)
	avgWhenTakingSpecialMinute=(avg*numberOfPenCackesOnPlatesLength+math.ceil(numberOfPenCackesOnPlates[0]/2)+math.floor(numberOfPenCackesOnPlates[0]/2)-numberOfPenCackesOnPlates[0])/(numberOfPenCackesOnPlatesLength+1)
	avgWhenNotTakingSpecailMinute=(avg*numberOfPenCackesOnPlatesLength-numberOfPenCackesOnPlatesLength)/numberOfPenCackesOnPlatesLength
	# print("avgWhenTakingSpecialMinute :"+str(avgWhenTakingSpecialMinute))
	# print("avgWhenNotTakingSpecailMinute :"+str(avgWhenNotTakingSpecailMinute))
	if(avgWhenTakingSpecialMinute>=avgWhenNotTakingSpecailMinute):
		if(len(numberOfPenCackesOnPlates)>1 and numberOfPenCackesOnPlates[0]>numberOfPenCackesOnPlates[1] and avgWhenTakingSpecialMinute==avgWhenNotTakingSpecailMinute):
			avg=avgWhenTakingSpecialMinute
			return True
		return False
	else:
		avg=avgWhenTakingSpecialMinute
		return True

for i in range(numOfTestCase):
	numberOfMinute,avg=0,0
	content.pop(0).replace('\n','')
	numberOfPenCackesOnPlates=[int(x) for x in content.pop(0).replace('\n','').split(" ")]
	numberOfPenCackesOnPlates.sort(reverse=True)
	# print(numberOfPenCackesOnPlates)
	for item in numberOfPenCackesOnPlates:
		avg+=item
	avg=avg/len(numberOfPenCackesOnPlates)
	# print("avg: "+str(avg))
	while (IsSpecialMinuteNeeded(numberOfPenCackesOnPlates)):
		ModifyElement(numberOfPenCackesOnPlates)
		# print("In loop")
		numberOfMinute+=1
		# print(numberOfPenCackesOnPlates)
		
	numberOfMinute+=numberOfPenCackesOnPlates[0]
	# print(numberOfPenCackesOnPlates)
	print("Case #"+str(i+1)+": "+str(numberOfMinute))
	