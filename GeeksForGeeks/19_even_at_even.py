num = [5,2,6,8,10,16, 18,11,19]

even, odd = {}, {}
for i in range(len(num)):
    if i % 2 == 1:
        if num[i] % 2 != 1:
            if len(odd) == 0:
                even[i] = num[i]
            else:
                key, value = list(odd.keys())[0], odd[list(odd.keys())[0]]
                del odd[key]
                num[i],num[key] = value, num[i]
    else:
        if num[i] % 2 != 0:
            if len(even) == 0:
                odd[i] = num[i]
            else:
                key, value = list(even.keys())[0], even[list(even.keys())[0]]
                del even[key]
                num[i],num[key] = value, num[i]

print(num)



