f = open('B-small-practice.in', 'r')
T = int(f.readline())

def flipTheFlip(groups, l):
	if l == 0: return 0
	notFlip = True
	flip = True
	nfgr = []
	fgr = []

	for outs, targs in groups:
		targ1 = [x[1:] for x in targs if x[0] == '1']
		targ0 = [x[1:] for x in targs if x[0] == '0']
		outs0 = [x[1:] for x in outs if x[0] == '0']
		outs1 = [x[1:] for x in outs if x[0] == '1']

		if len(outs0) != len(targ0): notFlip = False
		else:
			if outs0: nfgr.append((outs0, targ0))
			if outs1: nfgr.append((outs1, targ1))

		if len(outs1) != len(targ0): flip = False
		else:
			if outs1: fgr.append((outs1, targ0))
			if outs0: fgr.append((outs0, targ1))

	resp = 1000000
	if notFlip:
		resp = min(resp, flipTheFlip(nfgr, l-1))

	if flip:
		resp = min(resp, 1 + flipTheFlip(fgr, l-1))
	
	return resp

for t in range(T):
	print("Case #%d: " % (t+1), end = '')

	N, L = map(int, f.readline().split())

	outlets = f.readline().split()
	targets = f.readline().split()

	flips = flipTheFlip( [(outlets, targets)], L)
	print(flips if flips <= L else "NOT POSSIBLE")



# T = int(f.readline())
# for a in range(T):
#     N, L = [int(x) for x in f.readline().strip().split()]
#     initial = [[int(y) for y in x] for x in f.readline().split()]
#     required = [[int(y) for y in x] for x in f.readline().split()]
#     impossible, flip = False, 0
#     for j in range(L):
#         icount, rcount = 0, 0
#         for i in range(N):
#             if initial[i][j] == 0: icount += 1
#             if required[i][j] == 0: rcount += 1
#         if icount == rcount:
#             continue
#         elif icount + rcount == N:
#             flip += 1
#         else:
#             impossible = True
#             break

#     if impossible:
#         print("Case #" + str(a+1) + ": " + "NOT POSSIBLE")
#     else:
#         print("Case #" + str(a+1) + ": " + str(flip))