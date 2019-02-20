[TOC]
# BeautifulSoup的使用 
简单来说，BeautifulSoup 就是 Python 的一个 HTML 或 XML 的解析库，我们可以用它来方便地从网页中提取数据，官方的解释如下：
>BeautifulSoup提供一些简单的、Python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。 BeautifulSoup 自动将输入文档转换为 Unicode 编码，输出文档转换为 utf-8 编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。 BeautifulSoup 已成为和 lxml、html6lib 一样出色的 Python 解释器，为用户灵活地提供不同的解析策略或强劲的速度。
所以说，利用它我们可以省去很多繁琐的提取工作，提高解析效率。


## 解析器
BeautifulSoup在解析的时候实际上是依赖于解析器的，它除了支持Python标准库中的 HTML 解析器，还支持一些第三方的解析器比如 LXML，下面我们对 BeautifulSoup 支持的解析器及它们的一些优缺点做一个简单的对比。
解析器 | 使用方法 | 优势 | 劣势
---   | --- | --- | ---
python标准库 | Beautifulsoup(markup,'html.parse') | python的内置标准库、执行速度适中、文档容错能力强 | Python2.7.3 or 3.2.2前的版本中文容错能力差
LXML HTML 解析器 | BeautifulSoup(markup, "lxml") | 速度快、文档容错能力强 | 需要安装C语言库
LXML XML 解析器 | BeautifulSoup(markup, "xml") | 速度快、唯一支持XML的解析器 | 需要安装C语言库
html5lib | BeautifulSoup(markup, "html5lib") | 最好的容错性、以浏览器的方式解析文档、生成 HTML5 格式的文档 | 速度慢、不依赖外部扩展  


## 基本使用
下面使用实例感受BeautifulSoup的基本使用：
```python
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
```
首先我们声明了一个变量 html，它是一个 HTML 字符串，但是注意到，它并不是一个完整的 HTML 字符串，body 和 html 节点都没有闭合，但是我们将它当作第一个参数传给 BeautifulSoup 对象，第二个参数传入的是解析器的类型，在这里我们使用 lxml，这样就完成了 BeaufulSoup 对象的初始化，将它赋值给 soup 这个变量。
那么接下来我们就可以通过调用 soup 的各个方法和属性对这串 HTM L代码解析了。
我们首先调用了 prettify() 方法，这个方法可以把要解析的字符串以标准的缩进格式输出，在这里注意到输出结果里面包含了 body 和 html 节点，也就是说对于不标准的 HTML 字符串 BeautifulSoup 可以自动更正格式，这一步实际上不是由 prettify() 方法做的，这个更正实际上在初始化 BeautifulSoup 时就完成了。
然后我们调用了 soup.title.string ，这个实际上是输出了 HTML 中 title 节点的文本内容。所以 soup.title 就可以选择出 HTML 中的 title 节点，再调用 string 属性就可以得到里面的文本了，所以我们就可以通过简单地调用几个属性就可以完成文本的提取了，是不是非常方便？  


## 节点选择器 
* 选择元素（这种选择方式只会选择到第一个匹配的节点，其他的后面的节点都会忽略）
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)                    # 打印title节点的选择结果
print(type(soup.title))              # 打印title节点的类型
print(soup.title.string)             # 打印title节点内的文本
print(soup.head)                     # 打印head节点的选择结果
print(soup.p)                        # 打印p节点的选择结果
``` 

#### 提取信息
在上面我们演示了调用string属性来获取文本的值，那我们要获取节点属性值怎么办呢？获取节点名怎么办呢？下面我们来统一梳理一下信息的提取方式
* 获取名称（可以利用==name== 属性来获取节点的名称）
```python
print(soup.title.name)
```

#### 获取属性（毎个节点可能有多个属性，我们选择到这个节点元素后，可以调用==attrs== 获取所有属性）
```python
print(soup.p.attrs)                    # 打印p节点的属性
print(soup.p.attrs['class'])           # 打印p节点的class属性值
```

上面的写法有点繁锁，还有一种更简单的获取方式，我们可以不用写attrs，直接节点元素后面加中括号，传入属性名就可以达到属性值，示例如下：   
```python
print(soup.p['name'])
print(soup.p['class'])
```
==注意：有的返回结果是字符串，有的返回结果是字符串组成的列表。比如name属性的值是唯一的，返回的结果就是单个字符串，而对于class，一个节点元素可能由多个class，所以返回的是列表，所以在实际处理过程中要注意判断类型。==    

#### 获取内容（可以利用string属性获取）
```python
print(soup.p.string)
```
==再次注意这里选择的p节点是第一个p节点，获取的文本也就是第一个p节点里面的文本。== 


#### 嵌套选择
在上面的例子中我们知道每一个返回结果都是bs4.elemaent.Tag类型，它同样可以继续调用节点进行下一步的选择，比如我们获取了head节点元素，我们可以继续调用head来选取其内部的head节点元素。
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)                  # 调用head后再次调用title来选择title节点元素
print(type(soup.head.title))            # 打印类型
print(soup.head.title.string)           # 打印文本内容
```

#### 关联选择  
我们在做选择的时候有时候不能做到一步就可以选择到想要的节点元素，有时候在选择的时候需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等等。所以在这里我们就介绍下如何来选择这些节点元素。

#### 子节点和子孙节点   
选取到了一个节点元素之后，如果想要获取它的直接子节点可以调用contents属性，例子如下：   
```python
print(soup.p.contents)
```

同时地我们可以调用children属性，得到子孙子节点相应的结果，例子如下:
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.children)                           # 返回的结果是生成器类型
for i, child in enumerate(soup.p.children):      # 使用for偱环输出相应的内容
    print(i, child)                              # 内容是一様的不过是children返回的是生成器类型，contents返回的是列表类型。
```

如果要得到所有的子孙节点的话可以调用descendants属性：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants)                         # 返回的结果还是生成器
for i, child in enumerate(soup.p.descendants):    # descendants会递归地查询所有子节点，得到的是所有的子孙节点
    print(i, child)
```


#### 父节点和祖先节点
如果要获取某个节点元素的父节点，可以调用parent属性：
```python
from bs4 import BeautifulSoup
soup = BeartifulSoup(html,'lxml')
print(soup.a.parent)                               # 输出结果是a节点的父节点元素及其内部的内容
```

如果要获取所有的祖先节点，可以调用parents属性：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
```

#### 兄弟节点
获取同级的节点也就是兄弟节点，示例如下：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling', soup.a.next_sibling)                         # next_sibling获取节点的下一个兄弟元素
print('Prev Sibling', soup.a.previous_sibling)                     # prenious_sibling获取节点的上一个兄弟元素
print('Next Siblings', list(enumerate(soup.a.next_siblings)))      # next_siblings获取节点的下一个所有兄弟元素的生成器
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))  # prenious_siblings获取节点的上一个所有兄弟元素的生成器
```

#### 提取信息
在上面我们讲解了关联元素节点的选择方法，如果我们想要获取它们的一些信息，比如文本、属性等等也是同样的方法。
```python
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')                
print('Next Sibling:')                           # 打印‘Next Sbilinf’
print(type(soup.a.next_sibling))                 # 打印a节点下一个兄弟节点的类型
print(soup.a.next_sibling)                       # 打印a节点下一个兄弟节点元素
print(soup.a.next_sibling.string)                # 打印a节点下一个兄弟节点文本
print('Parent:')                                 # 打印‘Parent’
print(type(soup.a.parents))                      # 打印a节点的祖先节点类型
print(list(soup.a.parents)[0])                   # 打印a节点祖先节点的第0个元素
print(list(soup.a.parents)[0].attrs['class'])    # 打印a节点祖先节点的第0个元素class的值
```
如果返回结果是单个节点，那么可以直接调用 string、attrs 等属性来获得其文本和属性，如果返回结果是多个节点的生成器，则可以转为列表后取出某个元素，然后再调用 string、attrs 等属性来获取其对应节点等文本和属性。


## 方法选择器
前面我们所讲的选择方法都是通过属性来选择元素的，这种选择方法非常快，但是如果要进行比较复杂的选择的话则会比较繁琐，不够灵活。所以 BeautifulSoup 还为我们提供了一些查询的方法，比如 find_all()、find() 等方法，我们可以调用方法然后传入相应等参数就可以灵活地进行查询了。
最常用的查询方法莫过于 find_all() 和 find() 了，下面我们对它们的用法进行详细的介绍。

#### find_all()
查询所有符合条件的元素，可以给它传入一些属性或文本来得到符合条件的元素，功能十分强大。
它的API如下：
```find_all(name,attrs,recursive,text,**kwargs)```
    * name
    我们可以根据节点名来查询元素，下面我们用一个实例：
 ```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))                # 调用find_all()方法查询所有ul节点，返回结果是列表类型，每个元素都是bs4.element。Tag类型
print(type(soup.find_all(name='ul')[0]))       # 查询第0个ul的类型
```

因为都是Tag类型，所以我们依然可以进行嵌套查询，还是同样的文本，在这里我们查询出所有的ul节点后再继续查询其内部的li节点。
```python
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
```
返回结果是列表类型，列表中的毎个元素依然还是Tag类型。

接下来可以遍历毎个li获取它的文本，示例如下：
```python
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
```

#### attrs
除了根据节点名查询，我们也可以传入一些属性来进行查询，示例如下：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id': 'list-1'}))          # 查找所有ID名为list-1的节点
print(soup.find_all(attrs={'name': 'elements'}))      # 查找所有name值为elements的节点
```

对于一些常用的属性比如 id、class 等，我们可以不用 attrs 来传递，比如我们要查询 id 为 list-1 的节点，我们可以直接传入 id 这个参数，还是上面的文本，我们换一种方式来查询。
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(id='list-1'))          # 查找所有id值为list-1的节点
print(soup.find_all(class_='element'))     # 查找所有class值为element的节点，由于class在python里是一个关键字，所以在后面要加下划线。
```

#### text
用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象，示例如下：
```python
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))    
```
在这里有两个a节点，其内部包含有文本信息，在这里我们调用find_all()方法传入text参数，参数为正则表达式对象，结果会返回所有匹配正则表达式的节点文本组成的列表

#### find()
除了find_all()方法，还有find()方法，只不过find()方法返回的是单个元素，也就是第一个匹配的元素，而find_all()返回的是匹配的元素组成的列表。
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
```
返回结果不再是列表形式，而是第一个匹配的节点元素，类型依然是 Tag 类型。
另外还有许多的查询方法，用法与前面介绍的 find_all()、find() 方法完全相同，只不过查询范围不同，在此做一下简单的说明。

* find_parents() find_parent()
find_parents()返回所有祖先节点，find_parent()返回直接父节点

* find_next_siblings()find_next_sibling()
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。

* find_previous_siblings() find_previous_sibling()
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点

* find_all_next() find_next()
find_all_next()返回节点后所有符合条件的节点，find_next()返回第一个符合条件的节点。

* find_all_previous() find_previous()
find_all_previus()返回节点后所有符合条件的节点，find_previous()返回第一个符合条件的节点


## CSS选择器
BeautifulSoup 还提供了另外一种选择器，那就是 CSS 选择器，如果对 Web 开发熟悉对话，CSS 选择器肯定也不陌生，如果不熟悉的话，可以看一下：[w3c](http://www.w3school.com.cn/cssref/css_selectors.asp)

使用CSS选择器，只需要调用select()方法，传入相应的CSS选择器即可，示例如下：
```python
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')              
print(soup.select('.panel .panel-heading'))      # 查找class为'panel'内部的所有class为panel-heading元素
print(soup.select('ul li'))                      # 查找ul所有ul内部的所有li节点组成列表
print(soup.select('#list-2 .element'))           # 查找所有id值为list-2的所有class值为element组成列表
print(type(soup.select('ul')[0]))                # 类型
```


#### 嵌套选择
select()方法同样支持嵌套选择，例如我们先选择所有ul节点，再遍历每个ul节点选择其li节点，示例如下：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))
```


#### 获取属性
我们知道节点类型是 Tag 类型，所以获取属性还是可以用原来的方法获取，仍然是上面的 HTML 文本，我们在这里尝试获取每个 ul 节点的 id 属性。
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
```


#### 获取文本
那么获取文本当然也可以用前面所讲的 string 属性，还有一个方法那就是 get_text()，同样可以获取文本值。
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
```

## 结语
到此 BeautifulSoup 的使用介绍基本就结束了，最后做一下简单的总结：
* 推荐使用 LXML 解析库，必要时使用 html.parser。
* 节点选择筛选功能弱但是速度快。
* 建议使用 find()、find_all() 查询匹配单个结果或者多个结果。
* 如果对 CSS 选择器熟悉的话可以使用 select() 选择法。