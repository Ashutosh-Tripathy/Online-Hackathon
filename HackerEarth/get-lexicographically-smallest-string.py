def GetLexicographicallySmallestString(inputString,numberOfCharCanCut):
    charIndexToReplace=0
    indexAlreadyReplaced=  set()
    for i in range(len(inputString)):
        if(numberOfCharCanCut<=0):
            break
        charIndexToReplace=i
        for j in range(i+1,len(inputString)):
            if(numberOfCharCanCut>1):
                if(inputString[j]<inputString[i]):
                    if(charIndexToReplace!=i):
                        if(inputString[charIndexToReplace]>=inputString[j]):
                            charIndexToReplace=j
                    else:
                        charIndexToReplace=j                                                                                               
            elif(j in indexAlreadyReplaced and inputString[j]<inputString[i]):
                    if(charIndexToReplace!=i):
                        if(inputString[charIndexToReplace]>=inputString[j]):
                            charIndexToReplace=j
                    else:
                        charIndexToReplace=j 
            elif (i in indexAlreadyReplaced and inputString[j]<inputString[i]):
                    if(charIndexToReplace!=i):
                        if(inputString[charIndexToReplace]>=inputString[j]):
                            charIndexToReplace=j
                    else:
                        charIndexToReplace=j
                                     
        if(i!=charIndexToReplace):
            temp=inputString[i]
            inputString[i]=inputString[charIndexToReplace];
            inputString[charIndexToReplace]=temp
            if(charIndexToReplace in indexAlreadyReplaced):
                numberOfCharCanCut-=1
            elif(i in indexAlreadyReplaced):
                numberOfCharCanCut-=1
            else:
                indexAlreadyReplaced.add(charIndexToReplace)
                numberOfCharCanCut-=2
        # print('charIndexToReplace: '+str(charIndexToReplace))        
        # print(inputString)
        # print('numberOfCharCanCut: '+str(numberOfCharCanCut))
                
    return inputString                
                
        
            
            
    

firstInputString=raw_input().split(' ')
stringLength=int(firstInputString[0])
numberOfCharCanCut=int(firstInputString[1])
inputString=list(raw_input())
# sortedCharList=CreateSortedListOfChar(inputString)
result=GetLexicographicallySmallestString(inputString,numberOfCharCanCut) 
print(str(''.join(result)))