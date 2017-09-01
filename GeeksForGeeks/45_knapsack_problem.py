# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# vl, wl = len(val), len(wt)
# mat = [0 x for x in range(vl + 1)]
# for i in range(vl + 1):
#     for j in range(wl + 1):

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

def knapSackMulti(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                count = w // wt[i-1]
                K[i][w] = max(count * val[i-1] + K[i-1][w- count * wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]




val = [10, 100, 120]
wt = [10, 20, 30]
W = 60
n = len(val)
print(knapSackMulti(W, wt, val, n))