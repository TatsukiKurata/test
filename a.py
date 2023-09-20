import requests
from bs4 import BeautifulSoup
from Selenium import webdriver
from time import sleep
     
# r = requests.get('https://plus-info-tech.com/')
r = requests.get('https://plus-info-tech.com/contact')
     
# print("--------")
# print(r.encoding)
# print(r.content)
# print(r.headers)
print(r.text[:500])

soup = BeautifulSoup(r.content, "html.parser")
print(soup.select("form"))
