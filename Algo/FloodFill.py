import subprocess as sp
import time;
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1],
          ];

def flood_fill():
    x, y , c = 4, 4, 3
    X, Y = len(screen) -1,len(screen[0]) -1
    nodes = []
    if screen[x][y] == c:
        return

    if x >= len(screen) or y >= len(screen[0]):
        return
    oldc = screen[x][y]
    nodes.append((x, y))

    while nodes:
        i, j = nodes.pop()
        if screen[i][j] != oldc:
            continue
        screen[i][j] = c
        nodes.append((max(i-1, 0), j))
        nodes.append((i, min(j + 1, Y)))
        nodes.append((min(i +1, X), j))
        nodes.append((i, max(j - 1, 0)))
        print("\n".join([",".join([str(y) for y in x]) for x in screen]))
        print(nodes)
        print("_____________________")
        time.sleep(2)
        # sp.call('cls')
        sp.call('cls',shell=True)

flood_fill()

print("\n".join([",".join([str(y) for y in x]) for x in screen]))