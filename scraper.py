# coding:utf-8
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import urlopen
from selenium import webdriver
import time


base_url = "https://www.d-deltanet.com/pc/"
base_slot_url = "https://www.d-deltanet.com/pc/HallSelectLink.do?hallcode={0}#20slot"
slot_url = base_slot_url.format(23999290)


#
# slot_html = urlopen(slot_url)
# print (slot_url)
# soup = BeautifulSoup(slot_html,"lxml")
# links = soup.findAll("td",{"class":"clear"})
# # links = soup.findAll("input")
# for link in links:
#     # if ".do" in link:
#     print (link)

browser = webdriver.Firefox()
# browser = webdriver.Chrome()

# browser = webdriver.PhantomJS("/usr/bin")
browser.get(slot_url)
time.sleep(1)

# links = browser.find_elements_by_xpath('//th[@id="20slot"]')
buttons = browser.find_elements_by_xpath('//input[@name="select"]')
for i in range(len(buttons)):
    print (i)
    buttons = browser.find_elements_by_xpath('//input[@name="select"]')
    buttons[i].click()
    time.sleep(1.0)
    browser.back()
    time.sleep(1.0)
browser.quit()
