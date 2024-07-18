# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # extracting the no of items avilable instead of whole string
        val = adapter.get('availability')
        val = val[0]
        split_val = val.split('(')
        if len(split_val) < 2:
            adapter['availability'] = 0
        else:
            num_val = split_val[1].split(' ')
            adapter['availability'] = int(num_val[0])
        return item
    
