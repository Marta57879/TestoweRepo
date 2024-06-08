from selenium import webdriver

def test_pageload():
    driver = webdriver.Chrome()
    driver.get("http://seleniumdemo.com/")
    driver.implicitly_wait(10)

    try:

        driver.get("http://seleniumdemo.com/")

        print("Udało się odpalić stronkę: ", driver.title)

        assert "Selenium Demo Page – Selenium Demo Page" in driver.title, "Title does not contain 'bb'"

    finally:
        driver.close()











