[TOC]
# Requesets库

## 基本使用
1. **requests.get()**:以GET方式请求一个网页。通过GET方法得到一个Response对象，然后分别输出Response的类型，Status Code，Response Body的类型，内容还有Cookies。   

2. **requests.post()/requests.put()/requests.delete()/requests.head()/requests.options()**.---分别用post()、put()、delete()等方法实现了POST、PUT、DELETE等请求。   

2. **params**:附加额外信息内容   
```python
data = {
    'name' : 'germey',
    'age' : 22
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)
```    
4. **抓取图片、视频文件、音频方法：**
```python
import requests

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
```    
在这里用了 open() 方法，第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向文件里写入二进制数据，然后保存。

***

## 高级用法
1. **Cookies** 
使用Cookiesu来维持登陆，示例如下：   
```python
import requests

headers = {
    'Cookie': '填写Cookies',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
```

2. ==**Session**==
会话维持,示例如下：
```python
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
```   
3. **verify**
控制是否检查此证书，默认为True。
```python
import requests

response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
```    
4. **proxies**   
 代理设置。 示例如下：  
```python
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('https://www.taobao.com', proxies=proxies)
```   
若代理需要使用HTTP Basic Auth，可以使用类似http://user:password@host:port 这样的语法来设置代理。示例如下：
```python
import request

proxies = {
    'http' : 'http://user:password@10.10.1.10:3128/',
}
requests.get('https://www.taobao.com',proxies=proxies)
```    
Requests还支持SOCKS协议代理，示例如下：    
首先需要安装Socks库，命令如下：
```python
pip3 install 'requests[socks]'
```    
然后就可以使用SOCKS协议代理了，实例如下：
```python
import requests

proxies = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port',
}
requests.get('https://www.taobao.com',proxies=proxies)
```   
5. **timeout**
设置超时时间，即超过了这个时间还没有得到响应，就报错。示例如下：
```python
import requests

r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)
```    
6.**身份认证**    
遇到需要身份验证的网站，可以使用Requests自带的身份认证功能，实例如下：    
```python
import requests
r = requests.get('https//localhost:5000',auth = ('username','password'))
print(r.status_code)
```    
*OAuth认证*
```python
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
```   
详情查看官方网站[ Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/)
     
## 正则表达式
模式 | 描述
--- | ---
\w  | 匹配字母数字及下划线
\W  | 匹配非字母数字及下划线
\s  | 匹配任意空白字符，等价于[\t\n\r\f]
\S  | 匹配任意非空字符
\d  | 匹配任意数字，等价于[0-9]
\D  | 匹配任意非数字
\A	| 匹配字符串开始
\Z	| 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
\z	| 匹配字符串结束
\G	| 匹配最后匹配完成的位置
\n	| 匹配一个换行符
\t	| 匹配一个制表符
^	| 匹配字符串的开头
$	| 匹配字符串的末尾
.	| 匹配任意字符，除了换行符，当 re.DOTALL 标记被指定时，则可以匹配包括换行符的任意字符
[...] | 用来表示一组字符，单独列出：[amk] 匹配 'a'，'m' 或 'k'
[^...] | 不在 [] 中的字符：abc 匹配除了 a,b,c 之外的字符。
*	| 匹配 0 个或多个的表达式。
+	| 匹配 1 个或多个的表达式。
?	| 匹配 0 个或 1 个由前面的正则表达式定义的片段，非贪婪方式
{n}	| 精确匹配 n 个前面表达式。
{n, m}	| 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
`a	b`	| 匹配 a 或 b
( )	 |匹配括号内的表达式，也表示一个组
1. **match()**
match()方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果，否则，返回None。实例如下：
```python
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
```    
2. **匹配目标**   
如果想从字符串中提取一部分内容可使用()括号来将想提取的子字符串括起来，()实际上就是标记了一个子表达式的开始和结束位置，被标记的每个子表达式会依次对应每个分组，可以调用group()方法传入分组的索引即可获取提取的结果。示例如下：
```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
```     
2. **通用匹配**     
刚才我们写的正则表达式其实比较复杂，出现空白字符我们就写 \s 匹配空白字符，出现数字我们就写 \d 匹配数字，工作量非常大，其实完全没必要这么做，还有一个万能匹配可以用，也就是 .* （点星），.（点）可以匹配任意字符（除换行符），（星） 又代表匹配前面的字符无限次，所以它们组合在一起就可以匹配任意的字符了，有了它我们就不用挨个字符地匹配了。全部用 .* 来代替，最后加一个结尾字符串就好了示例如下：    
```python
import re 
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
```     
3. **贪婪与非贪婪**    
这里就涉及一个贪婪匹配与非贪婪匹配的原因了，贪婪匹配下，.* 会匹配尽可能多的字符，我们的正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，所以 .* 就尽可能匹配多的字符，所以它把 123456 也匹配了，给 \d+ 留下一个可满足条件的数字 7，所以 \d+ 得到的内容就只有数字 7 了。   
但这样很明显会给我们的匹配带来很大的不便，有时候匹配结果会莫名其妙少了一部分内容。其实这里我们只需要使用非贪婪匹配匹配就好了，非贪婪匹配的写法是 .*?，多了一个 ?，那么它可以达到怎样的效果？我们再用一个实例感受一下：    
```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
```     
字符串中间我们可以尽量使用非贪婪匹配来匹配，也就是用 .*? 来代替 .*，以免出现匹配结果缺失的情况,注意，如果匹配的结果在字符串结尾，.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符。     

4. **修饰符：re.S**    
 . 匹配的是除换行符之外的任意字符，当遇到换行符时，.*? 就不能匹配了，导致匹配失败。只需要加一个修饰符re.S,u即可。示例：
 ```python
 result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
 ```     
 修饰符 | 描述 
 ----  | ----
 re.I  | 使匹配对大小写不敏感
 re.L  | 做本地化识别(locale-aware)匹配
 re.M  | 多行匹配，影响^ 和 $
 re.S  | 使.匹配包括换行在内的所有字符
 re.U  | 根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B
 re.X  | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解     

 5. **转义匹配**     
 正则匹配模式的特殊字符时，我们在前面加反斜线来转义一下就可以匹配了。例如 . 我们就可以用 \\. 来匹配

6. **search()**
search()方法会在匹配时扫描整个字符串，然后返回第一个成功匹配的结果，也就是说，正则表达式可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None。示例如下：
```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
```    
7. **findall()**    
findall()方法会搜索整个字符串然后返回匹配正则表达式的所有内容。    
8. **sub()**    
正则表达式除了提取信息，我们有时候还需要借助于它来修改文本，比如我们想要把一串文本中的所有数字都去掉，如果我们只用字符串的 replace() 方法那就太繁琐了，在这里我们就可以借助于 sub() 方法。示例如下：     
```python
import re
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)
```    
9. **compile()**     
前面我们所讲的方法都是用来处理字符串的方法，最后再介绍一个 compile() 方法，这个方法可以讲正则字符串编译成正则表达式对象，以便于在后面的匹配中复用。示例如下：  
```python
import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
```     
例如这里有三个日期，我们想分别将三个日期中的时间去掉，所以在这里我们可以借助于 sub() 方法，sub() 方法的第一个参数是正则表达式，但是这里我们没有必要重复写三个同样的正则表达式，所以可以借助于 compile() 方法将正则表达式编译成一个正则表达式对象，以便复用。另外 compile() 还可以传入修饰符，例如 re.S 等修饰符，这样在 search()、findall() 等方法中就不需要额外传了。