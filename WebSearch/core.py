from selenium import webdriver


class WebSearch(object):

    def __init__(self, driverPath="./chromedriver", headless=False):
        self.driverPath = driverPath
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
            self.options.add_argument("--window-size=1280x1696")

    def open(self):
        self.driver = webdriver.Chrome(
            self.driverPath, chrome_options=self.options)

    def close(self):
        self.driver.quit()

    def search(self, query):
        pass
