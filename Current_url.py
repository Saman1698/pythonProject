from selenium import webdriver

class Current_Url():
    def Url(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)

        crnt_url = driver.current_url
        print("Current url of the page is:" + crnt_url)



link = Current_Url()
link.Url()













