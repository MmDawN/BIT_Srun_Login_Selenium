from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

def login_func(username,password):
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
    driver.get("http://10.0.0.55")

    username = driver.find_element_by_id("username")
    username.send_keys(username)

    password = driver.find_element_by_id("password")
    password.send_keys(password)

    login = driver.find_element_by_id("login")
    login.click()

def is_connect_internet(testip):
    status = os.system(u"ping {} -c 8".format(testip))
    return status == 0

if __name__=="__main__":
    checkinterval = 10 #ping间隔
    testip = "114.114.114.114" 
    timestamp = lambda : print(time.asctime(time.localtime(time.time())))

    while 1:
        time.sleep(checkinterval)
        if not is_connect_internet(testip):
            timestamp()
            try:
                login_func("username","password") #填入自己的统一身份认证帐号与密码
            except Exception:
                pass