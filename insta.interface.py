#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random
import json
# 12s + 5 = 17 
# 17 * int(ROWS)
with open('config.json') as json_data_file:
    config = json.load(json_data_file)



def Insta(username, password, url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless");



    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://www.instagram.com/accounts/login/")

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for page to load"
    sleep(1)
    try:
        driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    except:
        pass
    sleep(5)
    driver.get(url)

    MENTION = config['MENTION']  # how many users mention per rows
    ROWS = config['ROWS']  # how many rows comments

    mentions = open("lists/600-list-angham.txt").readlines()
    for x in range(ROWS):
        text = ''
        for y in range(MENTION):
            user = ' @' + random.choice(mentions)
            if user and user.strip():
                text = text + (user.rstrip("\n\r"))

        try:
            element_present = EC.presence_of_element_located(
                (By.XPATH, "//textarea[contains(@aria-label,'Add a comment')]"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print "Timed out waiting for page to load"
	sleep(12)

	print (x+1)	
        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").click()

        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").send_keys(
            text)
        sleep(5)
        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").send_keys(Keys.ENTER)
	driver.find_element_by_xpath("//button[@type='submit']").click()

    sleep(10)


for auth in config['auth']:
    username = auth['user']
    password = auth['pass']
    print username, password

    
    for url in config['urls']:
        if url and url.strip():
            print url
            Insta(username, password, url.strip())
