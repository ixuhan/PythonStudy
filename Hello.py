#coding:utf-8
#简单的输出语句
print 'hello world'   #在2.*的版本中能省略掉括号
print ('hello world') #在3.*的版本中没有括号就报错
#结论：为了兼容，以后都用有括号的。

#基本数据类型
#int
a = 1 #在申明变量的时候，前面不加变量类型 比如 int a = 1 就是错的。
print (a,type(a)) #type函数，可以