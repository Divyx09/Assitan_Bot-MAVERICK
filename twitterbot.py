from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import  Options
import time

def account_info():
    with open('account_info.txt','r') as f:
        info =f.read().split()
        email = info[0]
        password =info[1]
    return email,password

email,password = account_info()

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome()

driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")