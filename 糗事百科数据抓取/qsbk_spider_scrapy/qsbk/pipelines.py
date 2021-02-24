# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

# 数据存储方式一
# class QsbkPipeline:
#
#     def __init__(self):
#         self.fp = open('data.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫启动...')
#
#     def process_item(self, item, spider):
#         # print(item)
#         # self.fp.write(json.dumps(item, ensure_ascii=False))
#         # json.dump(item, fp=self.fp, indent=4, ensure_ascii=False)
#         json.dump(dict(item), fp=self.fp, indent=4, ensure_ascii=False)
#         return item
#
#     def close_spider(self, spider):
#         print('爬虫结束...')
#         self.fp.close()


# 数据存储方式二
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter
class QsbkPipeline:

    def __init__(self):
        self.fp = open('data.json', 'wb')
        # self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        # self.exporter.start_exporting()
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫启动...')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print('爬虫结束...')
        # self.exporter.finish_exporting()
        self.fp.close()
