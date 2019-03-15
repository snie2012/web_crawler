import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JobInfoSpider(scrapy.Spider):
    name = "job_info"

    def start_requests(self):
        url = 'https://sou.zhaopin.com/?p={}&jl=489'

        for i in range(1, 13):
            request = SeleniumRequest(
                url=url.format(i),
                callback=self.parse,
                wait_time=3000,
                wait_until=EC.visibility_of_element_located((By.CSS_SELECTOR, '.contentpile__content__wrapper__item__info__box__jobname__title'))
            )

            request.meta['page_number'] = i

            yield request

    def parse(self, response):
        filename = 'page_number_{}.html'.format(response.meta['page_number'])
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)