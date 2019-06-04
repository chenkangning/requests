import requests
from lxml import etree
import pprint

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',

	'Refer' : 'https://douban.com/'
}
urls = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
response = requests.get(url=urls,headers=HEADERS)
text = response.text
html = etree.HTML(text)
a = html.xpath('//ul[@class = "lists"]')[0]
b = a.xpath('./li')
movie = []
for lis in b:
	title = lis.xpath('@data-title')[0]
	score = lis.xpath('@data-score')[0]
	release = lis.xpath('@data-release')[0]
	duration = lis.xpath('@data-duration')[0]
	region = lis.xpath('@data-region')[0]
	director = lis.xpath('@data-director')[0]
	actors = lis.xpath('@data-actors')[0]
	img = lis.xpath('//img/@src')[0]

	movies = {
		'电影名':title,
		'评分':score,
		'上映时间':release,
		'时长':duration,
		'上映地点':region,
		'导演':director,
		'主演':actors,
		'海报':img
	}
	movie.append(movies)
pprint.pprint(movie)
with open('正在上映的电影.text','a',encoding='utf-8') as f:
	for a in movie:
		f.write('电影名：' + a['电影名'] + '\n')
		f.write('评分：' + a['评分'] + '\n')
		f.write('上映时间：' + a['上映时间'] + '\n')
		f.write('时长：' + a['时长'] + '\n')
		f.write('上映地点：' + a['上映地点'] + '\n')
		f.write('导演：' + a['导演'] + '\n')
		f.write('主演：' + a['主演'] + '\n')
		f.write('海报：' + a['海报'] + '\n' + '\n')