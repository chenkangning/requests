import  requests
from lxml import etree
import time

with open('p250.txt','a',encoding='utf-8') as f:
	for a in range(10):
		url = 'https://book.douban.com/top250?start={}'.format(a*25)
		reopense = requests.get(url).text
		rel = etree.HTML(reopense)
		laa = rel.xpath('//*[@id="content"]/div/div[1]/div/table')
		for info in laa:
			title = info.xpath('./tr/td[2]/div[1]/a/@title')[0]
			href = info.xpath("./tr/td[2]/div[1]/a/@href")[0]
			score = info.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
			commitmentNum = info.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
			scribe = info.xpath('./tr/td[2]/p[2]/span/text()')
			if len(scribe) > 0:
				f.write('{},{},{},{},{}'.format(title,href,score,commitmentNum,scribe[0]))
				# print(time.sleep(1))
			else:
				f.write('{},{},{},{}'.format(title,href,score,commitmentNum))
				# print(time.sleep(1))
