import scrapy
from ..items import VitchennaiWebScrapItem

class EmailspiderSpider(scrapy.Spider):
    name = "emailSpider"
    allowed_domains = ["chennai.vit.ac.in"]
    start_urls = ["https://chennai.vit.ac.in/member/page/1/"]
    email_seperator = "@vit.ac.in"
    navigation_count = 1

    def parse(self, response):

        items = VitchennaiWebScrapItem()

        all_faculty = response.css("div.col-md-4")
        for faculty in all_faculty:
            fac_name = faculty.css('.item-title .main-color-1-hover::text').extract()
            position = faculty.css('h4.small-text::text').extract()
            content = str(faculty.css('p::text').extract())
            try:
                try:
                    try:
                        if self.email_seperator in content:
                            email = content.split(self.email_seperator, 1)[0] + self.email_seperator
                            email = email.split(":", 1)[1].strip()
                        else:
                            email = "Not available"
                    except IndexError:
                        email = content.split(self.email_seperator, 1)[0] + self.email_seperator
                        email = email.lower().split("email", 1)[1].strip()
                except IndexError:
                    email = email.lower().split("-", 1)[1].strip()
            except:
                email = "Unknown error"

            items["faculty_name"] = fac_name
            items["position"] = position
            items["email"] = email
            yield items


        next_page = response.css("div.wp-pagenavi a.nextpostslink::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            self.navigation_count += 1
            print("Next page navigated " + str(self.navigation_count))

#Web server command- install "scrapyrt" and run this "http://localhost:9080/crawl.json?start_requests=true&spider_name=emailSpider"
#Note: The output file name should always be in "crawl.json","crawl.csv"... format.
