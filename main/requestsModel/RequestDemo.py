#使用这个封装好的第三方requests库 更方便使用
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
r.text #编码过的内容
r.content #字节式内容

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)