# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os.path

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from DataRecorder import Recorder

class DeepproPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item