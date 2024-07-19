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

        star_rating = adapter.get('rating')
        star_rating = star_rating[0]
        split_star_val = star_rating.split(' ')
        if split_star_val[1] == 'Zero':
            adapter['rating'] = 0
        elif split_star_val[1] == 'One':
            adapter['rating'] = 1
        elif split_star_val[1] == 'Two':
            adapter['rating'] = 2
        elif split_star_val[1] == 'Three':
            adapter['rating'] = 3 
        elif split_star_val[1] == 'Four':
            adapter['rating'] = 4
        elif split_star_val[1] == 'Five':
            adapter['rating'] = 5
        return item
    
