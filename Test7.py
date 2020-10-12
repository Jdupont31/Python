import time
from selenium import webdriver

# Test de chromedriver
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('http://www.google.com/');
time.sleep(5) 
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) 
driver.quit()
