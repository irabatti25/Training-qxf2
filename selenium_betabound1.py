from selenium import webdriver                  #import the webdriver 
import time
from selenium.webdriver import ActionChains
driver=webdriver.Firefox()
#Go to the website
driver.get("https://www.betabound.com/")
#Click on the menu tab of the webpage
elem_menu=driver.find_element_by_xpath("//span[@class='maLabel']").click()
time.sleep(5)
#Click on the start tour from menu 
elem_start_tour=driver.find_element_by_xpath("//span[text()='Start the Tour']").click()
#Starts with tour on website
elem_start_tour=driver.find_element_by_xpath("//a[@class='joyride-next-tip' and text()='Start the Tour!']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='joyride-next-tip' and text()='Next']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[@class='joyride-nub top']/following::a[@class='joyride-next-tip' and text()='Next']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='index']/div[9]/div/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='index']/div[10]/div/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='index']/div[11]/div/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='index']/div[12]/div/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='index']/div[13]/div/a[1]").click()
time.sleep(2)
#Click on the logo for getting on first page
elem_betabound_logo=driver.find_element_by_xpath("//a[@class='logo-link']")
#Select the type of beta test want to do
elem_beta_types=driver.find_element_by_xpath("//div[@class='btn btn-presets tour_betatype']").click()
#Select one type from the 'Beta Types' hover
elem_beta_web_app_beta=driver.find_element_by_xpath("//a[text()='Web App Betas']").click()
time.sleep(3)
#select first app for the te
elem_select_app=driver.find_element_by_xpath("//a[@href='https://jeevesbox.com/']")
actions=ActionChains(driver)
actions.move_to_element(elem_select_app)
actions.perform()

#Things want to personalize
driver.find_element_by_xpath("//a[@class='btn btn-personalize tour_personalize']").click()
#Deselect all the elements to select particular
driver.find_element_by_xpath("//a[@class='lnk lnk-toggleinputs']").click()
#Select 'Software'
driver.find_element_by_xpath("//label[text()='Software']").click()
#Submit it
driver.find_element_by_xpath("//input[@type='submit']").click()
#Close the driver
driver.close()
