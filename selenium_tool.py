from selenium import webdriver
import os
from random_word import RandomWords
import time 

r = RandomWords()
words = list()
words = r.get_random_words(maxLength=15, limit=2)
print('Random words: ', words)
composed_repository_name = 'orarepo'
for item in words:
    composed_repository_name = composed_repository_name + '-' + item
print('Composed repository name: ' + composed_repository_name)
# Convert to lowercasxe
composed_repository_name = composed_repository_name.lower()

driver = webdriver.Chrome('/home/jasper/Downloads/chromedriver_linux64/chromedriver')

driver.get('https://github.com')

# Redirect to sign in (github.com/login)
#sign_in_button = driver.find_element_by_xpath('/html/body/div/header/div/div/div/a[1]')
sign_in_button = driver.find_element_by_link_text('Sign in')

sign_in_button.click()

# Sign in 
username = driver.find_element_by_name('login')
password = driver.find_element_by_name('password')
sign_in_button = driver.find_element_by_name('commit')

username.send_keys(os.environ['GITHUB_USERNAME'])
password.send_keys(os.environ['GITHUB_PASSWORD'])
sign_in_button.click()

# Logged in
# Now, create a new repository
"""
new_button = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')
new_button.click()
"""

driver.get('https://github.com/new')
# Now, in github.com/new
repository_name = driver.find_element_by_name('repository[name]')
repository_description = driver.find_element_by_name('repository[description]')
repository_readme_init = driver.find_element_by_id('repository_auto_init')

repository_name.send_keys(composed_repository_name)
repository_description.send_keys('%s, generated using Selenium automation by jasperan' % composed_repository_name)
repository_readme_init.click()

time.sleep(.5)

repository_create = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
repository_create.click()