arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]

def get_max_window(arr, m):
    zero_count = 0
    wl, wr = 0, 0
    bestl, bestw = 0, 0
    while wr < len(arr):
        if zero_count <= m:
            if arr[wr] == 0:
                zero_count += 1
            wr += 1
        while zero_count > m:
            if arr[wl] == 0:
                zero_count -= 1
            wl += 1
        if wr - wl > bestw:
            bestl = wl
            bestw = wr - wl
    
    for i in range(bestl, bestl + bestw):
        if arr[i] == 0:
            print(i)
        
get_max_window(arr, 2)