from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from UtilityFunctions00 import *


#import csv file
data=pd.read_csv("phone_details_upd.csv",na_values=["N/A"," "])
#data=data.iloc[:,[1,2,4,5]] #ignore 'camera' for now
data.info()
print()
print(data.head())

#pre-process "camera" column
data=data_preprocessing(data)
data.info()
print()
print(data.head())

#take all columns except "PhoneName"
data=data.iloc[:,1:]
print(data.head())


# Include all feature and use PCA to extract two principal components
#apply PCA
pca=PCA(2)
data=pca.fit_transform(data)


#plot the raw data
'''
plt.scatter(data.iloc[:,0],data.iloc[:,1])
#plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=200,c='red')
plt.xlabel("Phone Price ->")
plt.ylabel("?? ->")
plt.show()
'''

#fit the model
model=KMeans(n_clusters=5)
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

data=pd.DataFrame(data=data)
data.columns=["PC1","PC2"]
print(data)

#insert labels against each observation
data.insert(2,"label",labels)
print(type(data),data)


# all clusters
for i in np.unique(labels):
	plt.scatter(data[labels==i].iloc[:,0],data[labels==i].iloc[:,1],label="Cluster"+str(i))
plt.legend()

plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c='red')

#format plot
plt.xlabel("PC1 -> ")
plt.ylabel("PC2 -> ")
plt.title("Mobile Price Vs Features")
plt.tight_layout()


plt.show()

