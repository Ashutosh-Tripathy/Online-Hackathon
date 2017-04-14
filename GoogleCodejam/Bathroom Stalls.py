# from sortedcontainers import SortedList
f = open('B-small-practice.in', 'r')
# T = int(f.readline())
# # from collections import sortedlist
# for t in range(T):
#     N, K = map (int, f.readline().strip().split())
#     # k, counter = 1, 0
#     # while k < K:
#     #     N = N // 2
#     #     k = k + pow(2, counter)
#     #     counter += 1
#     # print ('Case #%d: %d %d' % (t + 1,  N // 2, max(0, N - (N // 2) -1)))

#     slist = SortedList()
#     slist.add(N)
#     for k in range(K):
#         item = slist.pop(-1)
#         slist.add(item // 2) 
#         slist.add((item-1) // 2)    
#     print ('Case #%d: %d %d' % (t + 1,  item // 2, (item -1) // 2))





t = int(f.readline())


for tc in range(1, t + 1):
    print("Case #" + str(tc) + ": ", end = "")
    n, k = map(int, f.readline().split())
    d = {n: 1}
    lastc = None
    while k > 0:
        c = max(d)
        lastc = c
        d[(c - 1)//2] = d.get((c - 1)//2, 0) + d[c]
        d[c//2] = d.get(c//2, 0) + d[c]
        k -= d[c]
        del d[c]
    print(lastc // 2, (lastc - 1) // 2)


    
