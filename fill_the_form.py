from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
chrome = "https://docs.google.com/forms/d/e/1FAIpQLSfRau6WhhgJ28pRUzAeMHSDTT3RYOYVJoTg0zuEMMqs1iEPBw/viewform?usp=sf_link"


class SELENIUM:
    def __init__(self):
        self.chrome_path = r"C:\Users\haodi\Desktop\TransferData\Data Science course\Python Course " \
                           r"practice\DAY48\DAY48 PROJECT\chromedriver_win32\chromedriver.exe "
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.get(chrome)

    def form_input(self,x_path,content):
        time.sleep(3)
        input_box = self.driver.find_element(By.XPATH,x_path)
        input_box.send_keys(content)


    def send_form(self):
        send_button = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        send_button.click()
        time.sleep(2)

    def back_to_form(self):
        back_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        back_button.click()
        time.sleep(2)
    def quit(self):
        self.driver.quit()