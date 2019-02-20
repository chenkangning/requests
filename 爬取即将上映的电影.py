import requests
from lxml import etree
import pprint

HEADERS = {
	'User-gent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
	'Refer':'https://douban.com'
}

urls = 'https://movie.douban.com/cinema/later/shenzhen/'
response = requests.get(url=urls,headers=HEADERS)
text = response.text

a = etree.HTML(text)
z = a.xpath('//*[@id="showing-soon"]')[0]
k = z.xpath('./div')
n =[]
for i in k:
	titles = i.xpath('./div/h3/a/text()')[0]
	time = i.xpath('./div/ul/li[1]/text()')[0]
	types = i.xpath('./div/ul/li[2]/text()')[0]
	state = i.xpath('./div/ul/li[3]/text()')[0]
	kays = i.xpath('./div/ul/li[4]/span/text()')[0]
	imgs = i.xpath('./a/img/@src')[0]

	ing = {
		'电影名':titles,
		'上映日期':time,
		'类型':types,
		'制片国家':state,
		'想看':kays,
		'海报':imgs
	}
	n.append(ing)
pprint.pprint(n)

with open('即将上映的电影.csv','a',encoding='utf-8') as f:
	for c in n:
		f.write('电影名：' + c['电影名'] + '\n')
		f.write('上映日期：' + c['上映日期'] + '\n')
		f.write('类型：' + c['类型'] + '\n')
		f.write('制片国家：' + c['制片国家'] + '\n')
		f.write('想看：'+ c['想看'] + '\n')
		f.write('海报：' + c['海报'] + '\n' + '\n')