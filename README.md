# 1to50_AutoClicker
## 1to50 순발력 테스트 웹 게임 Auto Clicker
#### 똥손인 당신도 페이커급 반응속도를 체험해보세요!     
#### If you're clumsy, experience Faker-class reaction speed!
![GIF](1to50.gif)

* https://zzzscore.com/1to50/
* Selenium
* Python

# How To Use
1. pip install selenium
2. pip install webdriver_manager
3. install Chrome Web Browser

# Code
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
```
