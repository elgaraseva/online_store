import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_verify_button_add_to_basket(browser):
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(30)
    buttonAddToBasket = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')

    assert buttonAddToBasket, "Button \"Add to busket\" not found"