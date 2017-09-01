matrix = [40, 20, 30, 10, 30]
dimension = []

for i in range(1, len(matrix)):
    dimension.append((matrix[i-1], matrix[i]))

dimension.sort()
result = 0
while len(dimension) > 1:
    i, j = dimension[0]
    counter = 1
    while counter < len(dimension):
        k, l = dimension[counter]
        if k == j:
            break
        counter += 1
    result += (i * j * l)
    dimension.pop(counter)
    dimension[0]  = (i, l)
print(result)