# -*- coding: utf-8 -*-

import time

# http://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# open the web browser
driver = webdriver.Chrome()
driver.get('http://www.python.org')

# wait
time.sleep(4)

# select the pypi button
elem = driver.find_element_by_class_name('pypi-meta')
elem.click()

# wait
time.sleep(4)

# select the search element
elem = driver.find_element_by_id('search')

# type in the input text field
elem.send_keys('sphinx')

# hit enter
elem.send_keys(Keys.RETURN)

time.sleep(10)


elem = driver.find_element_by_xpath("//p[contains(text(),'Python documentation generator')]")
elem.click()

elem = driver.find_element_by_tag_name('time')
print(f'Last release for Sphinx is: {elem.text}')

# go back
driver.back()

time.sleep(2)

# go back again
driver.back()

# wait
time.sleep(2)

# close the browser
driver.close()
