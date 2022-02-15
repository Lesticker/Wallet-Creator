from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Settings import *


def Createwallet():
    

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : r'C:\Python\SolletWalletCreator\Download'}
    chrome_options.add_experimental_option('prefs', prefs)
    s = Service(r"C:\Users\Dawid\.wdm\drivers\chromedriver\win32\97.0.4692.71\chromedriver.exe")
    driver = webdriver.Chrome(service=s , chrome_options=chrome_options)
    #Open sollet.io website
    driver.get('https://sollet.io')

    #Clicking OK button
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[3]/button[2]/span[1]').click()

    #Getting Seed phtase from box
    seedbox = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div/div/textarea[1]')
    seedcontent = seedbox.get_attribute('innerHTML')


    #Writing seed phrase to file
    f = open("wallets.txt", "a")
    f.write(seedcontent)
    f.write(" , ")
    print (seedcontent)

    #clicking checkbox
    driver.find_element(By.CLASS_NAME, 'jss12').click()

    #clicking on download backup mnemonic
    driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/p[5]/button/span[1]').click()

    #clicking CONTINUE button
    driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[2]/button/span[1]').click()

    #Writing seed code to inputbox
    inputSeed = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/p/div[2]/div/input")
    inputSeed.send_keys(seedcontent)

    #confirm by clicking Ok  
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[2]/button[2]/span[1]').click()

    #entering new password 
    Newpassword = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div[1]/div/input')
    Newpassword.send_keys(walletpassword)

    #confirm passoword
    confirmPassword = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div[2]/div/input')
    confirmPassword.send_keys(walletpassword)

    #Clicking create wallet button //*[@id="root"]/main/div/div/div[2]/button[2]/span[1]
    driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[2]/button[2]/span[1]').click()

    #time.sleep(5)

    # Wait for page to load and get wallet address
    addressBox = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div/div/div/div/ul/div/div[2]/div[1]/p/div/div')))
    addressContent = addressBox.get_attribute('innerHTML')
    #write wallet address to file
    f = open("wallets.txt", "a")
    f.write(addressContent)
    f.write("\n")
    print (addressContent)
    

for _ in range(howmanywallets):
    Createwallet()
