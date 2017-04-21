import csv
import json

with open('example.csv', 'w', newline = '') as csvfile:
    fieldnames = ['First name', 'Last name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    names = [['Ashu', 'trip'], ['abc', 'def'], ['dgh', 'dcd']]
    writer.writeheader()
    for name in names:
        row = json.loads('{"First name": "%s", "Last name": "%s"}'%(name[0], name[1]))
        writer.writerow(row)