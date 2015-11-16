#coding=utf8
import requests
import datetime,re
from bs4 import BeautifulSoup

grasp_url=['http://wooyun.org/bugs/new_submit/page/']
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

class GetVulname:
    '''
        抓取链接名字
    '''

    def __init__(self, urllist=grasp_url):
        self.urllist = urllist

    def getContent(self):
        '''
            获取网页内容
        :return:
        '''
        for url in self.urllist:
            if 'wooyun' in url:
                print "wooyun : %s" % url
                page1 = requests.get(url=url+'1',headers=headers)
                #print 'page1 : %s' % page1.text
                page2 = requests.get(url=url+'2',headers=headers)
                return page1,page2

    def findVul(self):
        '''
        获取漏洞信息
        :return:
        '''
        page1, page2 = self.getContent()
        timetmp = datetime.datetime.now()
        nowtime = timetmp.strftime("%Y-%m-%d")
        soup_page1 = BeautifulSoup(page1.text, 'lxml')
        print "page1.txt %s " % soup_page1.strings
        soup_page2 = BeautifulSoup(page2.text, 'lxml')
        strings_page1 = list(soup_page1.strings)
        strings_page2 = list(soup_page2.strings)
        print "strings_page1 %s " % strings_page1
        result = ""
        for key,string in enumerate(strings_page1):
            if string == nowtime:
                result += strings_page1[key+2]+'<br>'
                print 'result : %s' % result
        for key,string in enumerate(strings_page2):
            if string == nowtime:
                result += strings_page2[key+2]+'<br>'

        return result

class get360vul:
    '''
        抓取链接名字
    '''

    def __init__(self, urllist=['http://loudong.360.cn/vul/list/page/']):
        self.urllist = urllist

    def findnum(self,text):
        p = '^￥\d{2,3}'
        m = re.findall(p,text)

        if m:
            #print "True ; %s " % text
            return True
        else:
            #print "False : %s " % text
            return False


    def getContent(self):
        page1 = None
        page2 = None
        for url in self.urllist:
            if "360" in url:
                print "360 : %s" % url
                try:
                    page1 = requests.get(url=url+'1',headers=headers)
                    page2 = requests.get(url=url+'2',headers=headers)
                except Exception , e:
                    print e
                return page1,page2

    def findVul(self):
        page1, page2 = self.getContent()
        timetmp = datetime.datetime.now()
        nowtime = timetmp.strftime("%Y年%m月%d日")
        soup_page1 = BeautifulSoup(page1.text, 'lxml')
        soup_page2 = BeautifulSoup(page2.text, 'lxml')
        strings_page1 = list(soup_page1.strings)
        strings_page2 = list(soup_page2.strings)
        result_str = ""

        for key,string in enumerate(strings_page1):
            #print "loudong %d: %s :"% (key,string.encode("ISO-8859-1"))
            if nowtime in string.encode("ISO-8859-1"):
                if self.findnum(strings_page1[key-3].encode('ISO-8859-1')):
                    result_str += strings_page1[key-4].encode("ISO-8859-1")+'<br>'
                else:
                    result_str += strings_page1[key-3].encode("ISO-8859-1")+'<br>'
        for key,string in enumerate(strings_page2):
            #print "loudong %d: %s :"% (key,string.encode("ISO-8859-1"))
            if nowtime in string.encode("ISO-8859-1"):
                if self.findnum(strings_page2[key-3].encode('ISO-8859-1')):
                    result_str += strings_page2[key-4].encode('ISO-8859-1')+'<br>'
                else:
                    result_str += strings_page2[key-3].encode("ISO-8859-1")+'<br>'

        return result_str