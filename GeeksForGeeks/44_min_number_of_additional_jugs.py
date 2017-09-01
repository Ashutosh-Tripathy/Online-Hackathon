from math import ceil,log
jugs = 10000003
k = 9
i = 1
while i < k and jugs > 0:
    num = 1
    while jugs > num * 2:
        num = num * 2
    jugs -= num
    i += 1    
required_jugs = 0
if jugs > 0:
    required_jugs = int(pow(2, ceil(log(jugs, 2))) - jugs)
print(required_jugs)

