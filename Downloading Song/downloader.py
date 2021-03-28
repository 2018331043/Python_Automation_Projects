from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,sys
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.mp3juices.cc/")
searchBox = driver.find_element_by_id("query")
searchBox.click();

searchBox.send_keys(" ".join(sys.argv[1:]))
searchButton=driver.find_element_by_xpath("/html/body/div[2]/form/button/i")
time.sleep(3)
ActionChains(driver).move_to_element(searchButton).click(searchButton).perform()
time.sleep(3)
#downloadButton=driver.find_element_by_class_name("download 2")
downloadButton=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div[3]/a[1]")
ActionChains(driver).move_to_element(downloadButton).click(downloadButton).perform()
time.sleep(3)
downloadButton2=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[3]/a[1]")
ActionChains(driver).move_to_element(downloadButton2).click(downloadButton2).perform()
#downloadButton.click();
#video=driver.find_element_by_id("mouseover-overlay") 1|W0DM5lcj6mw|SW1hZ2luZSBEcmFnb25zIC0gQmVsaWV2ZXIgKEx5cmljcykubXAz
#video.move_to download 2 /html/body/div[2]/div[4]/div[2]/div[3]/a[1]


#driver.quit()