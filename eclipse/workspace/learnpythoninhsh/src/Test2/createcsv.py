import csv
with open('eggs.csv','wb') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    spamwriter.writerow(['Apple']*5+['Baked Beans'])
    spamwriter.writerow(['Spam','Lovely Spam','Wonderful Spam'])