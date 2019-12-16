#coding:utf-8
#author:Ericam_
import scrapy
import re
import sys
from bs4 import BeautifulSoup
import urllib.request
import time

class GzrSpider(scrapy.Spider):
    name = 'GZR2'
    allowed_domains = ['biqudao.com']
    start_urls = ['https://www.biqudao.com/bqge1618/2911745.html']
    
    def get_download(url):
        file = urllib.request.urlopen(url)
        data = BeautifulSoup(file , from_encoding="utf8")
        section_name = data.title.string
        section_text = data.select('#wrapper .content_read. box_con #content ')[0].text        
        section_text=re.sub( '\s+', '\r\n\t', section_text).strip('\r\n')   
        fp = open('GZR.txt','a')   
        fp.write(section_name+"\n")  
        fp.write(section_text+"\n")  
        fp.close() 
        pt_nexturl = 'var next_page = "(.*?)"'
        nexturl_num = re.compile(pt_nexturl).findall(str(data))
        nexturl_num = nexturl_num[0]
        return nexturl_num
 
    if __name__ == '__main__':
        url = "https://www.biqudao.com/bqge1618/2911745.html"
        num = 2341
        index = 1
        get_download(url)
        while(True):
            nexturl = get_download(url)
            index += 1
            sys.stdout.write("已下载:%.3f%%" % float(index/num*100) + '\n')
            sys.stdout.flush()
            url = "https://www.biqudao.com/bqge1618/"+nexturl
            if(nexturl == 'https://www.biqudao.com/bqge1618/'):
                break
        print(time.clock())