from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
URL="https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.2.35e34076sLSRvB&q=mobile%20phone&_keyori=ss&clickTrackInfo=abId--379294__textId--5704130092250749346__score--223927.0__pvid--4cc43ae4-a964-495b-ba1f-67adaeefe86f__matchType--1__matchList--1__listNo--0__inputQuery--mob__srcQuery--mobile%20phone__spellQuery--mobile%20phone__ctrScore--0.0__cvrScore--0.0&from=suggest_normal&sugg=mobile%20phone_0_1"
cService=webdriver.ChromeService(executable_path="C:\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=cService)
driver.get(URL)
mobile_list=[]
mobile_div=driver.find_elements(By.XPATH,"//div[@data-qa-locator='product-item']")
for item in mobile_div:
    product = {}
    
    try:
        product['title'] = item.find_element(By.XPATH, ".//div[contains(@class, 'RfADt')]/a").text.strip()
    except:
        product['title'] = None

    # Price Fetch(Rs. 584,999)
    try:
        product['price'] = item.find_element(By.XPATH, ".//div[contains(@class, 'aBrP0')]//span").text.strip()
    except:
        product['price'] = None

    # Discount/Off Fetch(10% Off)
    try:
        product['off'] = item.find_element(By.XPATH, ".//div[contains(@class, 'WNoq3')]//span").text.strip()
    except:
        product['off'] = "No Discount"  
    # Image Link Fetch
    try:
        product['img'] = item.find_element(By.TAG_NAME, "img").get_attribute('src')
    except:
        product['img'] = None

    # Product URL 
    try:
        product['url'] = item.find_element(By.XPATH, ".//div[contains(@class, 'RfADt')]/a").get_attribute('href')
    except:
        product['url'] = None

    mobile_list.append(product)

import csv
filename = 'Week6_webscraping_selenium/daraz_products.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['title', 'price', 'off', 'img', 'url'])
    w.writeheader()
    
    for product in mobile_list:
        w.writerow(product)
driver.close()