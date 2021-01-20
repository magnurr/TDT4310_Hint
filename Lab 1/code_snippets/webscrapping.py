
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

# Parse the HTML in Bs4
soup = BeautifulSoup(content, features="html.parser")

# Find_all gives a list of all matching HTML documents (divs with class card-body)
tabs = soup.find_all('div', attrs={"class": "card-body"})

for tab in tabs:
    # They changed the webpage between me writting this script and the lecture....
    if (len(tab.select('p.card-text')) >= 1):
        # Find text inside tab by using a cssSelector
        #NBNB find_all and select do the same thing but in different ways :)
        text = tab.select('p.card-text')[0].get_text()
        print(text)

# Helps to quit the window after use.
driver.quit()
