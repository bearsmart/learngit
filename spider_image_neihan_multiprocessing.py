from urllib.request import urlopen,urlretrieve
import os,re
import time
#from threading import Thread
from multiprocessing import Pool

def getHTML(url):
    urll=urlopen(url)
    try:
        html=urll.read().decode('utf-8')
    except UnicodeDecodeError:
        pass
    finally:
        urll.close()
    return html

def spider(url,name='内涵吧'):
    html=getHTML(url)
    reg = re.compile(r'<img.*?src="(.*?)".*?>')
    reg_t = r'<title>(.*?)</title>'
    title=re.search(reg_t,html).group(1)
    dir_name = 'D:\\image\\' + title
    os.mkdir(dir_name)
    b=reg.findall(html)
    c=1
    for i in b:
        try:
            urlretrieve(i,(dir_name+'\\' + name + str(c) + i[-4:]))
            print(i)
        except:
            continue
        c+=1
    time.sleep(10)

def spider_neihan(n=1):
    
    neihan8 = 'http://www.neihan8.com/av'
    if n==1:
        page=neihan8
    else:
        page = '%s/index_%d.html'%(neihan8,n)
    html = getHTML(page)
    reg_av = r'<a\shref="/av(.*?)"\stitle'
    link=re.findall(reg_av,html)
    for i in link:
        spider(neihan8+i)
    print('第%d页下载完成')

def main():
    print('开始下载',time.ctime())
    #p = [1,2,3,4]
    # threads = []
    # for i in p:
    #     t = Thread(target=spider_neihan,args=(i,))
    #     threads.append(t)

    # for i in range(4):
    #     threads[i].start()
    # for i in range(4):
    #     threads[i].join()
    # print('下载完成')
    pool = multiprocessing.Pool(processes=4)
    for x in range(1,4):
        pool.apply_async(spider_neihan,(i,))
    pool.close()
    pool.join()
    print('下载结束',time.ctime())


if __name__ == '__main__':
    main()



