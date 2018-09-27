from bs4 import BeautifulSoup

import requests

url = raw_input("www.pythonforbeginners.com")

r = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))




# import urllib2
# from bs4 import BeautifulSoup
#
# url = raw_input('127.0.0.1:5000/compare/compare.html')
#
# html = urllib2.urlopen('http://' +url).read()
# soup = BeautifulSoup(html)
# print soup.prettify()
#
# # extract all the tables in the HTML
# tables = soup.find_all('table')
#
# # get the class name for each
# for table in tables:
#   class_name = table['class']
#   print class_name