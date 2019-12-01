import pyautogui
import random
import string
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Site web et param
url = 'https://www.ladepeche.fr'  #
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.prettify())
