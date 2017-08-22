items = [3, 5, 8, 11, 14, 2, 1]
5 8 11 14 3 2 1
14 5 8 11 3 2 1
14 8 11 5 3 2 1
14 11 8 5 3 2 1

n - 1 + n-2

num_sum = 0
result = [x + num_sum;num_sum += x for x in items]