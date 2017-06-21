#coding:utf-8
#简单的输出语句
#print 'hello world'   #在2.*的版本中能省略掉括号
print ('hello world') #在3.*的版本中没有括号就报错
#结论：为了兼容，以后都用有括号的。

#基本数据类型
#int
a = 1 #在申明变量的时候，前面不加变量类型 比如 int a = 1 就是错的。
print (a,type(a)) #type函数，可以查看变量的数据类型
#float
a = 1.1 #变量回收，a不需要删除，只需要重新使用即可，python会自动转换类型
print (a,type(a))
#bool
a = True #布尔变量，True真False假，首字符必须大写
print (a,type(a))
#String
a = 'Hello!' #单双引号都可以
print (a,type(a))
#结论：变量不需要申明类型，不需要删除，可以反复利用

#序列
#tuple
s1 = (2,1,True) #tuple用()圆括号
print (s1,type(s1))
#list
s2 = [2,1,False] #list用[]尖括号
print (s2,type(s2))
#区别 s1不可变，s2可变
s2[0] = 1 #s1不能这样改变，否则报错'tuple' object does not support item assignment
s3 = (False,s1) #序列可以用包含关系
print (s1,type(s1))
s4 = [1,True,[2,'hello'],(3,23.3)] #序列之间可以任意包含
print (s4,type(s4))
print (s1[0],s2[1],s3[1][2],s4[3][1]) #类似多维数组
#快捷输出方式：基本样式[下限:上限:步长]
print (s1[:1]) #从开始到下标为1的所有值，不包含下标为1的临界点
print (s2[1:]) #从下标1到末尾的所有值，包含下标为1的临界点
print (s3[0::1]) #从下标0到末尾，每隔1取一个元素
print (s4[1::-1]) #从下标1到末尾，每隔-1取一个元素
#字符串也可以认为是序列
s5 = 'hello world!'
print (s5[1:6])
#结论：序列分为tuple()和list[]，只有list可变。字符串可认为是一种tuple

#基本运算
#数学运算
print (1 + 2)
print (6 - 4)
print (2 * 3)
print (6 / 4)
print (6 % 4)
print (3 ** 2) #乘方3^2
#判断
print (1 == 2)
print (1 < 2)
print ('a' == 'a')
print (1 in s4) #in类似数据库的用法
print (1 is 1)
print (1 is not 2)
#逻辑
print (True and True)
print (True and False)
print (False or True)
print (not True) #和java中的!true一样
#总结：记住一些基本运算

#条件控制
#if if后面的条件没有括号，用：开启代码块，且用4个空格缩进代表隶属关系
if 1 < 2: #如果1<2
    print ('in one case') #前面有4个空格，代表这句话隶属上面的if语句
print ('out one case') #前面没有空格了，代表隶属关系结束
#复杂的if语句
i = 7
if i < 5:
    print ('i less 5')
elif i == 5: #elif = else if
    print ('i is 5')
else:
    print ('i more 5')
#嵌套if
i = 3
j = 6
if i < 5:
    if j < 5:
        print ('i , j less 5')
    else:
        print ('i less 5 , j more 5')
else:
    if j < 5:
        print ('i more 5 , j less 5')
    else:
        print ('i , j more 5')
#总结：python对缩进很严格，用4个空格代表隶属关系，不要随意缩进

#循环
#for
a = (1,2,'a',True)
for b in a:
    print (b), #Python2.*不换行就在后面加个逗号，3.*不换行需要加end=''
print
b = range(10) #生成0-9的序列
for a in b:
    print (a),
print
c = range(0,7,2) #生成0-7的序列，每隔2个取一次
for a in c:
    print (a),
print (type(tuple(c)))
#while
a = 1
while a < 10:
    print (a),
    a += 1
print
a = 0
while a < 10:
    a += 1
    if a == 2:
        continue
    elif a == 8:
        break
    else:
        print (a),
print
#总结：range生成数字数组，for/while循环，continue/break关键字

#函数
def square_num(a,b): #申明一个函数，返回a的b次方
    return a**b
print (square_num(2,3))

def add_num(a,b):
    return a+b
print (add_num(1,2))

def say_hello():
    print ('func say hello')
say_hello()

def init_tuple():
    return (1,2,True,'False') #返回多个值，相当于一个tuple
print (init_tuple())

#练习:写一个判断闰年的函数，参数为年。若是是闰年，返回True
def doubleYear(year):
    return True if ((year%4==0 and year%100!=0) or year%400==0) else False
a = int(input('输入年份:'))
print ( a , 'is' , '闰年' if doubleYear(a) else '平年')

#对象
class person(object): #定义一个person对象，继承于object
    name
    age
    sex
    def sayHello(self):
        print (age,'岁的',sex,name,'说：Hello')
p = person
p.sayHello()