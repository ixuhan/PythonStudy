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

class laugth(object):
    active = 'haha'
    def showLaugth(self):
        for i in range(2):
            print (self.active)#用self.attr取得属性
    def __init__(self): #构造函数，在建立对象的时候自动调用
        print ('init!',self.active)
me = laugth()
me.active = 'hehe'
me.showLaugth()

class cry(laugth): #继承了laugth
    __whyCry = 'loser' #两个下划线开头的函数是私有的
    cryVoice = 'wawawa'
    def __init__(self):
        print ('i need for cay')
    def __init__(self,say): #有参构造函数
        print ('i am the anther world',say)
    def beginCry(self):
        for i in range(3):
            print (self.cryVoice)
    def changeCryVoice(self,newVoice):
        self.cryVoice = newVoice
    def __showWhy(self): #两个下划线开头的函数是私有的
        print (self.whyCry)
    def showPrivate(self):
        print (self.__whyCry)
#you = cry() 同时有无参和有参构造函数时，无法调用无参构造
you = cry('i want you')
you.beginCry()
you.changeCryVoice('wuwuwu')
you.beginCry()
you.showLaugth() #继承后拥有父类所有的属性和方法
you.active = 'lalala'
you.showLaugth()
you.__whyCry = 'happy' #尝试修改私有属性
you.whyCry = 'happy'
you.showPrivate() #打印的是loser，修改失败

print (dir(list)) #查询一个类的所有属性
print (dir(cry))
print (help(list))

a = [1,2,3]
b = a    #用=拷贝后a改变b会改变
c = a[:] #用[:]拷贝后a改变c不会改变
a[2] = 1
print (a)
print (b)
print (c)

print ([1,2] + [3,4])
#print ([1,2] - [3,4]) #因为list里面没有sub减法
#尝试给list添加减法
class strongList(list):
    def __sub__(self,b): #self相当于减法的被减数，b是减数
        a = self[:] #拷贝
        for i in self:
            if i in b:
                a.remove(i)
        return a
print (strongList([1,2,3,5,4,4,7]) - strongList([3,4])) #添加减法后成功

dic = {'name':'hank','age':'21','sex':'boy'} #构建一个词典，类似于map
print (type(dic))
print (dic['name']) #输出value
print (dic)
dic['glasses'] = 'true'
if dic['glasses'] == 'true':
    print ('四眼仔')
for key in dic: #手动遍历词典
    print(key,dic[key])
print (dic.keys()) #系统函数，返回所有的key值
print (dic.values()) #系统函数，返回所有的value值
print (dic.items()) #系统函数，返回所有的键值对
del dic['glasses'] #删除字典的key
print (dic.items())
print (len(dic))

#文件操作
f = open('1.txt','a')
#lines = f.readlines()
#for i in lines:
#    print(i,end='')
for i in dic.keys():
    f.write(i+'：'+dic[i]+'\n')
f.close()
print ('come')

def add(a,b,c):
    return a+b+c
print(add(1,2,3))#直接按顺序传递参数
print(add(a=2,c=1,b=3))#也可以用名称制定参数，类似mybatis
def pri(a=0,b=0,c=0):#在函数上可以指定参数的默认值
    print ('a=',a,',b=',b,',c=',c,end='')
print(pri(1,2,3))
print(pri())#有默认值

def numpri(*num): # 一个*号，代表未知个数的参数，打包成为tuple
    print(type(num))
    for i in num:
        print (i,',',end='')
numpri(1,1,2,3,4)
def numpri2(**num):# 两个*号，同样代表未知个数的参数，打包成为dict
    print(type(num))
    for i in num.keys():
        print (i,',',end='')
numpri2(i='1',j='2',k='3')#传递时，按字典的格式
#为了方便
num=(1,2,3,4)#先打包
numpri(*num)#一起传递过去，但是一定要加上*号
num={'i':'1','j':'2'}
numpri2(**num)

#python循环
S = 'Administrator'
for i in S:
    print (i,end='')
for i in range(0,len(S),2):#beain,end,step
    print (S[i])
for (index,char) in enumerate(S):#取出来变成词典
    print(index,char)
ta = [1,2,3]
tb = [4,5,6]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):#zip
    print (a,b,c)

#lambda
func = lambda x,y:x+y #相当于x,y参数 返回x+y
print (func(3,4))
func = lambda f,a,b:print('test')
print (func(1,2,3))

def test(f,a,b): #f参数应该传递一个函数
    print('test')
    print(f(a,b))
print(test((lambda x,y:x**2+y),6,9))#传递lambda函数

re = map((lambda x,y,z:x+y+z),[1,3,5],[1,3,5],[1,3,5]) #map函数就是把前面的lambda函数作用在后面的list中
for i in list(re):#map第一个参数lambda表达式，把后面的list（n）带入
    print (i)
    
def func(a):
    if a > 10:
        print ('>10')
    elif a < 10:
        print ('<10')
    else:
        print ('=10')
print (list(filter(func,[1,10,15,20,50,100]))) #filter 让后面的值分别作用前面的函数

re = iter(range(5))
try:
    for i in range(5):
        print (re.next())
except AttributeError:
    print ('AttributeError')
print ('HaHaHaHa')

func = lambda :print('lambda test')
func()

help(1) #查看int object的方法
print (1+2) #实际执行了(1.__add__(2))

f = open('1.txt','a')
print (f.closed)
f.close()
print (f.closed)

with open('1.txt','a') as f:#用with...as打开资源管理器，离开时自动关闭f
    print(f.close)
    help(f)#实际上f有__enter__和__exit__在进入和退出时调用
    dir(f)
print (f.closed)

#重写__enter__和__exit__方法测试
class stu(object):
    def __init__(self,text):
        self.text = text
    def __enter__(self):#重写enter方法，必须返回self
        print('enter')
        return self
    def __exit__(self,exc_type,exc_value,traceback):#重写exit方法，必须有4个参数
        print('exit')
with stu('hello') as f:
    print (f.text)
class test(object):
    def say(self,word):
        return 'hello,'+ word
print (test().say('nihao'))

def test():
    def say(self,word):
        return 'hello'+word

flist = [1,2,3]
print(flist)
for i in range(len(flist)):
    flist[i] += 1
print(flist)

