exp = list("{{{")
new_exp = []
for item in exp:
    if item == "}" and len(new_exp) > 0 and new_exp[-1] == "{":
        new_exp.pop(-1)
    else:
        new_exp.append(item)
exp = new_exp
reversal = 0k

while len(exp) > 1:
    if exp[0] == "}":
        reversal += 1
    if exp[1] == "{":
        reversal += 1
    exp.pop(0)
    exp.pop(0)

if len(exp) != 0:
    print("not possible")
else:
    print(reversal)
