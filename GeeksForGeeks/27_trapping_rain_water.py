items = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left, right, h = 0, 0, 0
i, j = 0, len(items) - 1
water = 0
while i <= j:
    h = min(left, right)
    if left == h:
        if items[i] <= h:
            water += h - items[i]
        else:
            left = items[i]
        i += 1
    else:
        if items[j] <= h:
            water += h - items[j]
        else:
            right = items[j]
        j -= 1
print(water)

