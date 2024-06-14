# Task 1
# Task: Build a Web Scraper
# Develop a web scraper that extracts specific data from websites using libraries like BeautifulSoup or Scrapy. This task will improve their knowledge of web scraping techniques and handling HTML/XML data.

# Importing the required libraries (requests and Scrapy)
import requests
import scrapy
from scrapy.crawler import CrawlerProcess

# Creating a Spider class to scrape data from a website
class WebScraper(scrapy.Spider):
        name = 'web_scraper'
        # Defining the start URL
        start_urls = ['https://www.google.com']
        # Parsing the response
        def parse(self, response):
                # Extracting specific data from the page
                data = response.css('p::text').extract()
                # Displaying the extracted data
                for paragraph in data:
                        print(paragraph)

# Creating a CrawlerProcess object
process = CrawlerProcess()
# Running the spider
process.crawl(WebScraper)
process.start()