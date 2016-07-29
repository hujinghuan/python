import csv
with open('d:\pydata\pydata-book\ch02\names\yob1880.txt','rb') as csvfile:
    spamreader = csv.reader(csvfile,dialect='excel')
    for row in spamreader:
        print','.join(row)