link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_busket_present_on_page(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(
        "button.btn-add-to-basket").is_displayed(), \
        "Кнопка 'Добавить в корзину' отсутствует"
