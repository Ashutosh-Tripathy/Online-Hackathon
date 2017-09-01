arr = [3, 2 , 7 , 10]
exl, incl, new_exl = 0, 0, 0
for item in arr:
	new_exl = max(exl, incl)
	incl = exl + item
	exl = new_exl
print(max(incl,exl))