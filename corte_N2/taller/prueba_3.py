import csv
csvfile = open('wcm.csv')
file =csv.reader(csvfile,delimiter=',')

for f in file:
    print(f)
print('fin de programa')    