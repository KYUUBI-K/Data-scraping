# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from module.items import ModuleItem
from sqlite3 import connect
class ModulePipeline:
    def process_item(self, item, spider):
        return item

class SaveToDbPipline:
    def open_spider(self, spider):
        self.connection = connect("ekatalog.db")
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ModuleItem):
            self.cursor.execute(
                "INSERT INTO photoaparat (model, model_url,  start_price,end_price, img_url) VALUES (?,?,?,?,?)",
                [item["model"], item["model_url"], item["start_price"],
                    item["end_price"], item["img_url"]]
            )
            self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()