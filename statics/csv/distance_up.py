# importing csv module
import csv
import datetime

# csv file name
filename = "distance.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# print(rows)

a = 'Charni Road'
b = 'Mahalaxmi'
dist_a = 0
dist_b = 0
for i in range(0, len(rows)):
    if rows[i][0] == a:
        dist_a = float(rows[i][1])

    if rows[i][0] == b:
        dist_b = float(rows[i][1])

print(dist_b-dist_a)

z = "13:12"
z = z.split(":")
print(int(z[0]))
