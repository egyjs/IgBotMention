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


def Insta(username, password, url):
    driver = webdriver.Chrome()
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

    MENTION = 3  # how many users mention per rows
    ROWS = 5  # how many rows comments

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
	print '1'	
	sleep(12)

        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").click()

        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").send_keys(
            text)
        sleep(5)
        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Add a comment')]").send_keys(Keys.ENTER)
	driver.find_element_by_xpath("//button[@type='submit']").click()

    sleep(10)


auths = open('auth.txt', 'r')
for auth in auths:
    if auth and auth.strip():
        auth = auth.split('\t')
        username = auth[0].strip()
        password = auth[1].strip()
        print username, password

        urls = open('urls.txt', 'r')
        for url in urls:
            if url and url.strip():
                print url
                Insta(username, password, url.strip())
