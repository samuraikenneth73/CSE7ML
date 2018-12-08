from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset = 'train', shuffle = True)
print("length of the twenty_train ...",len(twenty_train))
print(twenty_train.target_names)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data,twenty_train.target)

import numpy as np
twenty_test = fetch_20newsgroups(subset = 'test', shuffle = True)
predicted = text_clf.predict(twenty_test.data)
accuracy = np.mean(predicted == twenty_test.target)
print("Predicted Accuracy = ",accuracy)

from sklearn import metrics
print("Accuracy = ",metrics.accuracy_score(twenty_test.target,predicted))
print("Precision = ",metrics.precision_score(twenty_test.target,predicted,average = None))
print("Recall = ",metrics.recall_score(twenty_test.target,predicted,average = None))
print(metrics.classification_report(twenty_test.target,predicted,target_names = twenty_test.target_names))