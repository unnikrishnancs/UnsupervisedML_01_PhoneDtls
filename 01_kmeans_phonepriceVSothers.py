from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np




#import csv file
data=pd.read_csv("phone_details.csv")
data=data.iloc[:,[1,5]] #...need to incl two features
#data.info()
print()
print(data)


# Include all feature and use PCA to extract two principal components


#plot the raw data
'''
plt.scatter(data.iloc[:,0],data.iloc[:,1])
#plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=200,c='red')
plt.xlabel("Phone Price ->")
plt.ylabel("?? ->")
plt.show()
'''

#fit the model
model=KMeans(n_clusters=3)
print(model)
model.fit_predict(data)

#print the details of the model
print()
print("model.cluster_centers_ \n",model.cluster_centers_)
print()
print("model.n_iter_ \n",model.n_iter_)
print()
print("model.n_features_in_ \n",model.n_features_in_)
print()
print("model.inertia_ \n",model.inertia_)
print()

#add the labels against each datapoint in the dataframe
labels=model.labels_
print("model.labels_ \n",labels)
data.insert(2,"label",labels)
print(type(data),data)


# all clusters
for i in np.unique(labels):
	plt.scatter(data[labels==i].iloc[:,0],data[labels==i].iloc[:,1],label="Cluster"+str(i))
plt.legend()

plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c='red')
plt.show()


