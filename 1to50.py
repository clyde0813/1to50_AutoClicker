from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
import requests
import os, time

options = webdriver.ChromeOptions()
options.add_argument(
    'User-Agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://zzzscore.com/1to50/"
while True:
    driver.get(url)
    
    for i in range(1, 51):
        print(i)
        for j in range(1, 26):
            if str(i) == driver.find_element(By.XPATH, '//*[@id="grid"]/div['+str(j)+']').text:
                driver.find_element(By.XPATH, '//*[@id="grid"]/div['+str(j)+']').click()
                break
            else:
                pass
    time.sleep(3)