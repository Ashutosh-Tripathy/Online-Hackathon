with open('B-small-practice.in') as f:
    content = f.readlines()

T = int(content.pop(0))
for y in range(T):
    R1 = int(content.pop(0).strip())
    set1 = [set([int(x) for x in content.pop(0).split()]) for i in range(4)]
    R2 = int(content.pop(0).strip())
    set2 = [set([int(x) for x in content.pop(0).split()]) for i in range(4)]
    number = set1[R1 - 1].intersection(set2[R2 - 1])
    if len(number) == 1:
        result = str(number.pop())
    elif len(number) > 1:
        result = "Bad magician!"
    else:
        result = "Volunteer cheated!"
    print("Case #" + str(y+1) + ": " + str(result))
