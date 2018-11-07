import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TOR_BINARY_PATH = ""
TOR_PROFILE_PATH = ""

DRIVER = None

#open tor process
def openTor():
    try:
        print("STARTING TOR... %s" % time.ctime(time.time()))
        #time.sleep(5)
        os.system('START firefox')
        time.sleep(10)
        print("OPEN TOR ... %s" % time.ctime(time.time()))
    except Exception as e:
        print("%s " % str(e))

#close tor process
def closeTor():
    try:
        print("KILLING TOR PROCESS... %s" % time.ctime(time.time()))
        time.sleep(3)
        os.system('TASKKILL /F /IM firefox.exe')
        print("CLOSE TOR ... %s" % time.ctime(time.time()))

    except Exception as e:
        print("%s " % str(e))

#scrolling to any element
def viewelement(driver, element):
    driver.execute_script("arguments[0].scrollIntoView()", element)

#Vote in target.
def vote(pTags, driver, target):
    print("BEGINING VOTE... %s" % time.ctime(time.time()))
    for tags in pTags:
        if(tags.text == target):
            viewelement(driver, tags)
            print("FINDED TARGET")
            ActionChains(driver).move_to_element(tags)
            tags.click()

    btns = driver.find_elements_by_name("<CLASS_TO_FIND>")

    for btn in btns:
        if(btn.text == "<TEXT_BUTTON_TO_FIND>"):
            vote = False
            viewelement(driver, btn)
            print("FINDED BTN_ACTION")
            ActionChains(driver).move_to_element(btn)
            btn.click()

            try:
                vote = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, "<CLASS_NAME>")))
                print(vote)
                time.sleep(3)
            finally:
                return vote

#Verify wether especifics webelements is loaded on current page
def is_loaded(driver):
    print("STARTING VERIFY LOADED STATUS... %s" % time.ctime(time.time()))
    loaded = False
    try:
        loaded = WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.TAG_NAME, "<TAG_NAME>")))
    finally:
        print("FINISH VERIFY LOADED STATUS... %s" % time.ctime(time.time()))
        return loaded
#Get a list with webelements
def get_elements(driver):
    print("STARTING GET ELEMENTS... %s" % time.ctime(time.time()))
    return driver.find_elements_by_tag_name("<TAG_NAME>")


#Function that will be used by Thread
def bot_process(driver, target_name):
    control = False
    openTor();
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        print("LOADING THE PAGE ...")
        driver.get("<TARGET_URL>")
    except Exception as e:
        print("%s " % str(e))
        control = True
    if(not control):
        print("PAGE LOADED!")
        control = False
        while(not control):
            control = is_loaded(driver)
            if(control):
                print("ELEMENTS LOADED!")
            else:
                print("TRYING LOAD ELEMENTS...")
                driver.refresh()
        control = False
        try:
            elements = get_elements(driver)
            print("ELEMENTS NUMBERS: ", len(elements))
            print("VOTE... %s" % time.ctime(time.time()))
            if(vote(elements,driver,target_name)):
                control = True
        except Exception as e:
            print("%s " % str(e))
        driver.quit()
        closeTor()
        time.sleep(3)
        return control
    else:
        print("ERROR LOADING PAGE!")
        return False

#--------------------------------------------------------------------
DRIVER = None
votes = 0
voted = False

#Loop for the voting
for i in range(0, 1000):
    voted = bot_process(DRIVER, "<ELEMENT_VALUE_TO_VOTE>")
    if(voted):
        votes += 1
    voted = False
    print("Current Votes: %s" % votes)
    print("------------------------------------------------------")

print("All Votes: %s" % votes)
