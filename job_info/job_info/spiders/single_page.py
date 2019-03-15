import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pickle

class SinglePageSpider(scrapy.Spider):
    name = "single_page"

    def start_requests(self):
        with open('job_page_links/all_links.pickle', 'rb') as f:
            urls = pickle.load(f)

        for url in urls:
            request = SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

            yield request

    def parse(self, response):
        filename = 'job_page_htmls/' + response.url.split('/')[-1].split('.')[0] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)