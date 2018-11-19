import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\Tidhar\Downloads\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://translate.google.co.il/?hl=iw&tab=wT')

print('page URL: ', driver.current_url)
print('page title: ', driver.title)
# print(driver.page_source)

ids = driver.find_elements_by_css_selector('[id]')
for i in range(len(ids)):
    print(driver.execute_script('var ele = arguments[0]; return ele.id', ids[i]))
    driver.execute_script('var a = arguments[0] + arguments[1]; console.log(a); ', 'a', 5)
    if(ids[i].get_attribute('id') == 'source'):
        ids[i].send_keys('hello')

driver.execute_script('window.alert("hello!!!")')
# labels = driver.find_elements_by_tag_name("label")
# inputs = driver.execute_script(
#     "var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" +
#     "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)
#


time.sleep(10)
driver.close()
driver.quit()