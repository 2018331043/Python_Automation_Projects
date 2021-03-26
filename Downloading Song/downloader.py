from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("http://nagordola.com.bd/")
searchBox = driver.find_element_by_id("search")
searchBox.click();
#ActionChains(driver).move_to_element(searchBox).click(searchBox).perform()
searchBox.send_keys("behula"+Keys.RETURN)
#video=driver.find_element_by_id("mouseover-overlay")
#video.move_to


#driver.quit()