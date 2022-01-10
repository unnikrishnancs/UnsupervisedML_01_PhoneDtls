from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


#url="https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india"
url="https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india?page=16"

try:
	response=requests.get(url)
	print(response)
	data=BeautifulSoup(response.text,"lxml")
	#print(data.prettify())
	
	'''
	#captures screen, camera, RAM, battery for all the phones	
	feat_all=data.find_all("div",class_="prdp-spc__cntnt d-block ellipsis")
	for feat in feat_all:
		print(feat.text)
		print()
	'''
	
	l_phone_name=list()
	l_phone_price=list()
	l_screensize=list()
	l_camera=list()
	l_RAM=list()
	l_battery=list()
	
	all_phones=data.find("div",class_="stack-inline m-b-xl flex-grid prdts-cnt")
	#print(all_phones)
	j=1
	try:
		for phone in all_phones:
			'''
			#print(i,"\n\n",phone,"\n\n",phone.text)
			#break
			name=phone.a
			price=phone.find("span",class_="d-block txt-al-c") #handle "None" type issue
			print(i,"\n\n",name,"\n\n",name.text,"\n\n",price,"\n\n",price.text)
			phone_dtls=phone.find_all("li",class_="m-v-xs m-r-xs v-al-top")
			for feat in phone_dtls:
				print("\n\n",feat.text)
			i=i+1		
			print("==================================")
			print()
			'''
			#print(j,"\n\n",type(phone),phone.text)
			
			
			if "View Details" not in (phone.text):
				#print(j, phone)
				continue			
				
			name=phone.a
			l_phone_name.append((name.text).strip())
			#print(l_phone_name)
			price=phone.find("span",class_="d-block txt-al-c") #handle "None" type issue
			#l_phone_price.append(((price.text).replace("Rs. ","")).replace(",","")) #Replace "Rs. " and ","
			l_phone_price.append(re.sub("[Rs. ,]","",price.text)) #Replace "Rs."," " and ","
			#print(l_phone_price)
			phone_dtls=phone.find_all("li",class_="m-v-xs m-r-xs v-al-top")
			i=1
			for feat in phone_dtls:
				if i==1:
					l_screensize.append(re.sub("[•Screen \"]","",feat.text))
				if i==2:
					cam=re.sub("[• ]","",feat.text)
					cam=(cam.replace("Camera",""))
					l_camera.append(cam)
				if i==3:
					ram=re.sub("[• ]","",feat.text)
					ram=(ram.replace("GBRAM",""))
					l_RAM.append(ram)
				if i==4:
					l_battery.append(re.sub("[•mAh Battery]","",feat.text))
				i=i+1
			
			j=j+1
		
		print("Phone Name: \n",l_phone_name)
		print()
		print("Phone Prize: \n",l_phone_price)
		print()
		print("Screen Size: \n",l_screensize)
		print()	
		print("Camera: \n",l_camera)
		print()
		print("RAM: \n",l_RAM)
		print()
		print("Battery: \n",l_battery)
		print()	
			
	except Exception as exp:
		print("Error: \n",exp) # how to continue on None type error
	
	
	#Create a series object out of the list	
	phone_name=pd.Series(l_phone_name)
	#print(phone_name)

	phone_price=pd.Series(l_phone_price)
	#print(phone_price)
	
	screensize=pd.Series(l_screensize)
	#print(phone_price)
	
	camera=pd.Series(l_camera)
	#print(phone_price)
	
	RAM=pd.Series(l_RAM)
	#print(phone_price)
	
	battery=pd.Series(l_battery)
	#print(phone_price)

	#concat the series into a dataframe
	dtls_df=pd.concat([phone_name,phone_price,screensize,camera,RAM,battery],axis=1)
	dtls_df.columns=["PhoneName","Prize (in Rs.)","screensize (in inches)","camera (in no./mp)","RAM (in GB)","battery (in mah)"]
	print(dtls_df)
	
	#export as CSV file
	dtls_df.to_csv("phone_details_page16.csv",index=False)
	print("\n Exported dataframe to CSV file \n")
	
	
	
except Exception as exp:
	print("======E R R O R    O C C U R R E D ========= \n",exp)


