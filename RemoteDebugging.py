from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
import time
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.keys import Keys

#open cmd and run this comments:chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r'C:\\Users\\ddand\\Downloads\\chromedriver\\chromedriver.exe'
#driver = webdriver.Chrome(chrome_options=options , executable_path=chrome_driver)
driver = webdriver.Chrome(options=options , executable_path=chrome_driver)

print(driver.title)
#
# e1=driver.find_element(By.XPATH,"//ul[@class='ratinglist finalRatings']//following::p").text
# lis=re.split('(|)',e1)
# print(int(lis[4]))
#
# # driver.find_element(By.XPATH,"//a[contains(text(),' Rate')]").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//a[contains(text(),' Rate')]//following::ul/li[1]/a/img").click()
#
# att=driver.find_element(By.XPATH,"//ul[@class='ratinglist finalRatings']/li[1]/a/img").get_attribute('src')
# print(att)




# ti = driver.find_elements(By.XPATH, "//div[@class='help-desk ng-star-inserted']/div//child::img[@title='Details']")
# for l in range(len(ti)):
#     print(driver.find_element(By.XPATH,"//div[@class='help-desk ng-star-inserted']/div//child::h3").text)
#     print(driver.find_element(By.XPATH,"//div[@class='help-desk ng-star-inserted']/div//child::p[1]").text)
#     cat=driver.find_element(By.XPATH, "//div[@class='help-desk ng-star-inserted']/div//child::p[2]").text
#     lis=cat.split(': ')
#     print(lis[1])
#
#     print(driver.find_element(By.XPATH, "//ul[@class='rate-area']").is_displayed())
#     ti[l].click()
#     time.sleep(3)
#     print(driver.find_element(By.XPATH,"//label[contains(text(),'Description *')]//following::div[@class='note-editable'][1]").text)
#     username=driver.find_element(By.XPATH,"//span[@class='ng-value-label ng-star-inserted']").text
#     print(" ".join(username.split()))
#     time.sleep(3)
#     driver.find_element(By.XPATH,"//button[contains(text(),'Cancel')]").click()
#     break



#driver.find_element(By.XPATH,"//i[@title='Filter']").click()

#driver.find_element(By.XPATH,"//*[@formcontrolname='withmentees']//ancestor::label/span[1]").click()
# el=driver.find_element(By.XPATH,"//span[contains(text(),'Experiencing a loss at work')]//parent::label/input")
# print(el.is_selected())



driver.find_element(By.XPATH,"//i[@title='Filter']").click()

time.sleep(10)



















# before_XPath = "//div[@class='row ng-star-inserted']/div["
# aftertd_XPath_1 = "]/div"
# midle_xpath="//ancestor::ul[@class='dotes-member-ul']/li["
# last_xpath="]/img"
# afterpatname="]/div//ancestor::div[@class='title']/div[1]"
#
# a=0
# totalcounts=len(driver.find_elements(By.XPATH,"//div[@class='row ng-star-inserted']/div"))
# for t_row in range(1, (totalcounts + 1)):
#     FinalXPath = before_XPath + str(t_row) + aftertd_XPath_1
#     FinalXPath2 = before_XPath + str(t_row) + afterpatname
#     cell_text = driver.find_element_by_xpath(FinalXPath2).text
#     print(cell_text)
#     #print(cell_text)
#     for t_col in range(1,4):
#         FinalXPath1 = FinalXPath+midle_xpath+str(t_col)+last_xpath
#         try:
#             t=driver.find_element_by_xpath(FinalXPath1).get_attribute('title')
#             print(t)
#         except:
#             print("...............E")















