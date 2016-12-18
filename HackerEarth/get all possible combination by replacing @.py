oldTempList,newTempList=[],[]
oldTempList.append(list(input()))
inputLength=len(oldTempList[0])
for i in range(inputLength):
    for item in oldTempList:
        for k in range(i,inputLength):
            if(item[k]=='?'):
                newList=list(item);
                newList[k]='0'
                newTempList.append(list(newList))
                newList=list(item);
                newList[k]='1'
                newTempList.append(list(newList))
                break
    if(len(newTempList)==0):
        break
    oldTempList=newTempList
    # print(oldTempList)
    newTempList=[]
for item in oldTempList:
    print(''.join(str(e) for e in item))       
        
    
