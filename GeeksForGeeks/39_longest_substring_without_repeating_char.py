name = 'GEEKSFORGEEKS'
result, tempresult = [], []
char_set = set()
for i in range(len(name)):
    if name[i] in char_set:
        char_set = set()
        tempresult = []
    char_set.add(name[i])
    tempresult.append(name[i])
    if len(result) < len(tempresult):
        result = tempresult
print(result) 