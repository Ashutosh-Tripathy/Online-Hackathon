# your code goes here
def DevidedLoadEqually(leftLoad,rightLoad,leftArray,rightArray,index,array):
	if(index<len(array)-1):
		leftLoad,rightLoad,leftArray,rightArray=DevidedLoadEqually(leftLoad,rightLoad,leftArray,rightArray,index+1,array)
	if(rightLoad<leftLoad):
		rightLoad+=array[index]
		rightArray.append(index+1)
		if(rightLoad>leftLoad):
			temp=rightLoad
			rightLoad=leftLoad
			leftLoad=temp
			temp=rightArray
			rightArray=leftArray
			leftArray=temp			
	else:
		leftLoad+=array[index]
		leftArray.append(index+1)
	# print ('L: '+str(leftLoad)+'   R: '+str(rightLoad))
	# print (leftArray)
	# print (rightArray)
	return leftLoad,rightLoad,leftArray,rightArray
 
 
numberOfPacket=int(input());
array= []
for x in range(numberOfPacket):
	array.append(int(input()))
leftLoad=rightLoad=0
leftArray=[]
rightArray=[]
leftLoad,rightLoad,leftArray,rightArray= DevidedLoadEqually(leftLoad,rightLoad,leftArray,rightArray, 0,array)
for x in leftArray:
	print (x)
# print (leftArray)
# print ('L: '+str(leftLoad)+'   R: '+str(rightLoad))
# print (array)
 
 