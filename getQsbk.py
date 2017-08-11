#coding:utf-8
from urllib import request # 导入解析网页包
import re #导入正则表达式包

#获取网页源代码
def getHtmlSource(url):
    print('begin get html....')
    html = ''
    try:
        #设置headers头 User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'} 
        body = request.Request(url,headers=headers);
        html = request.urlopen(body)#获取网页源代码
    except Exception as e:
        print('html get error:%s' % e)
        return ''
    finally:
        print('end get html.....')
    return str(html.read(),encoding='utf-8')

#解析网页源代码
def getContext(htmlSource,isSaveFile=False,filePath='context.txt'):
    context = dict()
    for i in range(0,25):
        context[i] = dict()#建立一个list(dic())
    #正则表达式结果为一个list[tuple]，
    reg = re.compile(r'<h2>([\s\S]*?)</h2>[\s\S]*?<div class="content">[\s\S]<span>([\s\S]*?)</span>[\s\S]*?</div>[\s\S]*?<i class="number">(\d*)?</i>[\s\S]*?<div class="single-clear"></div>([\s\S]*?)</div>',re.M|re.S)
    findList = re.findall(reg,htmlSource)
    for i in range(len(findList)):
        context[i]['authorName'] = findList[i][0].replace('\\n','',2).strip() #段子作者
        context[i]['txtBody'] = findList[i][1].replace('\\n','',10).replace('<br/>','',50).strip() #段子内容
        context[i]['txtGoodNum'] = findList[i][2] #段子点赞数量
        if findList[i][3] == '\n\n': #没有神评
            context[i]['godCommentAuthor'] = '无'#神评作者
            context[i]['godCommentBody'] = '无' #神评内容
            context[i]['godCommentGood'] = '无' #神评点赞数量
        else:
            reg = re.compile(r'<span class="cmt-name">(.*?)：</span>[\s\S]*?<div class="main-text">(.*?)<div class="likenum">[\s\S]*?.png.*b4ad">[\s\S]*?(\d+)',re.M|re.S)#在神评块中找到神评作者、内容和点赞数量
            godList = re.findall(reg,str(findList[i][3]))
            context[i]['godCommentAuthor'] = godList[0][0].strip() #神评作者
            context[i]['godCommentBody'] = godList[0][1].strip() #神评内容
            context[i]['godCommentGood'] = godList[0][2] #神评点赞数量
    if isSaveFile:
        with open(filePath,'w+') as f:
            f.write(str(findList).replace('\\n','\n',100))
    return context

htmlSource = getHtmlSource('https://www.qiushibaike.com/text/')
context = getContext(htmlSource)
for i in context:
    print("段子作者:",context[i]['authorName'])
    print("段子内容:",context[i]['txtBody'])
    print("段子点赞数量:",context[i]['txtGoodNum'])
    print("神评作者:",context[i]['godCommentAuthor'])
    print("神评内容:",context[i]['godCommentBody'])
    print("神评点赞数量:",context[i]['godCommentGood'])
    print()
