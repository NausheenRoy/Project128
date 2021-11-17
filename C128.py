from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests;

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:/Users/TRUSTANA MARKETING/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)
data = []
planet_data=[]
headers=["Name","Distance","Mass","Radius"]
page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')
time.sleep(20)

def scrape():
    headers=["Name","Distance","Mass","Radius"]
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for i in 1:                                                            
        for tr_tag in soup.find_all("tr",attrs={"class","wikitable sortable jquery-tablesorter"}):
            td_tags= tr_tag.find_all("td")
            temp_list=[]
            for index,tr_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)

scrape()
final_planet_data = []
for index,data in enumerate(data):
    final_planet_data.append(data+planet_data[index])

with open("scrapper.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_planet_data)

