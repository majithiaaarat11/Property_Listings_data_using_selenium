# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:09:09 2018

@author: majit
"""

from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


count=0
locations_ = ["Bhandup West","Mulund West","Powai","Kanjurmarg","Mulund","Vikhroli","Mulund East","Chandivali","Chembur","Antop Hill","Mira Road East","Virar","Nalasopara West","Nalasopara","Mira Road","Virar West","Vasai","Wadala","Sion","Kandivali East","Goregaon East","Andheri West","Malad East","Malad West","Jankalyan Nagar","Deonar","Vikhroli West","Dombivli","Badlapur East","Ambernath East","Neral Thane","Dombivli East","Titwala","Badlapur West","Kalyan West","Badlapur","Sewri","Vasai East"]
Area = []
Site_name = []
Developer = []
Transaction_type = []
Status = []
Area_sq_ft = []
Bhk = []
Price = []


driver = webdriver.Chrome()
driver.get("https://www.magicbricks.com")

for location in range(0,len(locations_)):
    loca = locations_[location]
    element = driver.find_element_by_id("keyword")
    element.send_keys(loca)
    
    search = driver.find_element_by_id("btnPropertySearch")
    search.click()
    search.submit()
    
    #main_window = driver.current_window_handle
    
    sleep(2)
    
    elements = driver.find_elements_by_class_name("m-srp-card__title")
    
    n = min(len(elements),15)
    
    for element in range(0,n):
        
        click = elements[element]
        click.click()
        allWindows = driver.window_handles
        driver.switch_to.window(allWindows[1])
    #driver.switch_to_window(main_window)
    #price = driver.find_element_by_class_name("priceSqft")
        sleep(1.5)
    #price_wind = driver.find_element_by_class_name("priceBreakupLink")
    #price_wind.click()
    
        price = driver.find_element_by_xpath("//*[@id='priceSv']")
        print(price.text)
        Price.append(price.text)        
        try:
            sqft = driver.find_element_by_xpath("//*[@id='carpetAreaDisplay']")
            print(sqft.text)
        except:
            sqft = driver.find_element_by_xpath("//*[@id='coveredAreaDisplay']")
            print(sqft.text)        
        Area_sq_ft.append(sqft.text)
        bhk = driver.find_element_by_xpath("//*[@id='propertyDetailTabId']/div[3]/div[1]/div/div[1]/div[3]/h1/span[1]")
        print(bhk.text[0])
        Bhk.append(bhk.text[0])    
        xpath_2_text = "//*[@id='fourthFoldDisplay']/div[2]/div[2]"
        xpath_3_text = "//*[@id='fourthFoldDisplay']/div[3]/div[2]"
    
        txntype_ = driver.find_element_by_xpath(xpath_3_text)
        if(txntype_.text=="New Property" or txntype_.text=="Resale"):
            txntype=txntype_
        else:
            txntype=driver.find_element_by_xpath(xpath_2_text)    
        Transaction_type.append(txntype.text)
        print(txntype.text)
    
        status = driver.find_element_by_xpath("//*[@id='fourthFoldDisplay']/div[1]/div[2]")
        print(status.text)
        Status.append(status.text)
    
        try:
            building_name = driver.find_element_by_xpath("//*[@id='projectDetailTabId']/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]")
            print(building_name.text)    
            Site_name.append(building_name.text)
            developer = driver.find_element_by_xpath("//*[@id='projectDetailTabId']/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]")
            Developer.append(developer.text[19:])
            print(developer.text[19:])
        except:
            Developer.append("NA")
            Site_name.append("NA")
        
        Area.append(loca)

        driver.close()
        driver.switch_to.window(allWindows[0])
        count=count+1
        print(count)
    driver.get("https:www.magicbricks.com")

import pandas as pd        

df1 = pd.DataFrame()
df2 = pd.DataFrame()

df1['Area']=Area
df1['Developer']=Developer
df1['Transaction_type']=Transaction_type
df1['Status']=Status
df1['Area_sq_ft']=Area_sq_ft
df1['Bhk']=Bhk
df1['Price']=Price
df2['Site_name']=Site_name

writer = pd.ExcelWriter('PropertyData.xlsx')
df1.to_excel(writer,'Details',index=False)
df2.to_excel(writer,'SiteName',index=False)
writer.save()