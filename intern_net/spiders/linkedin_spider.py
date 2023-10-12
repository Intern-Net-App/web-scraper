import os
import scrapy
from dotenv import load_dotenv
from intern_net.items import LinkedInJob

load_dotenv()
class LinkedInSpider(scrapy.Spider):
  name = "linkedin_spider"
  target_url = os.getenv("TARGET_URL")

  
  def start_requests(self):
    first_job_on_page = 0
    first_url = self.target_url + str(first_job_on_page)
    yield scrapy.Request(
      url=first_url, 
      callback=self.parse_job, 
      meta={
        'first_job_on_page': first_job_on_page
        }
      )
    
  def parse_job(self, response):
    first_job_on_page = response.meta['first_job_on_page']
    
    job_item = LinkedInJob()
    jobs = response.css("li")
    
    num_jobs_returned = len(jobs)
    print(num_jobs_returned)
    
    for job in jobs:
      job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
      job_item['job_detail_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
      job_item['job_listed'] = job.css('time::text').get(default='not-found').strip()

      job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
      job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
      job_item['company_location'] = job.css('.job-search-card__location::text').get(default='not-found').strip()
      yield job_item
      
    # if num_jobs_returned > 0:
    #     first_job_on_page = int(first_job_on_page) + 25
    #     next_url = self.target_url + str(first_job_on_page)
    #     yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})