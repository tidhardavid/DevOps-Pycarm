from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Tidhar Ben David
#Assignment 5 -

print('Assignment 5:')


def rundriver (browser, link, cta = None):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\\Users\Tidhar\Downloads\chromedriver_win32\chromedriver.exe')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\Users\Tidhar\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe')
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path='C:\\Users\Tidhar\Downloads\MicrosoftWebDriver.exe')

    driver.implicitly_wait(10)

    driver.get(link)

    result = None

    if callable(cta):
            result = cta(driver)

    driver.close()
    driver.quit()

    if result is not None:
        return result

######################################
#1
def main1():
    print('1.')
    rundriver('chrome', 'https://www.walla.co.il/')
    rundriver('firefox', 'https://www.ynet.co.il')

#2
def main2():
    print('2.')
    rundriver('chrome', 'https://www.walla.co.il/', fun2)
    rundriver('firefox', 'https://www.ynet.co.il', fun2)

def fun2(driver):
    browser = driver.name.capitalize()

    title1 = driver.title
    print(browser+' page title 1: ', title1)
    driver.refresh()
    title2 = driver.title
    print(browser+' page title 2: ', title2)

    if title1 == title2:
        print('both titles are the same after refreshing!!')
    else:
        print('both titles aren\'t the same!')

#3. both browsers return the same element, as they open the same page, and if the selectors are pointing to the same element, they will return the same element.
def main3():
    print('3.')
    ele1 = rundriver('chrome', 'https://www.google.co.il/', fun3)
    ele2 = rundriver('firefox', 'https://www.google.co.il', fun3)

    print(ele1)
    print(ele2)


def fun3(driver):
    return driver.find_elements_by_css_selector('#lst-ib')[0].tag_name


#4.
def main4():
    print('4.')
    global translatetext
    translatetext = 'שלום עולם'
    translation = rundriver('chrome', 'http://translate.google.co.il', fun4)
    print('translation:', translation)


def fun4(driver):
    global translatetext
    hebrewbutton = driver.find_element_by_id('sugg-item-iw')
    hebrewbutton.click()

    textarea = driver.find_element_by_id('source')
    textarea.send_keys(translatetext)

    translate = driver.find_element_by_id('gt-submit')
    translate.click()

    result = ''
    while len(result) == 0:
        result = driver.find_element_by_id('gt-res-dir-ctr').text
    return result


#5.
def main5():
    print('5.')
    rundriver('chrome', 'https://www.youtube.com/', fun5)


def fun5(driver):
    search = driver.find_element_by_id('search')
    search.send_keys('sorry justin beiber')
    search.send_keys(Keys.ENTER)

#6.
def main6():
    print('6.')
    rundriver('firefox', 'https://translate.google.com', fun6)

def fun6(driver):
    search1 = driver.find_element_by_id('gt-submit')
    print(search1)

    search2 = driver.find_element_by_css_selector('#gt-submit')
    print(search2)

    search3 = driver.find_element_by_xpath('//*[@id="gt-submit"]')
    print(search3)



7.
from fb import fb
def main7():
    print('7.')
    rundriver('firefox', 'https://www.facebook.com/', fun7)

def fun7(driver):
    email = driver.find_element_by_css_selector('#email')
    pwd = driver.find_element_by_css_selector('#pass')
    signin = driver.find_element_by_css_selector('input[type=submit][aria-label="Log In"]')

    email.send_keys(fb['email'])
    pwd.send_keys(fb['pwd'])
    signin.click()


#challenges
8.
def main8():
    print('8.')
    rundriver('chrome', 'https://www.google.co.il/', fun8)

def fun8a(driver):
    cookies = driver.get_cookies()
    if len(cookies) > 0:
        for cookie in driver.get_cookies():
            print (cookie['name'], ': ', cookie['value'], '\n')
    else:
        print('No cookies here ;-)')

def fun8(driver):
    fun8a(driver)
    driver.delete_all_cookies()
    print('Cookies Have been deleted\n')
    fun8a(driver)


#9.
def main9():
    print('9.')
    rundriver('chrome', 'https://github.com/', fun9)

def fun9(driver):
    search = driver.find_element_by_css_selector('[placeholder="Search GitHub"]')
    if not search.is_displayed():
        hamburger = driver.find_element_by_css_selector('button[aria-label="Toggle navigation"]')
        hamburger.click()

    search.send_keys('selenium')
    search.send_keys(Keys.ENTER)


#10.
def main10():
    print('10.')
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions");
    driver = webdriver.Chrome(executable_path='C:\\Users\Tidhar\Downloads\chromedriver_win32\chromedriver.exe', options = options)

    # options2 = webdriver.FirefoxOptions
    # options2.add_argument("--disable-extensions")
    # driver2 = webdriver.Firefox(executable_path='C:\\Users\Tidhar\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe', options = options2)

    # options3 = webdriver.IeOptions.add_argument("--disable-extensions")
    # driver3 = rundriver('edge', 'https://www.google.co.il/', webdriver.Edge(executable_path='C:\\Users\Tidhar\Downloads\MicrosoftWebDriver.exe'))

if __name__ == '__main__':
    exec('main'+str(input('enter question number:'))+'()')
