from bs4 import BeautifulSoup
import requests

url="https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india"

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
	
	all_phones=data.find("div",class_="stack-inline m-b-xl flex-grid prdts-cnt")
	#print(all_phones)
	i=1
	try:
		for phone in all_phones:
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
	except:
		print("Error") # how to continue on None type error
	
	
except Exception as exp:
	print("======E R R O R    O C C U R R E D ========= \n",exp)


