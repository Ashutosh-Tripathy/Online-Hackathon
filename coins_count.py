def get_change(M, P):
    price = M * 100 - P * 100
    currency = [1, 5, 10, 25, 50, 100]
    result = []
    while len(currency) > 0:
        coin = currency.pop()
        if price >= coin:
            result.insert(0, int(price // coin))
            price = price % coin
        else:
            result.insert(0, 0)
    return result


# print(get_change(5, .99))
# print(get_change(4, 3.14))
print(get_change(.45, .34))
# print(get_change(5, .99))
