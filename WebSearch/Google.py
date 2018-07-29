from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from WebSearch import WebSearch


class Google(WebSearch):

    def search(self, key):
        self.driver.get("https://www.google.co.jp")
        el = self.driver.find_element(By.NAME, "q")
        el.send_keys(key)
        el.send_keys(Keys.ENTER)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        rcs = soup.find_all("div", class_="rc")
        result = {}
        for i, rc in enumerate(rcs):
            d = {}
            d["title"] = rc.find("a").text
            d["url"] = rc.find("a").get("href")
            result[i] = d
        return result
