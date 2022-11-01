# auth: code_king
# time: 2022/8/4 16:28
# file: scrapy_test.py
import requests

url = 'https://webbook.nist.gov/chemistry/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
content=requests.get(url=url,headers=headers).text
print(content)
