

from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import csv
import  matplotlib.pyplot as plt

data=[]
ydata=[]
with open("cluster3.csv") as tsv:
    for line in csv.reader(tsv):
        data=[int(i) for i in line]
        ydata=[10-int(i) for i in line]

x1=np.array(data)
x2=np.array(ydata)

print(x1)
plt.plot()
plt.xlim([0,10])
plt.ylim([0,10])
plt.title('Dataset')
plt.scatter(x1,x2)
plt.show()

plt.plot()
X=np.array(list(zip(x1,x2))).reshape(len(x1),2)
colors=['b','g','r']
markers=['o','v','s']

K=3
kmeans_model=KMeans(n_clusters=K).fit(X)

plt.plot()
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x1[i],x2[i],color=colors[l],marker=markers[l],ls='None')
    plt.xlim([0,10])
    plt.ylim([0,10])
    
plt.show()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    