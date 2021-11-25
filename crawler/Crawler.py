from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.url = ''

    def _set_url(self, url):
        self.url = url

    def _crawl(self, url):
        pass