#Start Rotate an array
arr=[1,2,3,4,5,6,7]
index=0;
Print("Rotation number.");
rotatePoint=int(input());
temp=arr[index];
Print("Press l for left or r for right")
rotatingDirection=(input);
if(rotatingDirection=="r"):
	rotatePoint=len(arr)-rotatePoint;
    endIndex=(index+rotatePoint) % len(arr);
    endCondition=len(arr)-(endIndex);

    while (index!=endCondition):
        arr[index]=arr[endIndex];
        index=endIndex;
        endIndex=(index+rotatePoint) % len(arr);
        print (arr);


        arr[endCondition]=temp;
        print (arr);

#End Rotate an array


#Start Merge sort (Recursive)
def Merge(arr,startIndex,endIndex):
    print("-------------------------------------------");    
    print (arr);
    middle=startIndex+((endIndex-startIndex)/2);
    firstArray=arr[startIndex:middle+1];
    secondArray=arr[middle+1:endIndex+1];
    firstArrIndex=len(firstArray)-1;
    secondArrIndex=len(secondArray)-1;
    # endIndex=len(arr)-1;
    
    while(endIndex>=startIndex):
        if(firstArrIndex<0):
            arr[endIndex]=secondArray[secondArrIndex];
            secondArrIndex-=1;
        elif(secondArrIndex<0):
            arr[endIndex]=firstArray[firstArrIndex];
            firstArrIndex-=1;
        elif(firstArray[firstArrIndex]>secondArray[secondArrIndex]):   
            arr[endIndex]=firstArray[firstArrIndex];
            firstArrIndex-=1;
        else:
            arr[endIndex]=secondArray[secondArrIndex];
            secondArrIndex-=1;
            endIndex-=1;
            print (arr);
            print("-------------------------------------------");
            
            
            def MergeSort(arr, startIndex,endIndex):
                if(endIndex<=startIndex):
                    return;
                    if(endIndex==startIndex+1):
                        if(arr[startIndex]>arr[endIndex]):
                            temp=arr[startIndex];
                            arr[startIndex]=arr[endIndex];
                            arr[endIndex]=temp;
                        else: 
                            middle=startIndex+((endIndex-startIndex)/2);
                            MergeSort(arr,startIndex,middle);
                            MergeSort(arr,middle+1,endIndex);
                            Merge(arr,startIndex,endIndex);        



# Merge
arr=[55,23,11,8,9,83,8,25,49,2,4,1,6,9,0,7];
print (arr);
MergeSort(arr,0,len(arr)-1);

#End Merge sort (Recursive)



#Start Merge sort (Itrative)

def Merge(arr,startIndex,endIndex):
    print("-------------------------------------------");    
    print (arr);
    middle=startIndex+((endIndex-startIndex)/2);
    firstArray=arr[startIndex:middle+1];
    secondArray=arr[middle+1:endIndex+1];
    firstArrIndex=len(firstArray)-1;
    secondArrIndex=len(secondArray)-1;
    while(endIndex>=startIndex):
        if(firstArrIndex<0):
            arr[endIndex]=secondArray[secondArrIndex];
            secondArrIndex-=1;
        elif(secondArrIndex<0):
            arr[endIndex]=firstArray[firstArrIndex];
            firstArrIndex-=1;
        elif(firstArray[firstArrIndex]>secondArray[secondArrIndex]):   
            arr[endIndex]=firstArray[firstArrIndex];
            firstArrIndex-=1;
        else:
            arr[endIndex]=secondArray[secondArrIndex];
            secondArrIndex-=1;
            endIndex-=1;
            print (arr);
            print("-------------------------------------------");
            
            def MergeSort(arr, startIndex,endIndex):
                group=2;
                startIndex=0;
                while(startIndex+group-1<len(arr)):
                    mergeStartIndex=startIndex;
                    mergeEndIndex=mergeStartIndex+group-1;
                    print(""+str(mergeStartIndex)+":"+str(mergeEndIndex));
                    while(mergeStartIndex<len(arr)):
                        print(""+str(mergeStartIndex)+":"+str(mergeEndIndex));
                        Merge(arr,mergeStartIndex,mergeEndIndex);
                        mergeStartIndex=mergeEndIndex+1;
                        mergeEndIndex= mergeStartIndex+group-1 if mergeStartIndex+group-1<len(arr) else len(arr)-1;
                        group*=2;
                        
# Merge
arr=[55,23,11,8,9,83,8,25,49,2,4,1,6,9,0,7];
print (arr);
MergeSort(arr,0,len(arr)-1);

#End Merge sort (Itrative)