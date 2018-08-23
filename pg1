import csv
#hypo = ['%','%','%','%','%','%']
with open('p1.csv') as csv_file:
    read_csv = csv.reader(csv_file,delimiter=',')
    data = []
    loa = 0
    for row in read_csv:
        if row[len(row)-1].upper()=="YES":
            loa += 1
            data.append(row)
    var = len(data[0])-1
    print "The total number of positive training sets: ", var
    print "The total length of attributes: ", loa
    print "The valid training sets of the given example are:\n"

    
    for i in range(var):
        print data[0][i]
