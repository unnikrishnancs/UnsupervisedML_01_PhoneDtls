from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np


#import csv file
data=pd.read_csv("phone_details_upd.csv",na_values=["N/A"," "])
data.info()
#print(data["battery (in mah)"].value_counts())

#drop nan values
data=data.dropna()
data.info()

'''
#plot the raw data
plt.scatter(data.iloc[:,1],data.iloc[:,5])
plt.xlabel("Phone Price ->")
plt.ylabel("Battery (in mAh) ->")
plt.show()
'''

#extract two columns
yaxis="Battery (in mAh) ->"
data=data.iloc[:,[1,5]]


#data.info()
print()
print(data.head())


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

labels=model.labels_
print("model.labels_ \n",labels)

#add the labels against each datapoint in the dataframe
data.insert(2,"label",labels)
print(type(data),data)


#plot the clusters
for i in np.unique(labels):
	plt.scatter(data[labels==i].iloc[:,0],data[labels==i].iloc[:,1],label="Cluster"+str(i))
plt.legend()

#plot the cluster center
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c='red')

#format plot
plt.xlabel("Mobile Price -> ")
plt.ylabel(yaxis)
plt.title("Mobile Price Vs Features of phone")
plt.tight_layout()

plt.show()

