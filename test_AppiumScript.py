import allure
from appium import webdriver

desired_capabilities = {
    "platformName": "iOS",
    "platformVersion": "14.5",
    "deviceName": "iPhone 8 Plus",
    "app": "/Users/nikolaipetrov/Library/Developer/Xcode/DerivedData/Calculator-gufvwxekmdbtayatmfysxecpfjiw/Build/Products/Debug-iphonesimulator/Calculator.app"
}

@allure.title('Calc')
#@allure.severity(Severity.BLOCKER)

def test_case01():
    with allure.step('Check value "0,"'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
    #with allure.step('Check value "0,"'):
    with allure.step('Enter number "9" 9'):
        driver.find_element_by_name('9').click()
    with allure.step('Tap on the  "СA" button'):
        driver.find_element_by_name('AC').click()
    with allure.step('"0," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 0



def test_case02():
    with allure.step('Check sum'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on plus button'):
        driver.find_element_by_name('+').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"4," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 4

def test_case03():
    with allure.step('Check minus'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on minus button'):
        driver.find_element_by_name('-').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"0," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 0

def test_case04():
    with allure.step('Check multiply'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on multiply button'):
        driver.find_element_by_name('x').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"4," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 4

def test_case05():
    with allure.step('Check division'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on multiply button'):
        driver.find_element_by_name('/').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"1," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 1

def test_case05():
    with allure.step('Check negative number'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on minus button'):
        driver.find_element_by_name('-').click()
    with allure.step('Tap on number "3" 3'):
        driver.find_element_by_name('3').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"1," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == -1

def test_case06():
    with allure.step('Check fractional number'):
        driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capabilities)
        driver.find_element_by_name('AC').click()
    with allure.step('Tap on number "5" 5'):
        driver.find_element_by_name('5').click()
    with allure.step('Tap on minus button'):
        driver.find_element_by_name('/').click()
    with allure.step('Tap on number "2" 2'):
        driver.find_element_by_name('2').click()
    with allure.step('Tap on equally button'):
        driver.find_element_by_name('=').click()
    with allure.step('"2.5," displayed in the field'):
        numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
        assert int(numbers_field.text) == 2.5
