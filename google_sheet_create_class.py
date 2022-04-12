from selenium import webdriver
from selenium.webdriver.common.by import By
import time
Chrome_driver = "../chromedriver.exe"

class GoogleSheet:
    def __init__(self, name_list, price_list, link_list):
        self.name_list = name_list
        self.price_list = price_list
        self.link_list = link_list

    def create_sheet(self):
        browser = webdriver.Chrome(executable_path=Chrome_driver)
        browser.get(url='https://docs.google.com/forms/d/e/1FAIpQLSdI_u_i9b1D9sHG_-nkBKtI2csOFiqJK8nzz4D_qT9sDyW2rA/viewform?usp=sf_link')
        browser.maximize_window()

        time.sleep(2)
        for i in range(len(self.name_list)):
            send_name = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            send_name.send_keys(self.name_list[i])

            send_name = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            send_name.send_keys(self.price_list[i])

            send_name = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            send_name.send_keys(self.link_list[i])

            submit_key = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_key.click()

            another_response = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()

            time.sleep(2)

        browser.quit()
