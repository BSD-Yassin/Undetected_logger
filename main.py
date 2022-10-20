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
# options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)

driver.get('https://www.crunchbase.com/login/')

login_PATH = "/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/div[2]/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[1]/div/div[1]/div/input"
password_PATH = "/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/div[2]/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[2]/div/div[1]/div/input"
button_login = "/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/div[2]/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/button"

driver.find_element(By.XPATH, login_PATH).send_keys("#PutyourUsernamehere")
driver.find_element(By.XPATH, password_PATH).send_keys("#PutyourPasswordhere")
driver.find_element(By.XPATH,button_login).click()

# This only serves to keep the window open, otherwise Selenium will block it
time.sleep(60)