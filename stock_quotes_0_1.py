#!/bin/python

#Author:	Yoan Hermida
#Date:		2016-09-13
#Purpose:	Scrapes Google Finance for price of major indexes and prints them.

from urllib import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

start = 'https://www.google.com/finance'

page = urlopen(start)

soup = BeautifulSoup(page, "html.parser")

dji_price = soup.find('span',{'id':'ref_983582_l'})
dji_change = soup.find('span',{'id':'ref_983582_c'})
dji_pct = soup.find('span',{'id':'ref_983582_cp'})

sp500_price = soup.find('span',{'id':'ref_626307_l'})
sp500_change = soup.find('span',{'id':'ref_626307_c'})
sp500_pct = soup.find('span',{'id':'ref_626307_cp'})

nasdaq_price = soup.find('span',{'id':'ref_13756934_l'})
nasdaq_change = soup.find('span',{'id':'ref_13756934_c'})
nasdaq_pct = soup.find('span',{'id':'ref_13756934_cp'})

print ""
print "------------------------------"
print "UPDATED: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print "------------------------------"
print ""

print("Dow Jones: " + dji_price.get_text() + " " + dji_change.get_text() + " " + dji_pct.get_text())

print ""

print("S&P 500: " + sp500_price.get_text() + " " + sp500_change.get_text()+ " " + sp500_pct.get_text())

print ""

print("Nasdaq: " + nasdaq_price.get_text() + " " + nasdaq_change.get_text()+ " " + nasdaq_pct.get_text())

raw_input("")