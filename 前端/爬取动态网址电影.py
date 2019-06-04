import requests
import time
with open('2.csv','a',encoding='utf-8') as f:
	for a in range(3):
		#取三组20*3=60个数据
		url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
		file = requests.get(url_visit).json()
		#之前我们用的 .text是需要网页返回文本的信息,而这里返回的是json文件所以用.json()
		time.sleep(2)
		for i in range(20):
			dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
			urlname=dict['url'] #取出URL
			title=dict['title'] #取出电影名称
			rate=dict['rate'] #取出评分
			cast=dict['casts'] #取出演职人员
			f.write('{},{},{},{}\n'.format(title,rate,'  '.join(cast),urlname))
			#’ '.join(cast)将每个演员都用空格分开
