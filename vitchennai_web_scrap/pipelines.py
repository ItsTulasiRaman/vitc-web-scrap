# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class VitchennaiWebScrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://ItsTulasiRaman:admin123@vitccweb.x8cotvw.mongodb.net/?retryWrites=true&w=majority")
        db = self.conn["vitccwebscrap"]
        self.collection = db["faculty_info"]
        if self.collection.count_documents({})!=0:
            self.collection.drop()
            self.__init__()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
