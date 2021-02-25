# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

# 数据保存方式一
# class QsbkSpiderPipeline:
#
#     def __init__(self):
#         self.fp = open('data.json', 'w', encoding='UTF-8')
#
#     def open_spider(self, spider):
#         print('爬虫启动...')
#
#     def process_item(self, item, spider):
#         # json.dump(item, fp=self.fp, indent=4, ensure_ascii=False)
#         json.dump(dict(item), fp=self.fp, indent=4, ensure_ascii=False)
#         return item
#
#     def close_spider(self, spider):
#         print('爬虫结束...')

# 数据保存方式二
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter


class QsbkSpiderPipeline:

    def __init__(self):
        self.fp = open('data.json', 'wb')
        # self.exporter = JsonItemExporter(file=self.fp, ensure_ascii=False, encoding='UTF-8', indent=4)
        # self.exporter.start_exporting()
        self.exporter = JsonLinesItemExporter(file=self.fp, ensure_ascii=False, encoding='UTF-8', indent=4)

    def open_spider(self, spider):
        print('爬虫启动...')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        print('爬虫结束...')
