
with open('B-small-practice.in') as f:
    content = f.readlines()
T = int(content.pop(0))
for y in range(T):
    X, R, C = [int(x) for x in content.pop(0).split()]
    winner, total = "RICHARD", R * C
    if total % X != 0 or total < X or X > 6:
        pass
    elif X in [4, 5, 6] and total == 2 * X:
        pass
    elif total == X and (max(R, C) < X or min(R, C) < (X + 1 ) / 2):
        pass
    else:
        winner = "GABRIEL"
    print("Case #"+str(y+1)+": " + winner)
