import csv
hypo = ['%','%','%','%','%','%']
with open('p1.csv') as csv_file:
    read_csv = csv.reader(csv_file,delimiter=',')
    data = []
    loa = 0
    for row in read_csv:
        if row[len(row)-1].upper()=="YES":
            data.append(row)
    var = len(data[0])-1
TotExamples = len(data)
i=0
j=0
k=0
print('Steps of Find-s Algorithm :')
list = [] 
p=0
d = len(data[p])-1;
for j in range(d):
    list.append(data[i][j])
hypo = list
i=1
for i in range(TotExamples):
    for k in range(d):
        if hypo[k] != data[i][k]:
            hypo[k] = '?'
            k += 1
        else:
            hypo[k]
        #print(hypo)#dataset
i += 1
print('Max Specific Find-S hypothesis for given csv are:')
list = []
for i in range(d):
    list.append(hypo[i])
print(list)
