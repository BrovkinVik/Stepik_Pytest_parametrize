import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_busket_button_shown_in_all_languages(browser):
	browser.get(link)
	time.sleep(10)
	button = browser.find_element_by_css_selector("button.btn-add-to-basket")
	assert button, "button not found"