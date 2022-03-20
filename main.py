import json
import re
from time import strftime, sleep

import requests
# 函数 函数名():
def a():
    # 路径
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/63dd903c-55b0-4c0d-a4a0-bf77e4bde8ea'
    # 通过什么访问，用户代理：
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    # 得到网页信息(获取请求响应)
    gf=requests.get(url,headers=head)
    getjson=json.loads(gf.text)
    # 输出键值对的“值”
    print("------------------商品：" +getjson['data']['share_title'] + "------------------")
    print("规格：" + getjson['data']['spec'])
    # int转string
    print("价格：" + str(getjson['data']['market_price']))
    print("原价/折扣价：" + str(float(getjson['data']['market_price'] * 0.01)) + '元/' + str(float(getjson['data']['price'] *0.01)) + '元')
    print("详细内容：" + getjson['data']['share_content'])
    # 空一行
    print ('\n' * 1)
    print("------------------“" + getjson['data']['share_title'] + "”的价格波动------------------")
    while (1):
        res = requests.get(url, headers=head)
        price = re.findall(r'price":(.*?),', res.text)[0]
        price = str(int(price) / 100)
        # 获取当前时间
        nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M,价格为' + price)
        print(nowTimeAndPrint)
        # 休眠6秒
        sleep(6)

# main主函数
if __name__ == '__main__':
    a()

    # print("" + getjson[])