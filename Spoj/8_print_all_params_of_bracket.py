items = ['{}']
n = int(input())
for i in range(2, n+1):
    tmp = []
    for item in items:
        tmp.append(item + '{}')
        tmp.append('{}' + item)
        tmp.append('{' + item + '}')
    tmp.remove(i * '{}')
    items = tmp


for i in items:
    print(i)
