import csv
import math
import random
def majorClass(a,d,t):
	freq = {}
	index = a.index(t)
	for tuple in d:
		if tuple[index] in freq:
			freq[tuple[index]] +=1
		else:
			freq[tuple[index]] =1
	max = 0
	major = ''
	for key in freq.keys():
		if freq[key] > max:
			max = freq[key]
			major = key
	return major
def entropy(a,d,t):
	freq = {}
	dE = 0
	i = 0
	for entry in a:
		if(t == entry):
			break
		i += 1
	i -= 1
	
	for entry in d:
		if entry[i] in freq:
			freq[entry[i]] +=1
		else:
			freq[entry[i]] =1
	
	for freq in freq.values():
		dE += (-freq/len(d))*math.log(freq/len(d),2)
	return dE
def info_gain(at,d,a,t):
	freq = {}
	ssE = 0
	i = at.index(attr)
	for entry in d:
		if entry [i] in freq:
			freq[entry[i]] += 1
		else:
			freq[entry[i]] = 1
	for val in freq.keys():
		vP = freq[val]/sum(freq.values())
		dSs = [entry for entry in d if entry[i] == val]
		ssE += vP * entropy(a,dS,t)
	return (entropy(at,d,t)-ssE)
def attr_choose(d,a,t):
	best = a[0]
	maxGain = 0
	for attr in a:
		newGain = info_gain(at,d,a,t)
		if newGain > maxGain:
			maxGain = newGain
			best = attr
	return best
def get_values(d,at,a):
	index = at.index(a)
	values = []
	for entry in d:
	if entry[index] not in values:
		values.append(entry[index])
	return values
def  get_data(d,at,b,v):
	new_data = [[]]
	index = at.index(b)
	for entry in d:
		if entry[index] == v:
			newEntry= []
	for i in range(0,len(entry)):
		if(i != index):
			newEntry.append(entry[i])
	new_data.remove([])
	return new_data
def build_tree(d,a,t):
	d = d[:]
	vals = [record[a.index(t)] for record in data]
	default = majorClass(a,d,t)
	if not data or (len(a)) -1 <= 0:
		return default
	elif vals.count(vals[0]) == len(vals):
		return vals[0]
	else:
		best = attr_choose(d,a,t)
		tree = {b:{}}
	for val in get_values(d,a,b):
		new_data = get_data(d,a,b,v)
		nA = a[:]
		nA.remove(b)
		subtree = build_tree(new_data,newAttr,t)
		tree[best][val] = subtree
	return  tree
def execution_decision_tree():
	d = []
	with open('p3.csv') as tsv:
		for line in csv.reader(tsv):
			d.append(tuple(line))
		print('Number of records: ',len(d))
		at = ['outlook','temperature','humidity','wind','play']
		t = a[-1]
		acc = []
		training_set = [ x for i,x in enumarate(d)]
		tree = build_tree(training_set,at,t)
		print(tree)
		results = []
		test_set = [('rainy','mild','high','strong')]
		for entry in test_set:
			tempDict = tree.copy()
			result = ''
			while(isinstance(tempDict,dict)):
				child = []
				nodeVal = next(iter(tempDict))
				child = tempDict[next(iter(tempDict))].keys()
				tempDict = tempDict[next(iter(tempDict))]
				index = a.index(nodeVal)
				value = entry[index]
				if value in tempDict.key():
					result = tempDict[value]
					tempDict = tempDict[value]
				else:
					result = 'Null'
					break
				if result != 'Null':
					results.append(result==entry[-1])
				print(result)
if __name__ == '__main__':
	execute_decision_tree()					
