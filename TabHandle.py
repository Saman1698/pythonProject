from selenium import webdriver
import time

class Tab_handle():
    def tab(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe ")
        url = "https://accounts.google.com/signup"       # parent window
        driver.maximize_window()
        driver.get(url)  # hit the url
        print("You hit the url")

        # open next tab
        driver.find_element_by_xpath("//a[normalize-space()='Privacy']").click()
        time.sleep(2)
        print("Clicked on privacy...!")

        driver.current_window_handle      # handle current window

        handles = driver.window_handles
        for h in handles:
            driver.switch_to.window(h)
            print(driver.title)

        driver.find_element_by_xpath("//a[@class='bCzwPe YySNWc']").click()
        time.sleep(2)
        print("Click was performed...!!")


ht = Tab_handle()
ht.tab()












