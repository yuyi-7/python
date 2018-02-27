#!/usr/bin/env python
# encoding: utf-8

import requests
import os
from bs4 import BeautifulSoup
from PIL import Image

__author__ = 'yuyi-7'


class Guitar(object):
    """docstring for guitar"""

    def __init__(self, url):
        super(Guitar, self).__init__()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400',
            'Connection': 'keep-alive', 'Cache-Control': 'private, must-revalidate', 'Content-Encoding': 'gzip',
            'Content-Type': 'text/html; charset=UTF-8'}
        self.url = requests.get(url, headers)
        self.soup = BeautifulSoup(self.url.content, 'lxml')
        path = r'C:\Users\Administrator\Desktop\guitar'
        if not os.path.isdir(path):
            os.mkdir(path)

    def name(self):
        title = self.soup.find('h1', class_='ph')
        self.names = title.get_text()

    def savelocal(self, path, image):
        f = open(path, 'ab')
        image_down = requests.get(image)
        f.write(image_down.content)
        f.close()

    def picture(self):
        td = self.soup.find('td', id='article_contents')
        #print(self.soup)
        td = td.find_all('img')
        img = []
        image = []
        width = []
        high = []
        num = len(td)
        print('抓取到曲谱，总共有%d张曲谱'%num)
        for i in range(num):
            img.append(td[i].get('src'))
            path = r'C:\Users\Administrator\Desktop\guitar\%s.png'%(i)
            self.savelocal(path, img[i])
            print('正在保存第%d张曲谱'%(i+1))
            image.append(Image.open(path))
            widths, highs = image[i].size
            width.append(widths)
            high.append(highs)
        for j in range(num - 1):
            newwidth = width[j] + width[j + 1]
            newhigh = high[j] + high[j + 1]
        print('正在拼合曲谱')
        if num % 2:
            target = Image.new('RGB', (width[0], newhigh))
            for i in range(num):
                if i == 0:
                    target.paste(image[i], (0, 0))
                else:
                    target.paste(image[i], (0, high[i - 1]))
            self.name()
            print('拼合曲谱成功，正在保存')
            target.save(r'C:\Users\Administrator\Desktop\guitar\%s.png' % (self.names), quality=100)
            print('已保存')
        if num % 2 == 0:
            target = Image.new('RGB', (width[0] * 2, newhigh / 2))
            for i in range(num):
                if i == 0:
                    target.paste(image[0], (0, 0))
                    continue
                if i == 1:
                    target.paste(image[1], (width[0], 0))
                    continue
                if i % 2 == 0:
                    target.paste(image[i], (0, high[i - 1]))
                    continue
                if i % 2 != 0:
                    target.paste(image[i], (width[0], high[i - 1]))
                    continue
            print('正在保存')
            target.save(r'C:\Users\Administrator\Desktop\guitar\%s.png' % (self.names), quality=100)
            print('已保存')
        print('正在删除缓存')
        for i in range(num):
            repath = r'C:\Users\Administrator\Desktop\guitar\%s.png'%(i)
            os.remove(repath)
        print('删除缓存完毕')


if __name__ == '__main__':
    url = input('请输入该曲谱的网页网址：')
    # http://www.17jita.com/tab/whole_7883.html
    shili = Guitar(url)
    shili.picture()
    print('曲谱下载成功！')
