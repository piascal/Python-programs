from selenium import webdriver
import random

browser = webdriver.Chrome()
browser.get('https://bandcamp.com/')
tracks = browser.find_element_by_class_name('playbutton')
tracks.click()
