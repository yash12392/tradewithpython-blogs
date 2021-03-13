from selenium.common.exceptions import StaleElementReferenceException
import time, glob, os
import undetected_chromedriver as uc
from os.path import join

def download_corp_action(driver, action_type):
    '''
    The main function which launches uses the undetected_chromedriver's driver to click on the BSE corp action page.
    Params:
        driver = uc.Chrome() [should be defined in the main function, see corporate_actions() to understand more]
        action_type = str: ['dividend', 'split', 'bonus']
    '''

    #Purpose keys on BSE website
    purpose_dict = {"Bonus" : "P5", "Dividend" : "P9", "StockSplit" : "P26"}

    #Exception and Error Handling
    if not driver:
        raise ValueError("ChromeDriver needs to be provided to download data.")

    if not action_type:
        raise ValueError("You need to mention the corp action type, allowable fields ['dividend', 'split', 'bonus']")

    if not isinstance(action_type, str):
        raise ValueError("action_type arguement needs to be a str.")

    action_type =  action_type.lower()

    if action_type not in ['dividend', 'split', 'bonus']:
        raise ValueError("Incorrect Corporate Action Input, allowable fields ['dividend', 'split', 'bonus']")
    
    #Finding the purpose box on page and clicking it.
    purpose = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlPurpose"]')

    purpose.click()

    #Deciding which corporate action to download data on
    if action_type == 'dividend':
        corp_act = purpose_dict['Dividend']
    elif action_type == 'split':
        corp_act = purpose_dict['StockSplit']
    else:
        corp_act = purpose_dict['Bonus']

    #Selecting the relevant corporate action with some error handling as BSE website active executes Javascript to change itself.
    selected_purpose = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlPurpose"]/option[@value=\"{corp_act}\"]')

    try:
        selected_purpose.click()
    except StaleElementReferenceException:
        selected_purpose = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlPurpose"]/option[@value=\"{corp_act}\"]')
        selected_purpose.click()

    #Finally submit the request and intentionally waiting for 5 mins. 
    submit = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSubmit"]')
    submit.click()

    time.sleep(5)

    #Downloading the .CSV File from the website for relevant corporate action. 
    download_csv = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload1"]/img')

    try:
        download_csv.click()
    except StaleElementReferenceException:
        download_csv = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload1"]/img')
        download_csv.click()


def get_latest_file(path):
    '''
    A simple func to get the latest Corporate Actions files in the defined path.
    Params:
        path: should be default download path
    
    Returns:
        The full path of latest file downloaded.

    '''

    list_of_files = glob.glob(f'{path}/Corporate_Actions*.csv')
    try:
        latest_file = max(list_of_files, key = os.path.getctime)
    except ValueError:
        time.sleep(10)
        try:
            latest_file = max(list_of_files, key = os.path.getctime)
        except ValueError:
            raise ValueError("Sorry, we are not able to download data from BSE website.")

    return latest_file

def rename_latest_file(filepath, newfilepath):
    '''
    A simple func to rename the latest file as all data from BSE website comes in 
    Corporate_Actions.csv name, so this function will rename those files to avoid confusion.
    Params:
        filepath: get_latest_file(path)
        newfilepath: the new name of the file you want like ['dividend.csv', 'split.csv', 'bonus.csv']
    '''
    try:
        os.rename(filepath,newfilepath)
    except FileExistsError:
        os.remove(newfilepath)
        os.rename(filepath, newfilepath)
    except FileNotFoundError:
        raise ValueError("Sorry, we are not able to download data from BSE website.")

def corporate_actions():
    '''
    The wrapper function which utilizes all other functions and utilizes them to download files.

    NOTE: I have noticed the best time to download the file is from 10AM - 5PM, after that BSE
    Website starts getting unresponsive and the code is unable to download .csv files because of no 
    response from BSE. Please keep that in mind while scheduling scrips and see what works best for you.
    '''
    bse_corp_path = 'https://www.bseindia.com/corporates/corporate_act.aspx'

    default_downloads_path = join('C:', os.sep, 'Users', os.getlogin(), 'Downloads')

    driver = uc.Chrome()
    driver.get(bse_corp_path)
    download_corp_action(driver, 'dividend')
    time.sleep(15)
    latest_file = get_latest_file(default_downloads_path)
    rename_latest_file(latest_file, f'{default_downloads_path}/dividend.csv')
    
    download_corp_action(driver, 'split')
    time.sleep(5)
    latest_file = get_latest_file(default_downloads_path)
    rename_latest_file(latest_file, f'{default_downloads_path}/split.csv')
    
    download_corp_action(driver, 'bonus')
    time.sleep(5)
    latest_file = get_latest_file(default_downloads_path)
    rename_latest_file(latest_file, f'{default_downloads_path}/bonus.csv')
    
    driver.close()

if __name__ == "__main__":

    corporate_actions()

