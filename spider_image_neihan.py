from urllib.request import urlopen,urlretrieve
import os,re
import time
from tkinter import *

#top = Tk()
#top.title('内涵吧第一页下载')
#top.geometry('600x300')
#tax = Text(top)
#tax.pack()

def getHTML(url):
    #字符串方式返回html文件
    urll = urlopen(url)
    try:
        html = urll.read().decode('utf-8')
    except UnicodeDecodeError:
        pass
    return html

def spider(url,name = '内涵吧'):
    #传入URL爬取每个url中的图片，并根据标题创建目录
    html = getHTML(url)
    reg = re.compile(r'<img.*?src="(.*?)".*?>')
    reg_t = r'<title>(.*?)</title>'
    title = re.search(reg_t,html).group(1)
    sign = re.compile(r'[\?、\\/\'\'\*\:\;\<\>\s]')
    title=sign.sub(' ',title)
    #title = title.replace('/',' or ')
    dir_name = 'E:\\image\\' + title
    if title in os.listdir('E:\\image'):
        return
    else:
        os.mkdir(dir_name)
    b = reg.findall(html)
    c = 1
    log = open((dir_name+'\\log.txt'),'a')
    for i in b:
        try:
            urlretrieve(i,(dir_name+'\\' + name + str(c) + i[-4:]))
            #tax.insert(INSERT,i+'\n')
            print(i)
            log.write(i+'\n')
        except:
            continue
        c += 1
    log.close()
    
    #urll.close()
    time.sleep(5)

def spider_neihan(n = 1):
    #根据内涵吧的目录页号码爬取每个U的url存入列表，并调用spider()爬取
    neihan8 = 'http://www.neihan8.com/av'
    if n == 1:
        page = neihan8
    else:
        page = '%s/index_%d.html'%(neihan8,n)
    html = getHTML(page)
    reg_av = r'<a\shref="/av(.*?)"\stitle'
    link = re.findall(reg_av,html)
    for i in link:
        spider(neihan8+i)
    print('第%d页下载完成'%n)

if __name__=='__main__':
    for k in range(1,11):
    #重复给spider_neihan()传入页码号
        spider_neihan(k)
#top.mainloop()


