from selenium import webdriver

import datetime
import random
import time
import os

#Tidhar Ben David
#Buy Me Automation -


def getLink():
    link = None

    try:
        linkFile = open('C:\\Users\Tidhar\PycharmProjects\BuyMeAutomation\BuyMeLink.txt', 'r', encoding='utf-8')
        link = linkFile.read().strip()
        linkFile.close()
    except IOError:
        print('File error!!')

    return link


def runAutomation():
    print('Buy Me Automation is running...')

    link = getLink()

    if link is not None:
        rundriver(link)
    else:
        print('Link from txt file wasn\'t found :-(')


def rundriver(link):

    driver = webdriver.Chrome(executable_path='C:\\Users\Tidhar\Downloads\chromedriver_win32\chromedriver.exe')

    driver.implicitly_wait(30)

    driver.get(link)

    email = ('test'+datetime.datetime.now().strftime("%f")+'t@tester.com')

    runRegistrationScreen(driver, email)

    time.sleep(2)

    runHomeScreen(driver)

    time.sleep(2)

    runBuisnessScreen(driver)

    time.sleep(2)

    runRecieverScreen(driver, email)

    time.sleep(5)

    driver.close()
    driver.quit()

    print('\nBuy Me Automation is done successfully!!')


def runRegistrationScreen(driver, emailaddres):
    enterregister = driver.find_element_by_css_selector('.my-account>a, .nav-bar li:nth-child(3) a')
    enterregister.click()

    notregisteredyet = driver.find_element_by_css_selector('#auth-modal .header-link, .switch-text .text-btn')
    notregisteredyet.click()

    firstname = driver.find_element_by_css_selector('[placeholder="שם פרטי"]')
    firstname.send_keys('Moshe')

    email = driver.find_element_by_css_selector('[placeholder="מייל"]')
    email.send_keys(emailaddres)

    pwd = driver.find_element_by_css_selector('[placeholder="סיסמה"]')
    pwd.send_keys('Ab123456')

    pwd2 = driver.find_element_by_css_selector('[placeholder="אימות סיסמה"]')
    pwd2.send_keys('Ab123456')

    registerconsent = driver.find_elements_by_css_selector('label[for="register-consent"], .oldschool form .fa-check')[0]
    registerconsent.click()

    register = driver.find_element_by_css_selector('#register-block button[type="submit"], .oldschool form button[type="submit"]')
    register.click()


def runHomeScreen(driver):
    selects = driver.find_elements_by_css_selector('.main-header-search .chosen-container, .header-search-bar .chosen-container')
    for select in selects:
        select.click()
        options = select.find_elements_by_css_selector('.active-result')
        index = random.randint(1, len(options) - 1)
        options[index].click()

    searchgift = driver.find_element_by_css_selector('.main-header-search button[type="submit"], .header-search-bar a[href*="/search"]')
    searchgift.click()

    time.sleep(2)

    #in case we get no results - we rerun this function
    if driver.execute_script('var a; return ((a = document.querySelector("h1.page-title")) && /לא נמצאו תוצאות מתאימות/i.test(a.textContent))'):
        runHomeScreen(driver)


def runBuisnessScreen(driver):
    buisnesses = driver.find_elements_by_css_selector('a[href*="/supplier/"]')
    index = random.randint(0, (len(buisnesses) - 1))
    buisnesses[index].click()

    time.sleep(2)

    #checking if we have a gift card option, if not choosing one of the options
    isGiftcard = driver.execute_script('return !!document.querySelector(".cash-giftcard")')
    if isGiftcard:
        amount = driver.find_element_by_css_selector('.money input[placeholder="מה הסכום?"]')
        amount.send_keys('200')

        send = driver.find_element_by_css_selector('.cash-giftcard button[type="submit"]')
        send.click()
    else:
        gifts = driver.find_elements_by_css_selector('a.card-wrapper')
        index = random.randint(0, (len(gifts) - 1))
        gifts[index].click()


def runRecieverScreen(driver, email):
    tosomeoneelse = driver.find_element_by_css_selector('label[data="forSomeone"]')
    tosomeoneelse.click()

    recievername = driver.find_element_by_css_selector('input[data-parsley-required-message*="שם המקבל"]')
    recievername.send_keys('Haim')

    sendername = driver.find_element_by_css_selector('input[data-parsley-required-message*="השם שלך"]')
    sendername.clear()
    sendername.send_keys('Moshe')

    events = driver.find_element_by_css_selector('.step-form .ui-card .chosen-container')
    events.click()
    options = events.find_elements_by_css_selector('.active-result')
    index = random.randint(1, len(options) - 1)
    options[index].click()

    greeting = driver.find_element_by_css_selector('textarea[placeholder*="כאן כותבים מילים טובות"]')
    greeting.clear()
    greeting.send_keys('מזל טוב לקורס devOps!!!!')

    pictureupload = driver.find_element_by_css_selector('.media-fields input[name="fileUpload"]')

    #image file should be in the same folder as this main.py file, so it will be uploaded from any computer
    pictureupload.send_keys(os.path.abspath('Devops_Experts_final_logo-1-300x120.jpg'))

    sendnow = driver.find_element_by_css_selector('label.send-now')
    sendnow.click()

    bymail = driver.find_elements_by_css_selector('.send-methods .btn-send-option')[1]
    bymail.click()

    mailinput = driver.find_element_by_css_selector('input.input-mail')
    mailinput.send_keys(email)

    save = driver.find_element_by_css_selector('.form-well button[type = "submit"]')
    save.click()

    submit = driver.find_element_by_css_selector('.submit-wrapper button[type = "submit"]')
    submit.click()


if __name__ == '__main__':
    runAutomation()