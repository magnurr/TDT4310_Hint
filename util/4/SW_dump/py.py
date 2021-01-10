from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())

BaseURL = "https://www.imsdb.com/scripts/Star-Wars-The-Empire-Strikes-Back.html"

CSSselector = "pre"

driver.get(BaseURL)
text_source = driver.find_element_by_css_selector(CSSselector)

with open('dump.html', "w") as file:
    file.write(text_source.get_attribute('innerHTML'))
driver.quit()
