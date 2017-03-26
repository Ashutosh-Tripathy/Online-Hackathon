
with open('B-small-practice.in') as f:
    content = f.readlines()
import copy

def get_pelindrom_length():
    if L > S:
        return 0
    o = max(i for i in range(L) if T.endswith(T[:i]))
    m = (S - o) // (L - o)
    e = S - L + 1
    for l in T:
        e *= M.count(l) / K
    if e == 0:
        return 0
    return m - e

N = int(content.pop(0))
for y in range(N):
    K, L, S = map(int, content.pop(0).split())
    M = content.pop(0).strip()
    T = content.pop(0).strip()
    # print(best_case, probability, best_case - (best_case * probability))
    print("Case #"+str(y+1)+": " + str(get_pelindrom_length()))











    # key_map = {}
    # for k in key:
    #     if k not in key_map:
    #         key_map[k] = 0
    #     key_map[k] += 1
    # palindrome_length = L - 1 if req.count(req[0]) == L else 0
    # if palindrome_length == 0 and req.count(req[0]) > 1:
    #     palindrome_length = get_pelindrom_length()

    # best_case = 1 + (S - L) // (L - palindrome_length)
    # probability = 1
    # counter = 0
    # for i in range(S):
    #     if (req[counter] not in key_map):
    #         probability = 0
    #         best_case = 0
    #         break
    #     probability *= key_map[req[counter]] / K
    #     counter = min (counter + 1, L -1 - palindrome_length)
    # probability = min(probability + (probability * ((S - L) // (L - palindrome_length))), 1)
