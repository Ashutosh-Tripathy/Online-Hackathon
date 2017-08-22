import re
with open("abc.html", 'r', encoding='utf-8') as infile:
    for line in infile:
        print(re.escape(line), end = '')