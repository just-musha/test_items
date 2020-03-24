link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_busket_present_on_page(browser):
    browser.get(link)
    buttonFound = True
    try:
        button = browser.find_element_by_css_selector("button.btn-add-to-basket44")
    except:
        buttonFound = False
    assert buttonFound == True
