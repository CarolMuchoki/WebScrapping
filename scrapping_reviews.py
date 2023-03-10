from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(30)
location = '600028'
print('Search By')
print('1.Book shops')
print('2.Food')
print('3. Temples')
print('4. Exit')
ch = 'Y'

while ch.upper() == 'Y':
    choice = input('Enter choice (1/2/3/4):')
    query = ()
    if choice == '1':
        query = 'book shops near' + location
    if choice == '2':
        query = 'food near' + location
    if choice == '3':
        query = 'temples near' + location
    driver.get('https://www.google.com/search?q=' + query)
    wait= WebDriverWait(driver, 10)
    ActionChains(driver).move_to_element(wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains (@href, '/search?tbs')]")))).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, "a[contains (@href, '/search?tbs')]"))).click()
    names = []

    for name in driver.find_elements(By.XPATH, "//div[@aria-level= '3']"):
        names.append(name.text)
    print(names)
    ch = input('Do you want to continue (Y/N):')

