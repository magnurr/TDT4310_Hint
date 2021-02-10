
# Selenium is a program for test automation.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Bs4 is a framework for traversing, wrangling and working with HTML
from bs4 import BeautifulSoup
import os

dumpMade = os.path("reddit.html")

if not dumpMade:
    # Get the browser you want to use
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # How to call is driver.{METHODE} | POST, PUT, GET etc
    driver.get('https://old.reddit.com/')
    # Pulling the raw HTML from the webpage
    content = driver.page_source
    driver.quit()
    with open('reddit.html', "w+") as file:
        file.write(content)
else:
    with open('reddit.html') as file:
        content = file.read()

# Input the HTML to Bs4
soup = BeautifulSoup(content, features="html.parser")
# Find the first tab
tab = soup.find('div', attrs={"id": "siteTable"})


for entry in tab.find_all('div', attrs={"data-score": True}):
    # Ads
    if entry['data-score'] == "0":
        break
    score = entry['data-score']
    title = entry.find('a', attrs={"class": 'title'}).get_text()
    subreddit = entry['data-subreddit']
    timeHtml = entry.find('time')
    time = 'No time' if timeHtml == None else timeHtml.get_text()
    print(
        f"The post {title} from subreddit {subreddit} has a score of {score} and was posted at {time}")
