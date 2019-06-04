import requests
import re                                        #正则
import json                                      #字节转字符串
import time                                      #推迟线程执行的秒数（防止速度过快无响应）
from requests.exceptions import RequestException #捕抓requestsu异常
def get_one_page(url):
	try:
		response = requests.get(url)            #获取网址
		if response.status_code == 200:         #检查状态码
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile(                   #正则表达式
		'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"'
		+'.*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'
		+'.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>'
		+'.*?fraction.*?>(.*?)</i>.*?</dd>',
		re.S)
	items = re.findall(pattern, html)       #提取所有内容（元组）
	# return items
	for item in items:                      #遍历结果生成字典
		yield {
			'排名': item[0],
			'图片': item[1],
			'电影名': item[2].strip(),
			'主演': item[3].strip()[3:] ,
			'上映日期': item[4].strip()[5:] ,
			'评分': item[5].strip() + item[6].strip()
		}
# [3:]剪切

# 这里直接写入一个文本文件中。这里通过JSON库的dumps()方法
# 实现字典的序列化，并指定ensure_ascii参数为False,这样就可以保证输
# 出结果是中文形式而不是Unicode编码。
def write_to_json(content):
	with open('result.txt','a',encoding='UTF-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False,)+'\n')


#接收一个offset值作为偏侈量，然后构造UPL进行爬取，实现如下：
def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset)
	html = get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_json(item)


#传入参数，遍历多页网页
if __name__ == '__main__':
	for i in range(10):
		main(offset=i * 10)
		time.sleep(1)