'''
For a given set of training data examples stored in a .CSV file, implement and demonstrate the Candidate-Elimination algorithmto output a description of the set of all hypotheses consistent with the training examples.
'''
import numpy as np
import pandas as pd
data = pd.DataFrame(data = pd.read_csv('p2.csv'))
con = np.array(data.iloc[:,0:-1])
tar = np.array(data.iloc[:,-1])
def learn(con,tar):
    sh = con[0].copy()
    print("Initialization of specific hypothesis and general hypothesis")
    print(sh)
    gh = [["?"for i in range(len(sh))] for i in range(len(sh))] 
    print(gh)
    for i,h in enumerate(con):
        if tar[i] == "YES":
            for x in range(len(sh)):
                if h[x] != sh[x]:
                    sh[x] = '?'
                    gh[x][x] = '?'
        if tar[i] == "NO":
            for x in range(len(sh)):
                if h[x] != sh[x]:
                    gh[x][x] = sh[x]
		else:
		    gh[x][x] = '?'
        print("steps of candidate eliminate algorithm",i+1)
        print(sh)
        print(gh)
    indices=[i for i,val in enumerate(gh)if val == ['?','?','?','?','?','?']]
    for i in indices:
        gh.remove(['?','?','?','?','?','?'])
    return sh,gh
s,g = learn(con,tar)
print("Final sh",s)
print("Final gh",g)
