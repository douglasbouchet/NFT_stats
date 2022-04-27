#from urllib.request import urlopen
#from bs4 import BeautifulSoup

#url = "https://magiceden.io/stats"
#html = urlopen(url).read()
#soup = BeautifulSoup(html, features="lxml")
#
# print(soup.prettify())

# for script in soup(["script", "style"]):
#    script.decompose()
#
#strips = list(soup.stripped_strings)
# print(strips[:5])


#from urllib.request import Request, urlopen
#
#req = Request('https://www.yahoo.com', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()
#soup = BeautifulSoup(webpage, features="lxml")
# print(soup.prettify())


#url = "https://magiceden.io/stats"
#html = urlopen(url).read()
#soup = BeautifulSoup(html, features="lxml")
# req = Request('https://magiceden.io/stats',
#              headers={'User-Agent': 'Mozilla/5.0'})
#html = urlopen(req).read()
#soup = BeautifulSoup(html, features="lxml")
#
# print(soup.prettify())
# print(soup)

#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://magiceden.io/stats")
time.sleep(10)
# res = driver.find_element_by_xpath(
#    "/html/body/div[2]/div/div/div/div[3]/div[2]/section/div/div/div[3]/div/div/table/tbody/tr[1]")
# res = driver.find_element_by_xpath(
#    "/html/body/div[2]/div/div/div/div[3]/div[2]/section/div/div/div[3]/div/div/table/tbody/tr[1]/td[7]")
# res = driver.find_element_by_xpath(
res = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div/div[3]/div[2]/section/div/div/div[3]/div/div/table/tbody/tr[2]/td[6]/span")


print("res = ", res.text)

res = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div/div[3]/div[2]/section/div/div/div[3]/div/div/table/tbody/tr[3]/td[6]/span")
print("res = ", res.text)

res = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div/div[3]/div[2]/section/div/div/div[3]/div/div/table/tbody/tr[6]/td[6]/span")
print("res = ", res.text)


# driver.close()

