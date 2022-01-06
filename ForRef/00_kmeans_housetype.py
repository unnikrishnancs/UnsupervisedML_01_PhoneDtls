from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#import csv file
data=pd.read_csv("00_house_type.csv")
data.info()
print()
print(data.tail())

#convert housetype to numeric
le=LabelEncoder()
le.fit(data)
print("le.classes_ \n",le.classes_)
data=le.transform(data)

#fit the model
model=KMeans(n_clusters=3)
model.fit(data.reshape(-1,1))

#print the details of the model
print()
print("model.cluster_centers_ \n",model.cluster_centers_)
print()
print("model.labels_ \n",model.labels_)
print()
print("model.n_iter_ \n",model.n_iter_)
print()
print("model.n_features_in_ \n",model.n_features_in_)
print()
print("model.inertia_ \n",model.inertia_)
print()


