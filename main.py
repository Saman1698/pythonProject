from selenium import webdriver


driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")

driver.get("https://www.google.com/")

print(driver.title)

print("done")




