from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from lxml import etree
import time

input_element = "/html/body/div[1]/div[1]/div[3]/div/div[1]/div/main/div[2]/nav/div/div[2]/div/div/div[1]/section/div/div[2]/div[1]/section/div/div[1]/d-textarea/div[1]"
output_element= "/html/body/div[1]/div[1]/div[3]/div/div[1]/div/main/div[2]/nav/div/div[2]/div/div/div[1]/section/div/div[2]/div[3]/section/div[1]/d-textarea"
                
class Scraper():
    def __init__(self, text, headless=False):
        print("Scraper initializing")
        # self.headers = None
        self.options = Options()
        if headless: self.options.add_argument("-headless")
        self.url = "https://www.deepl.com/translator#ru/en/" + text
        self.driver = None
        self.start()

    def start(self):
        print("Scraper tries to open a page")
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get(self.url)
        time.sleep(5)

    # TO:DO - wait untill message appears, if not - return "Cant get translation"
    def get_translation(self):
        # Open page on start and open new tab instead
        output = self.driver.find_element_by_xpath(output_element)
        text = []
        for element in output.find_elements_by_tag_name("p"):
            text.append(element.text)
        self.quit()
        print("Scraper got translation - ", text)
        return text

    # Not used
    def get_by_xpath(self, xpath):
        try:
            html = self.driver.page_source
            soup = bs(html, "lxml")
            dom = etree.HTML(str(soup))
            result = dom.xpath(f'{xpath}')[0].text
            return result
        except Exception as e:
            return f'Error: {e}'

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    result = Scraper("привет, как твои дела?", headless=True).get_translation()
    print(result)