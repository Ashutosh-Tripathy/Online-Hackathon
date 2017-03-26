from decimal import *
with open('B-small-practice.in') as f:
    content = f.readlines()

T = int(content.pop(0))
for y in range(T):
    C, F, X = [Decimal(x) for x in content.pop(0).split()]
    current_rate = 2
    time = 0
    while True:
        CTime = C / current_rate
        XTime = X / current_rate
        new_time = CTime + (X / (current_rate + F))
        if XTime <= new_time:
            time += XTime
            break
        else:
            time += CTime
            current_rate += F
    print("Case #" + str(y+1) + ": " + str(round(time, 8)))
