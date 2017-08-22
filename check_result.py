# from sortedcontainers import SortedList
import math
f = open('output.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    prev, i = "", 0
    # while i < len(line):
    #     if line[i] == prev:
    #         print(line[i-3 : i + 2])
    #         print("I: " + str(i))
    #         print(line)
    #         break
    #     else:
    #         prev = line[i]
    #     i += 1
    line = line[line.index(":")+ 2:]
    if line[0] == line[-1]:
        print(line)