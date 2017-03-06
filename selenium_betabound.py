from selenium import webdriver                  #import the webdriver 
import time                                     #import the time
#select the Chrome browser
driver=webdriver.Firefox()

#Go to the website
driver.get("https://www.betabound.com/")
driver.maximize_window()
str1=driver.current_window_handle


#Click on the menu tab of the webpage
elem_menu=driver.find_element_by_xpath("//span[text()='Menu']").click()
time.sleep(2)
#Click on the start tour from menu 
elem_start_tour=driver.find_element_by_xpath("//span[text()='Start the Tour']").click()

#It is the welcome window, it takes us on tour.
elem_start_tour=driver.find_element_by_xpath("//a[text()='Start the Tour!']").click()
time.sleep(1)
#It tells what betabound does
driver.find_element_by_xpath("//div[@data-index='1']/descendant::a[text()='Next']").click()
time.sleep(1)
#It tells about the various beta types hover on which betabound work and we need to choose one
driver.find_element_by_xpath("//h2[text()='Choose a Filter']/ancestor::div[@class='joyride-tip-guide adjustTopLower step3']/descendant::a[text()='Next']").click()
time.sleep(1)
#It tells that there is an option to create a custom filter
driver.find_element_by_xpath("//h2[text()='Create a Custom Filter']/ancestor::div[@class='joyride-content-wrapper']/descendant::a[text()='Next']").click()
time.sleep(1)
#It tells by singing up we can be a member of betabound.
driver.find_element_by_xpath("//div[@data-index='4']/descendant::a[text()='Next']").click()
time.sleep(1)
#It shows all the social media where they put their opportunities.
driver.find_element_by_xpath("//span[@class='joyride-nub right']/following::a[text()='Next']").click()
time.sleep(1)
#Here it shows a 'Submit a Beta' where we can give our feedback
driver.find_element_by_xpath("//a[text()='Almost there...']").click()
time.sleep(1)

#It tells that there are much more things to learn.
driver.find_element_by_xpath("//h2[text()='Learn More']/ancestor::div[@class='joyride-content-wrapper']/descendant::a[@href='#']").click()
time.sleep(2)


#Click on the logo for getting on first page
elem_betabound_logo=driver.find_element_by_xpath("//a[@title='Betabound']")
#Select the type of beta test want to do
elem_beta_types=driver.find_element_by_xpath("//div[text()='Beta Types']").click()
#Select one type from the 'Beta Types' hover
elem_beta_web_app_beta=driver.find_element_by_xpath("//a[text()='Web App Betas']").click()
time.sleep(4)
#select first app for the test
elem_select_app=driver.find_element_by_xpath("//a[@href='https://jeevesbox.com/']")
elem_select_app.location_once_scrolled_into_view
elem_select_app.click()
str2=driver.current_window_handle
time.sleep(15)

driver.switch_to_window(str1)

#Things want to personalize
driver.find_element_by_xpath("//a[text()='Personalize']").click()
#Deselect all the elements to select particular
driver.find_element_by_xpath("//a[text()='Clear selections']").click()
time.sleep(2)
#Select 'Software'
driver.find_element_by_xpath("//input[@name='product_type']/ancestor::div[@class='icheckbox_flat']").click()
time.sleep(2)
#Submit it
driver.find_element_by_xpath("//input[@type='submit']").click()
#Close the driver
driver.close()
