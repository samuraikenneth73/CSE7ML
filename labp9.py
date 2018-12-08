import pandas as pd
dataset=pd.read_csv('iris.csv')
feature_columns=['sepal_length','sepal_width','petal_length','petal_width']
x=dataset[feature_columns].values
y=dataset['species'].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("y_pred,y_test")
for i in range (len(y_pred)):
    print(y_pred[i]," ",y_test[i])

from sklearn.metrics import confusion_matrix
cm=confusion_matrix (y_test,y_pred)
print("confusion matrix:")
print(cm)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)*100
print('accuracy of our model is equal' + str(round(accuracy,2)) + '%.')
