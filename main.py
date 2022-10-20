import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = uc.ChromeOptions()
agent = "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
options.add_argument('--enable-javascript')
options.add_argument("--disable-extensions")
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)

driver.get('https://www.crunchbase.com/login/')

# This only serves to keep the window open, otherwise Selenium will block it
time.sleep(60)