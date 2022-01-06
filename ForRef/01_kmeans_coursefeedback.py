from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np

#import csv file
data=pd.read_csv("01_course_feedback.csv")
data=data.iloc[:,[0,2]] #need to incl two features
#data.info()
print()
print(data)

#plot the data

#fit the model
model=KMeans(n_clusters=2)
print(model)
model.fit_predict(data)


#print the details of the model
print()
print("model.cluster_centers_ \n",model.cluster_centers_)

print()
labels=model.labels_
print("model.labels_ \n",labels)

'''
data.insert(2,"label",labels)
print(type(data),data)
'''

print()
print("model.n_iter_ \n",model.n_iter_)
print()
print("model.n_features_in_ \n",model.n_features_in_)
print()
print("model.inertia_ \n",model.inertia_)
print()

'''
#visualize the clusters
data_label0=data[labels==0]
print(data_label0)
'''

'''
# all clusters
for i in np.unique(labels):
	plt.scatter(data[labels==i].iloc[:,0],data[labels==i].iloc[:,1],label=i)
plt.legend()
plt.show()
'''

plt.scatter(data.iloc[:,0],data.iloc[:,1])
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=200,c='red')
plt.show()












