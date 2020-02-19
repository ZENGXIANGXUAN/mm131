import urllib.request,urllib.parse,json,re,time
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url1 = 'https://www.mm131.net/xinggan/'
url2 = 'https://www.mm131.net/xinggan/list_6_{}.html'
dict1 = {}
def get_url(url):
    request =urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response.read().decode('gbk'),'lxml')
    div = soup.find('div', class_="main")
    list_backup = div.select('.main > dl > dd > a > img')
    for i in list_backup:
        dict1[i['alt']] = i['src']
    time.sleep(0.5)
    return dict1
# print(dict1)
for i in range(1,210):
    print(i)
    if i == 1:
        get_url(url1)
    else:
        get_url(url2.format(i))
#     print(dict1)