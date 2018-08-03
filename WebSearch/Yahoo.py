from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from WebSearch import WebSearch


class Yahoo(WebSearch):

    def search(self, query):
        self.driver.get("https://www.yahoo.co.jp")
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        if soup.find(id="srchtxt") is not None:
            self.driver.find_element(By.ID, "srchtxt").send_keys(query)
            self.driver.find_element(By.ID, "srchbtn").click()
        else:
            self.driver.find_element(By.ID, "p").send_keys(query)
            self.driver.find_element(By.NAME, "search").click()

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        h3s = soup.find_all("h3")
        result = {}
        for i, h3 in enumerate(h3s):
            d = {}
            d["title"] = h3.find("a").text
            d["url"] = h3.find("a").get("href")
            result[i] = d
        return result
