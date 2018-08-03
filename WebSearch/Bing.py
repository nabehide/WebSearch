from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from WebSearch import WebSearch


class Bing(WebSearch):

    def search(self, query):
        self.driver.get("https://www.bing.com")
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        self.driver.find_element(By.ID, "sb_form_q").send_keys(query)
        self.driver.find_element(By.ID, "sb_form_go").click()

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        lis = soup.find_all("li", class_="b_algo")
        result = {}
        for i, li in enumerate(lis):
            d = {}
            d["title"] = li.find("a").text
            d["url"] = li.find("a").get("href")
            result[i] = d
        return result
