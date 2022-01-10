
import pandas as pd
from sklearn.preprocessing  import OneHotEncoder
import numpy as np


if __name__=="__main__":
	print("This program (UtilityFunctions.py) was called directly from python command prompt: python <file.py>")
	print()
else:
	print("This program (UtilityFunctions.py) was called by another program")
	print()

		
def data_preprocessing(data):	
	
	#Handle NaN value
	data=data.dropna()
	#data.info()
	#data_bkup=data # this wiill be used later for converting labels to numeric
	#print()
	
	#Handle categorical value (INPUT FEATURES)
	ohe=OneHotEncoder()
	ohe.fit(data[["camera (in no./mp)"]])
	#print("-----------Identified Categories: \n",ohe.categories_,"\n Feature Names : \n",ohe.get_feature_names_out())
	data_new=ohe.transform(data[["camera (in no./mp)"]]).toarray()
	data_newdf=pd.DataFrame(data=data_new,columns=ohe.get_feature_names_out())	
	
	#remaining columns
	df_oth=data[["PhoneName","Prize (in Rs.)","screensize (in inches)","RAM (in GB)","battery (in mah)"]]
	#to make it concat friendly		
	df_oth=df_oth.reset_index(drop=True) 
	
	#join input features
	inp_feat=pd.concat([df_oth,data_newdf],axis=1)
		
	return inp_feat
	

