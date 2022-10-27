from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pyotp


def login_in_zerodha(api_key, api_secret, user_id, user_pwd, totp_key):
    driver = uc.Chrome()
    driver.get(f'https://kite.trade/connect/login?api_key={api_key}&v=3')
    login_id = WebDriverWait(driver, 10).until(
        lambda x: x.find_element(by=By.XPATH, value='//*[@id="userid"]'))
    login_id.send_keys(user_id)

    pwd = WebDriverWait(driver, 10).until(
        lambda x: x.find_element(by=By.XPATH, value='//*[@id="password"]'))
    pwd.send_keys(user_pwd)

    submit = WebDriverWait(driver, 10).until(lambda x: x.find_element(
        by=By.XPATH,
        value='//*[@id="container"]/div/div/div[2]/form/div[4]/button'))
    submit.click()

    time.sleep(1)

    totp = WebDriverWait(driver, 10).until(lambda x: x.find_element(
        by=By.XPATH,
        value='//*[@id="container"]/div/div/div[2]/form/div[2]/input'))
    authkey = pyotp.TOTP(totp_key)
    totp.send_keys(authkey.now())

    continue_btn = WebDriverWait(driver, 10).until(lambda x: x.find_element(
        by=By.XPATH,
        value='//*[@id="container"]/div/div/div[2]/form/div[3]/button'))
    continue_btn.click()

    time.sleep(5)

    url = driver.current_url
    initial_token = url.split('request_token=')[1]
    request_token = initial_token.split('&')[0]

    driver.close()

    kite = KiteConnect(api_key=api_key)
    #print(request_token)
    data = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(data['access_token'])

    return kite


if __name__ == '__main__':

    kiteobj = login_in_zerodha('ZERODHA_API_KEY', 'ZERODHA_API_SECRET',
                               'ZERODHA_USER_ID', 'ZERODHA_USER_PWD',
                               'ZERODHA_TOTP_KEY')

    print(kiteobj.profile())
