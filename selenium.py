from selenium import webdriver

driver = webdriver.Chrome('E:\\Downloads\\chromedriver_win32.exe')

driver.get('https://github.com')

# Login
sign_in_button = driver.find_element_by_xpath('/html/body/div/header/div/div/div/a[1]')

sign_in_button.click()

