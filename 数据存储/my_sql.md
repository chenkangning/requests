* CREATE DATABASE:使用这条语句设置装有表的数据库
* USE DATABASE：进入数据库以创建表
* CREATE TABLE:开始设置你的表，但还需要知道COLUMN NAMES和DATA TYPES---可通过分析要存入表的数据种类而得知
* NULL与NOT NULL:需要知道哪些列不应该接NULL值，才能帮助你整理和搜索数据。当你创建表时需要设置列为NOT NULL。
* DEFAULT:用于指定某列的默认值，在输入一条记录但没有为某列赋值的时候。
* DROP TABLE:用于删除岀错的表，但最好在使用任何INSERT语句向表中插入数据前删除表

* DESC:查看表的结构
* INSERT:为表插入数据
* NULL:是未定义的值。它不等于零，也不是等于空值。值是可以是NULL，但绝非等于NULL。
    * 可以把列修改为不接受NULL值，这需要在创建表时使用关键字NOT NULL

* AND:需要所有条件都成立
* OR:需要任何条件成立时

* SELECT *:用于选择表中的所有列。
* 用'与\转义:字符串中的单引号或反斜线来把它转换成直接量。
* = <> < > <= >=:等于 不等于 小于 大于 小于等于 大于等于。

* IS NULL:可用于创建检查麻烦的NULL值的条件。
* AND与OR：有了AND与OR，就可以在WHERE子句中结合查询更精确。
* NOT:NOT反转查询结果，取得相反的值。
* BETWEEN:选选一个范围的值。
* LIKE搭配%或_:使用like搭配通配符，可搜索部分文本字符串。

* DELETE的规则
    * DELETE不能删除单一列中的值或表中的某一列的所有值。
    * DELETE可用于删除一行或多行，根椐WHERE子句而定。
    * 我们已经知道如何从表中删除一行，也可以删除多行。为了实现这个目标，我们利用WHERE子句告诉DELETE该选择哪些行。WHERE子句和第2章中搭配SELECT时的使用方法完全相同，凡是第二章用于WHERE子句中的关键字，如LIKE、IN、BETWEEN，都可以在此处使用，而且所有条件都能更准确地要求RDBMS删除特定行。
    * 还有，这一段语句可以删除表中的每一行：DELETE FROM YOUR_TABLE

* UPDATE的规则
    * 使用UPDATE，你可以改变单一列或所有列的值。在SET子句中加入更多column=values组，其间以逗号分隔：
    UPDATE YOUR_TABLE SET first_column = 'newvalue',second_colum = 'another_values';
    * UPDATE可用于更新单一行或多行，一切都交给WHERE子句决定。

* DELETE:这是删除表中记录的工具。它和WHERE子句一起使用，可精确地瞄准你想删除的行。
* UPDATE:这条语句以新值更新现有的一列或多列，它也可以使用WHERE子句。
* SET:这个关键字属于UPDATE语句，可用于改变现迶列的值。

