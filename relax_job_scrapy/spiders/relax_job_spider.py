import scrapy
from bs4 import BeautifulSoup
from relax_job_scrapy.items import RelaxJobScrapyItem

class RelaxJobSpider(scrapy.Spider):
    name = 'relax_job_spider'
    allowed_domains = ['relax-job.com']
    start_urls = [
        'https://relax-job.com/search?business_type=biyoshi&sort=recommended',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        salon_list = soup.find_all('li', class_='js-shops-accordion__item')
        for salon in salon_list:
            yield scrapy.Request(salon.find('a').get('href'), self.parse_salon_page)
        
        # 次ページへ
        pagination = soup.find_all('li', class_='c-pagenation__item')
        last_pagination = pagination[len(pagination) - 1]
        next_link = last_pagination.find('a', rel='Next')
        if next_link is not None:
            yield scrapy.Request(response.urljoin(next_link.get('href')), callback=self.parse)

    def parse_salon_page(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        item = RelaxJobScrapyItem()
        item['求人ページurl'] = response.url
        
        #dt_list = soup.find('dl', class_='p-job-table').find_all('dt')
        #for dt in dt_list:
        #    if dt.find('span').get_text() == '職種 / 役職':
        #        item['職種_役職'] = dt.next_element.findNext('dd').find('p').get_text()
        #    elif dt.find('span').get_text() == '給与':
        #        item['給与'] = dt.next_element.findNext('dd').find('p').get_text()

        item_list = soup.find('div', class_='p-job-table p-job-table--tab-content').find_all('div', class_='p-job-table__left')
        for itm in item_list:
            #if itm.get_text() == '給与' and not '給与備考' in item:
            #    item['給与備考'] = itm.findNext('div').get_text().strip()
            if itm.get_text() == '住所' and not '住所' in item:
                item['住所'] = itm.findNext('div').get_text().strip()
            elif itm.get_text() == '店舗名・勤務地' and not 'アクセス' in item:
                access_list = itm.findNext('div').get_text().strip().splitlines()
                item['サロン名'] = access_list[0].replace('・', '').strip()
                item['アクセス'] = access_list[len(access_list) - 1].replace('（', '').replace('）', '').strip()
            #elif itm.get_text() == '勤務時間' and not '勤務時間' in item:
            #    item['勤務時間'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '特徴' and not '特徴' in item:
            #    feature = []
            #    for li in itm.findNext('div').find_all('li'):
            #        feature.append(li.get_text())
            #    item['特徴'] = '/'.join(feature)
            #elif itm.get_text() == '仕事内容' and not '仕事内容' in item:
            #    item['仕事内容'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '必要経験' and not '必要経験' in item:
            #    item['必要経験'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '必要資格' and not '必要資格' in item:
            #    item['必要資格'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '休日' and not '休日' in item:
            #    item['休日'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '福利厚生' and not '福利厚生' in item:
            #    item['福利厚生'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '求める人物像':
            #    item['求める人物像'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '役職の詳細':
            #    item['役職の詳細'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == '私たちの夢・想い':
            #    item['私たちの夢_想い'] = itm.findNext('div').get_text().strip()
            #elif itm.get_text() == 'PR':
            #    item['PR'] = itm.findNext('div').get_text().strip()

        yield item
