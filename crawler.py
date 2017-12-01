from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup


def get_soup(rooturl, tag):
	url = rooturl + tag.a.attrs.get('href')
	ret = requests.get(url)
	soup = BeautifulSoup(ret.text, "lxml")
	return soup

def get_subitem(rooturl, div):
	subitem = {}
	soup = get_soup(rooturl, div)
	contents = soup.find_all('div', class_="component-product-detail")
	itemID = contents[0].find_all('div', class_="itemID")[0].attrs.get('data-item-id')
	baseurl = "https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item="
	jsonurl = baseurl + itemID
	
	details_ret = requests.get(jsonurl)
	details_json = details_ret.text

	dic = json.loads(details_json)
	for category in dic['item']['nutrient_facts']['nutrient']:
		subitem[category['name'].lower()] = float(category['value'])

	return subitem

def get_submenu(rooturl, li):
	submenu = {}
	soup = get_soup(rooturl, li)
	contents = soup.find_all('div', class_="iconic_count col-sm-6 zoom-anim-parent no-class")
	for div in contents:
		subitem = div.find('h4', class_="making-iconic-header").text.strip()
		submenu[subitem.lower()] = get_subitem(rooturl, div)
	pprint(submenu)
	return submenu


def get_menu():	
	fout = open('data.json', 'w')
	# download html source code
	hpurl = "https://www.mcdonalds.com/us/en-us.html"
	ret = requests.get(hpurl)

	# get menulist
	soup = BeautifulSoup(ret.text, "lxml")
	contents = soup.find('div', class_="menulist-flyout")
	menulist = contents.find_all(class_="vertical-middle")
	rooturl = "https://www.mcdonalds.com"
	menu = {}

	for li in menulist:
		category = li.text.strip()
		menu[category.lower()] = get_submenu(rooturl, li)
		# test = get_submenu(rooturl, li)
		# fout.write(test)

	jsonmenu = json.dumps(menu, indent = 4)
	fout.write(jsonmenu)
get_menu()


