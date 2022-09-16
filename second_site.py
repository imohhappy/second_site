from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import keys
import random

#adding the chrome webdriver 
#driver = webdriver.Chrome()

options = Options()
options.add_argument("no-sandbox")
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options)

url = 'https://businesses.connectnigeria.com/category/agricultural-chemicals'
#the user info / the user setup
driver.get(url)
sleep(4)
companies = driver.find_elements_by_xpath('//div[@class="h-auto relative largeRadius md:flex-shrink-0 lg:mr-4"]')
print(companies)
phone2 = driver.find_elements_by_xpath('//p[@class="text-mainBlack-80 break-all font-medium"]')
address2 = driver.find_elements_by_xpath('//span[@class="text-mainBlack-80 break-all  font-medium"]')
name2 = driver.find_elements_by_xpath('//h6[@class="  break-all truncate mb-1 text-base lg:text-xl font-medium text-mainBlack-100"]')
category = url.split('/')
category = category[len(category)-1]
result = []
for i in range(len(companies)):
    """ area = companies[i]
    phone = area.find_element_by_xpath('//p[@class="text-mainBlack-80 break-all font-medium"]')
    address = area.find_element_by_xpath('//span[@class="text-mainBlack-80 break-all  font-medium"]')
    name = area.find_element_by_xpath('//h6[@class="  break-all truncate mb-1 text-base lg:text-xl font-medium text-mainBlack-100"]')
     """
    str(category.replace('-', ' ')).capitalize()
    if (len(companies) == len(address2)):
        print([ name2[i].text, category, phone2[i].text, address2[i].text])
        result.append([ name2[i].text, category, phone2[i].text, address2[i].text])

df = pd.DataFrame(result, columns=['company','address', 'phone','idx'])
df.to_excel(url[8:12]+str(random.randint(1, 15))+category+'.xlsx', sheet_name='new_sheet_name', index=False) 
print("Done Saving")

driver.quit()
""" 
def detailers_gettor(driver, url):
    driver.get(url)
    sleep( random.randint(12, 20))
    text_way = driver.page_source
    soup = BeautifulSoup(text_way, 'html.parser')
    print(soup)
    #companies = soup.find_all('div', {'class': 'h-full w-full flex flex-col sm:flex-row gap-5'})  
    companies = driver.get
    print(companies)
    #soup.get_attribute_list

    print('Saving In file...')
    for i in companies:
        aa = soup.find_parent(i)
        company_rm = i.find('h6', {"class": "break-all truncate mb-1 text-base lg:text-xl font-medium text-mainBlack-100"})
        address = driver.
        
        i.find('span', {"class": "text-mainBlack-80 break-all  font-medium"})
        phone = i.find('p', {"class": "text-mainBlack-80 break-all font-medium"})
        idx = 0
        category = url.split('/')
        category = category[len(category)-1]
        #result.append([company_rm.text, address.text, phone, idx ])
        print(aa)
        print([company_rm, address, phone, idx, category])
    df = pd.DataFrame(result, columns=['company','address', 'phone','idx'])
    df.to_excel(url[8:12]+str(random.randint(1, 15))+'.xlsx', sheet_name='new_sheet_name', index=False) 
    print("Done Saving")
detailers_gettor(driver, url) """