def find_count(item):
    result, charset = 0, set(item)
    for char in charset:
        count = item.count(char)
        combination = int(count * (count -1)/2)
        result += count + combination
    print(result)

find_count("aba")