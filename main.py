from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('Users/Efosa1/Downloads/chromedriver')
driver.get('https://csgoempire.com/withdraw#730')
item = driver.find_element(By.CLASS_NAME, 'item item--trading item--undefined item--instant-withdraw item--730')
itemName = item.find_element(By.XPATH, './/*[@id="page-scroll"]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]').text

print(itemName, "jj")
