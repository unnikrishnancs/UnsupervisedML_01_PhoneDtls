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
	
	all_phones=data.find_all("div",class_="stack-inline m-b-xl flex-grid prdts-cnt")
	#print(all_phones)

	for phone in all_phones:
		name=phone.find("a",class_="productSKULink ellips-line nav--snhdr ttl-height m-b-xs txt-al-c m-t-m txt-m ellips-line-ell-2 product_link-105700")
		price=phone.find("span",class_="d-block txt-al-c")
		print(name.text,price.text)

	
	
except Exception as exp:
	print("======E R R O R    O C C U R R E D ========= \n",exp)


