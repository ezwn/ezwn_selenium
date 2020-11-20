from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # untested
import time

# Settings

max_try = 100

def page_loading_pause():
    time.sleep(0.5)

def dom_refresh_pause():
    time.sleep(0.25)

def page_loading_safe_pause():
    time.sleep(5)

def transaction_safe_pause():
    time.sleep(60 * 15)

# Code
class TooManyTries(Exception):
    pass

driver = None
actions = None # untested

def open_browser(headless = False):
    global driver
    global actions # untested

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless")  

    driver = webdriver.Chrome('./bin/chromedriver', options=options)
    driver.set_window_size(1024,900)
    page_loading_pause()

    actions=ActionChains(driver) # untested

def find_many(selector, min=1, max=None):
    global driver

    loops = 0
    while loops<max_try:
        time.sleep(0.1)
        try:
            elements = driver.find_elements_by_css_selector(selector)
            if (len(elements)>=min and (max==None or len(elements)<=max)):
                return elements
        except:
            pass

        loops = loops + 1

    raise TooManyTries()

def find_one(selector):
    return find_many(selector, max=1)[0]

def click(element): # untested
    actions.move_to_element(element).perform() # untested
    page_loading_safe_pause() # untested
    actions.click().perform() # untested

def refresh():
    global driver

    driver.refresh()
    page_loading_pause()

def get(url):
    global driver

    driver.get(url)
    page_loading_pause()

def close_browser():
    global driver

    driver.close()

def parseFloat(string):
    return float(string.replace("\xa0", "").replace(",", "."))
