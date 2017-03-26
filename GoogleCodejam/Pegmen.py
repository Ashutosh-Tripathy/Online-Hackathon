
with open('B-small-practice.in') as f:
    content = f.readlines()

def has_arrow(r, c, diri, dirj):
    while True:
        r += diri
        c += dirj
        if (r < 0 or r >= R or c < 0 or c >= C):
            return False
        if (mat[r][c] == '.'):
            continue
        else:
            return True

T = int(content.pop(0))
for y in range(T):
    count = 0
    impossible = False
    R, C = map(int, content.pop(0).split())
    # mat, pair, allowed, count = [], {'>' : '<', 'v' : '^'}, {'>', 'v'}, 0
    dirs = {'>' : [0, 1], '<' : [0, -1], 'v' : [1, 0], '^' : [-1, 0]}
    mat = [[x for x in content.pop(0).strip()] for r in range(R)]

    for r in range(R):
        for c in range(C):
            if mat[r][c] == '.':
                continue
            diri, dirj = dirs[mat[r][c]]
            if (has_arrow(r, c, diri, dirj)):
                continue
            can_save = False
            for dir in dirs:
                diri, dirj = dirs[dir]
                if(has_arrow(r, c, diri, dirj)):
                    can_save = True
            if can_save:
                count += 1
            else:
                impossible = True
    if impossible:
        print("Case #" + str(y+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(y+1) + ": " + str(count))
