import requests
from lxml import etree

url = 'https://www.webofscience.com/wos/alldb/summary/5c01cb96-9349-4e3c-9536-0b40306e7c46-460caee9/relevance/1'

headers = {
    'cookie': 'WOSSID=USW2EC0E8E9Jn6EqRY2crKKRSxQQg; dotmatics.elementalKey=SLsLWlMhrHnTjDerSrlG; OptanonAlertBoxClosed=2022-07-28T08:18:31.177Z; _abck=C278C0D02FC1211C76F62D65078A0654~0~YAAQBxQgFwOzq0CCAQAAD/SzSAivkCVRSSw5CJB7z9oHWfwJYEGXDUdcdATomeB8LUprdQReguqfjQsuZ68bGMmuCLuQ9nG63/e7C0by/q+UTyjmKgZk2SVVFFLtG7rb9ZaQxTXgIdxdnoH7nqhiHwKuFWEMmggFZZnzUgwAmX046fn42Lozdtq8bGxNSspngZ9JQnOOZV9CwzFcUgbJz3bCCctdPC2Tg2ofQWh0JFrpGwDVcj8SZtrFDik0+tEv73AIidcqgT195N0SX9AjMYkZR8QB5odGGz4HB74RGEwD1aL7Bu0I2KtGZbXaMCgENjE9AXb6YBwpZOlKaGeZ75qdVqsYEaFo2c4JOJwut5N863vuNBxmiCHS9CXn2aaCXdu/WxfnACsvQlgYh4lC2JtWEHuAiMYMlADyWSfX~-1~-1~-1; bm_sz=44DFB291EEA9C5B1EFFA703BDD333559~YAAQBxQgFwSzq0CCAQAAD/SzSBC3ciTZJfxdWCLwrsXMMEevoRcbRgV6qsgSGbu66Uh2/vXalUMNrfsyAGLHyW1kohNEo6CXcIv9rkOtC599w7A1BMUYHQSFejkFc4K3HHvo6tVLjgFegxRVBO1YnjN3os652OtdaA1cwwlB2PA5PZZ19OUkAzMmDvrKjZc8x7wzN8PM9igm8qbgXJ6cqF/ipUA/STGFaiA+nL73a/vVV+LZou59kZ1BHsAAyD5IhtxdChHkIt92qyjS5q2Lb6CHg3J/G7qapImoI8BFFHM24z0uxuTXxms=~3486276~4538936; ak_bmsc=9C2E6B63829D25B305B3CB62A0097A5D~000000000000000000000000000000~YAAQBxQgFy+6q0CCAQAAlj21SBCoUUyVi6ELd0tSrt1xckkNtIc1VzqVzLcvx8QJwscSy0xPv+XUst2IKJZ8tpAq6NXKAPlO7A4j2uKJ4fa7v7/+TtP9jbutWNe7wgG95oCLHyyZHnU57XdY4UO2moocQh8bWrMWl2qavM2If56X83O0MLEf97xArfQ7znA2dQRnDrHyIk+nWq9VmWUAGmblyrB60cc7Rn6OtZx68pXgfKQgFrH6Ap48KVTi7BanOWq0GKsX/lMTQGAWuVUZSSy1DiuSXb35HMh6Tq5RZJL4nBNpsDBgJDT+x8h8QB7+3MNyFJVYC3a8Ub4emqFatbAHZBfoBlUB/X+eE0+yUAvuqJljS5jJGil2DKwZTRdx2Tk+WFXXd5WM1xo3pjTr9+s=; _sp_ses.840c=*; _sp_id.840c=abfeb2a4-cbd2-412d-b50c-3d21af6dd789.1658996292.6.1659079143.1659066033.b6a130b9-ee57-41e9-9525-950cf9519efc.b9b8d281-a544-4b24-ad23-26277f85e3fe.850ff4dd-b849-499d-9bcb-4631a731045d.1659077213114.4; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jul+29+2022+15%3A19%3A04+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.37.0&isIABGlobal=false&hosts=&consentId=dcef5f92-96e8-4693-9a05-3e362e42fed5&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1&geolocation=CN%3B&AwaitingReconsent=false; bm_sv=79BBB1C2BF2D8BC8F6FB76A3DDCFC8AA~YAAQdYFtaJYrLS6CAQAA07fSSBAWu5IJw02ki8aUdXc/1O/CP/5dfbwum/Re40SLMdWwri6vX7Fekx25eqXGbvaBW1pynXYEmt5ZITeRtIRCuAYbxfYK3D3jgRWsP/uodFiljRXPCy9ebW+9Bu60CoS9vK0QGxgHRCCyymdmxbnJzdyAlttiosv3KEAX9cA/O8dDAXt5aikJNkm5ryxN2I1qM2q3VktyMm4jU3n5SBgqTpWFkHssNgSoHnPzaT03X638melR~1; RT="z=1&dm=www.webofscience.com&si=7f759c5c-7318-4a28-adf5-364357891bb2&ss=l664vusl&sl=0&tt=0&bcn=%2F%2F684d0d43.akstat.io%2F&ld=15f0d&ul=39w"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# request = urllib.request.Request(url=url,headers=headers)
#
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')

content = requests.get(url=url, headers=headers).text

print(content)

tree = etree.HTML(content)

# result = tree.xpath('//div[@class="ng-star-inserted"]//h3/a')
result = tree.xpath('//html')

# print(result)
