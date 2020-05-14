from selenium import webdriver
from time import sleep

class LikeBot:
  def __init__(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://instagram.com")
    sleep(2)

LikeBot()