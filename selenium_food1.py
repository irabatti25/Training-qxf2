#Import the webdriver
from selenium import webdriver
#Import time
import time
#Select Chrome webdriver
driver=webdriver.Chrome()
#Maximize the window
driver.maximize_window()
#Go to the Foodpanda website
driver.get('https://www.foodpanda.in/')
time.sleep(5)
#Find the web element 'Popular Cities'
#elem=driver.find_element_by_xpath("//select[@placeholder='Enter a city' and @data-prefill='location.cityId']/ancestor::div[@id='wrapper-element-1']")         
select_city=driver.find_element_by_xpath("//input[@class='form-control twitter-typeahead tt-input']")
time.sleep(2)
select_city.clear()
#Send the keys as "Bangalore" to the 'Popular Cities'
select_city.send_keys("Bangalore")
#Find the web element 'Find an area'
elem_area=driver.find_element_by_xpath("//input[@placeholder='Enter an area']")
#Send the keys as "Hoodi (ITPL Road Whitefield)" to the 'Find an area'
area=elem_area.send_keys("Hoodi (ITPL Road Whitefield)")
time.sleep(10)
#Click on the 'Show Restaurants'
elem_restaurants=driver.find_element_by_xpath("//button[@type='submit'][text()='Show restaurants']").click()
time.sleep(10)
#Select text of delivery time of any one restaurant from the resataurant list
#elem2=driver.find_element_by_xpath("//span[@data-tooltip-element='.delivery-time-tooltip-v6sk']").text
elem2=driver.find_element_by_xpath("//a[starts-with(@href, '/restaurant/') and @data-clicked_restaurant_position='1']/descendant::span[@class='minutes']").text
#print the selected text
print elem2
#Create a list to store the digits of text
elem2_d=[]
#For loop to extract the digits from the text
for i in elem2:
    #Condition to check whether the element in i of elem2 is digit ir not.
    if i.isdecimal():
        #If condition is true append to the list
        elem2_d.append(i)

print elem2_d
#Select text of delivery time of another one restaurant from the resataurant list
elem4=driver.find_element_by_xpath("//a[starts-with(@href, '/restaurant/') and @data-clicked_restaurant_position='4']/descendant::span[@class='minutes']").text
#elem3=driver.find_element_by_xpath("//span[@data-tooltip-element='.delivery-time-tooltip-m0an']").text
#print the selected text
print elem4
#Create a list to store the digits of text
elem3_d=[]
#For loop to extract the digits from the text
for i in elem4:
    #Condition to check whether the element in i of elem3 is digit ir not.
    if i.isdecimal():
        #If condition is true append to the list
        elem3_d.append(i)

print elem3_d

#Compare the delivery time of both the restaurants and select the one having less delivery time
if(elem2_d[0]<elem3_d[0]):
    elem2_se=driver.find_element_by_xpath("//a[starts-with(@href, '/restaurant/') and @data-clicked_restaurant_position='1']/descendant::span[@class='minutes']").click()
else:
    elem2_se1=driver.find_element_by_xpath("//a[starts-with(@href, '/restaurant/') and @data-clicked_restaurant_position='4']/descendant::span[@class='minutes']").click()

#Select one item from the menu of selected restaurant and place into 'Your order'
elem_select_soup=driver.find_element_by_xpath("//article[@data-clicked_product_id='5025052']/descendant::i[@class='icon icon-add icon-add-to-cart']")
elem_select_soup.location_once_scrolled_into_view
elem_select_soup.click()
time.sleep(5)
#Select another item from the menu of selected restaurant and place into 'Your order'
elem_r1=driver.find_element_by_xpath("//article[@data-clicked_product_id='5025145']/descendant::i[@class='icon icon-add icon-add-to-cart']")
elem_r1.location_once_scrolled_into_view
elem_r1.click()
time.sleep(5)
elem_rr1=driver.find_element_by_xpath("//label[@for='cart_product_skeleton_choices_145165_full_0']").click()
elem_rr2=driver.find_element_by_xpath("//button[text()='Continue']").click()
time.sleep(5)
#driver.close()
