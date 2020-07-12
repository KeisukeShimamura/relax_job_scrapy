# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RelaxJobScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    サロン名 = scrapy.Field()
    職種_役職 = scrapy.Field()
    給与 = scrapy.Field()
    給与備考 = scrapy.Field()
    住所 = scrapy.Field()
    アクセス = scrapy.Field()
    勤務時間 = scrapy.Field()
    特徴 = scrapy.Field()
    仕事内容 = scrapy.Field()
    必要経験 = scrapy.Field()
    必要資格 = scrapy.Field()
    休日 = scrapy.Field()
    福利厚生 = scrapy.Field()
    求める人物像 = scrapy.Field()
    役職の詳細 = scrapy.Field()
    企業の夢_想い = scrapy.Field()
    PR = scrapy.Field()
    企業名 = scrapy.Field()
    求人ページurl = scrapy.Field()
