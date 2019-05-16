import csv

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:

        profit = row[13]
        print(profit)
Fruits = row [13]
Fruits = 0

print("Total Profit")