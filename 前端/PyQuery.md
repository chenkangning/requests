# PyQuery的使用
## 初始化
* 字符串初始化
```python
from pyquery import PyQuery as pq           #引入PyQuery对象，取别名pq
doc = pq(html)                              #声明的HTML字符串当作参数传递给PyQuery，就成功完成了初始化
print(doc('li'))                            #初始化的对象传入CSS选择器，传入li节点，就会选择所有li节点，打印输出li节点的HTML文本。
```

* URL初始化
```python
from pyquery import PyQuery as pq            
doc = pq(url='http://cuiqingcai.com')        #传入网页的URL，指定参数为url，相当于pq(requests.get('http://cuiqingcai.com').text)
print(doc('title'))
```

* 文件初始化
```python
from pyquery import PyQuery as pq
doc = pq(filename='demo.html')                #传递本地的文件名，参数指定filename即可
print(doc('li'))
```


## 基本CSS选择器
```python
from pyquery import PyQuery as pq
doc = pq(html)                                 #初始化PyQuery对象
print(doc('#container .list li'))              #传入CSS选择器，意思为选取id为container内部的class为list内部的所有li节点
print(type(doc('#container .list li')))        #打印类型输岀
```


## 查找节点
* 子节点
查找子节点需要用到find()方法，传入的参数是CSS选择器,示例如下：
```HTML
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
```
```python
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')          #解析class为list的节点
print(type(items))            #打印类型
print(items)                  #输出items
lis = items.find('li')        #调用find方法，传入CSS选择器，选取其内部li节点
print(type(lis))               #打印类型
print(lis)                     #输出lis
```

find()的查扰找范围是节点的所有子孙节点，如果只想查找子节点，可以用children()方法：
```python
lis = items.children()
print(type(lis))
print(lis)
```

要筛选所有子节点中符合条件的节点，比如筛选出子节点中class为active的节点，可以向children()方法传入CSS选择器.active:
```python
lis = items.children('.active')
print(lis)
```

* 父节点
用parent()方法来获取某个节点的父节点
```python
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)
```

用parents()方法获取祖先节点
```python
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)                  #parents()会返回所有祖先节点
print(parents('.wrap'))         #如果要筛选某个祖先节点的话在parents中传入css选择器即可
```

* 兄弟节点
用siblings()方法获取兄弟节点
```python
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active') #选择class为list的节点内部的class为item-0和active的节点
print(li.siblings())             
```
筛选某个兄弟节点，可以向方法传入CSS选择器，这样就会在所有兄弟节点中挑选岀符合条件的节点
```python
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings('.active'))      #筛选class为active的节点
```


## 遍历
对于多个节点的结果，我们就需要遍历来获取，需要调用items()方法
```python
from pyquery import PyQuery as pq
doc = pq(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))
```
在这里我们可以发现调用 items() 方法后，会得到一个生成器，遍历一下，就可以逐个得到 li 节点对象了，它的类型也是 PyQuery 类型，所以每个 li 节点还可以调用前面所说的方法进行选择，比如继续查询子节点，寻找某个祖先节点等等，非常灵活。


## 获取信息
* 获取属性，可以调用attr()方法来获取属性
```python
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))
```
* 遍历获取多个结果
```python
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('a')
for item in a.item():
   print(item.attr('herf'))
```

* 获取文本
获取其内部的文可以调用text()方法
```python
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())
```
text()会返回所有内部纯文本，中间用一个空格分割开，实际上是一个字符串


## 节点操作
* addClass、removeClass
```python
doc = pq('html')
li = doc('.item-0.active')
print(li)
li.removesClass('active')           #去掉类active
li.addClass('active')               #添加类active
```

* attr、text、html
```python
form pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')              #attru属性传入一个参数就是获取属性值，传入两个参数可以用来修改属性值
li.text('changed item')             #text属性不传参数是获取节点內纯文本，传入参数则是赋值
li.html('<span>changed item</span>')#html属性与text属性一样
```

* remove
```python
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
wrap.find('p').remove()             #移除p节点
print(wrap.text())
```


## 伪类选择器