import urllib.request, urllib.parse, json, re, time, os
from bs4 import BeautifulSoup
fp = open('url.txt', 'r')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
dict2 = json.loads(fp.read())
get_url = 'https://www.mm131.net/xinggan/{}.html'
img_url="https://img1.mmmw.net/pic/{}/{}.jpg"
def download_img(url,filename,headers2):
    request = urllib.request.Request(url=url, headers=headers2)
    img  = urllib.request.urlopen(request)
    with open(filename,'wb') as fp:
        fp.write(img.read())
def get_img_url(title, img_num):
    request = urllib.request.Request(url=get_url.format(img_num), headers=headers)
    headers2 = {'Host': 'img1.mmmw.net',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'no-cors',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Referer': get_url.format(img_num)
                }
    # try:
    response = urllib.request.urlopen(request)
    # except ConnectionAbortedError as e:
    #     print('网络发生中断')
    #     get_img_url(title, img_num)
    # except urllib.error.URLError as e:
    #     print('网络发生中断')
    # get_img_url(title, img_num)
    result = response.read().decode('gbk')
    soup = BeautifulSoup(result, 'lxml')
    end_page = len(soup.find('div', class_='content-page')) - 3
    if not os.path.exists('G:\\mm131\\{}'.format(title)):
        os.mkdir('G:\\mm131\\{}'.format(title))
    path = 'G:\\mm131\\{}'.format(title)
    for i in range(1, end_page + 1):
        url = img_url.format(img_num, i)
        download_img(url , filename=path + '\\'+str(i) + '.jpg', headers2 = headers2)
star = 0
for title , url in dict2.items():
    if title == '宅男女神妮小妖身姿曼妙风情万种':
        star = 1
        print("开始了")
    if star == 1:
        print('{}开始下载'.format(title))
        img_num = url.split('/')[4]
        get_img_url(title, img_num)
        print('{}下载完成'.format(title))
        time.sleep(0.5)




