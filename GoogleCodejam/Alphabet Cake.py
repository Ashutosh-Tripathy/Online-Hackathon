# from sortedcontainers import SortedList
import math
f = open('B-small-practice.in', 'r')
t = int(f.readline())

def fill_element(G,item, r, c):
    column = [G[i][c] for i in range(R)]
    row_count,column_count = G[r].count(item), column.count(item)
    
    if row_count > 1 and column_count > 1 and G[r].count(item) != len(G[r]) and column.count(item) != len(column):
        minr, maxr = column.index(item), len(column) - column[::-1].index(item) - 1
        minc, maxc = G[r].index(item), len(G[r]) - G[r][::-1].index(item) - 1
        while minr <= maxr:
            while minc <= maxc:
                G[minr][minc] = item
                minr += 1
                minc += 1
    elif row_count > 1 and G[r].count(item) != len(G[r]) :
        minc, maxc = G[r].index(item), len(G[r]) - G[r][::-1].index(item) - 1
        while minc <= maxc:
            G[r][minc] = item
            minc += 1
    elif column_count > 1 and column.count(item) != len(column):
        minr, maxr = column.index(item), len(column) - column[::-1].index(item) - 1
        while minr <= maxr:
            G[minr][c] = item
            minr += 1
    elif G[r].count("?") == len(G[r]) - 1:
        for j in range(C):
            G[r][j] = item
    elif column.count("?") == len(column) - 1:
        for i in range(R):
            G[i][c] = item
for tc in range(1, t + 1):
    print("Case #" + str(tc) + ": ")
    R, C = map(int, f.readline().split())
    G = []
    [G.append([y for x in f.readline().strip().split() for y in x]) for r in range (R)]
    lastchar = '.'
    for r in range(R):
        for c in range(C):
            if G[r][c] == "?":
                continue
            fill_element(G, G[r][c], r, c)
    print("\n".join(["".join(x) for x in G]))




