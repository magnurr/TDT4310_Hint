
# Selenium is a potentially headless-browser for test automation.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Bs4 is a framework for traversing, wrangling and working with HTML
from bs4 import BeautifulSoup

# Get the browser you want to use
driver = webdriver.Chrome(ChromeDriverManager().install())
# How to call is driver.{METHODE}([URL]) | POST, PUT, GET etc
driver.get('https://www.ntnu.edu/')

# Pulling the raw HTML from the webpage
content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# Soup.find([TAG],attrs=[Attributes as dict]) finds the first matching html element
tab = soup.find('div', attrs={"class": "card-body"})
# find_all gives a list of all matching HTML documents
tabs = soup.find_all('div', attrs={"class": "card-body"})

print(tab)

print(tabs)

# Helps to quit the window after use.
driver.quit()
