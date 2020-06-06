import time
from urllib.parse import urlparse
import cssutils
from webdrivermanager.webdrivermanager import ChromeDriverManager
from selenium import webdriver


class BaseScrapper:

    def __init__(self,url="",soup=None):
        self.page_url = url
        self.scrap = soup
        self.site_domain = self.get_domain(self.page_url)

    def get_domain(self,url):
        parsed_uri = urlparse(url)
        return parsed_uri.netloc

    def get_all_links(self):
        return [l['href'] for l in self.scrap.find_all('a',href=True)]

    def get_all_domain_links(self):
        return [l['href'] for l in self.get_all_links()
                if l['href'].contains(self.site_domain)]

    def get_all_background_images(self,element_list=[]):
        all_img = []
        # self.scrap.find_all() ---All tags
        for el in element_list:
            if el.has_attr('style'):
                all_img.append(self.get_background_image())

    def get_background_image(self,el):
        el_style = cssutils.parseStyle(el['style'])
        if el_style['background-image']:
            return el_style['background-image']
        else:
            return None

    def get_all_images(self):
        return [image['src'] for image in
                self.scrap.find_all('img',src=True)] + \
               self.get_all_background_images(self.scrap.find_all())

    def get_next_siblings(self,el):
        return el.find_next_siblings()

    def get_all_children(self, el):
        return el.children

    def scroll_to_bottom_of_page(self, driver):

        SCROLL_PAUSE_TIME = 20

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                return driver
            last_height = new_height

    def get_driver(self, url):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().download_and_install()[0],
                                  chrome_options = options)
        # driver = webdriver.Chrome(executable_path='C:\\Users\\shash\\PycharmProjects\\ScrapMe\\venv\\' +
        #                                           'WebDriverManager\\chrome\\81.0.4044.69\\chromedriver_win32\\'+
        #                                           'chromedriver.exe',chrome_options= options)
        driver.get(url)

        return driver