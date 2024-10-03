import requests
import os

def makeHead(cookie):
    temp = {
        "Host": "www.luogu.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.luogu.com.cn/",
        "Cache-Control": "no-cache",
        "TE": "Trailers",
        "Cookie": cookie
    }
    return temp

def punch(cookie):
    response = requests.get('https://www.luogu.com.cn/index/ajax_punch', headers=makeHead(cookie))
    # 强制将响应编码设置为 UTF-8
    response.encoding = 'utf-8'
    return response.text

if __name__ == "__main__":
    uid = os.getenv('LUOGU_UID')  # 从环境变量中获取 uid
    client_id = os.getenv('LUOGU_CLIENT_ID')  # 从环境变量中获取 client_id
    cookie = "__client_id=" + client_id + ";_uid=" + uid + ";"  # 构造 Cookie
    result = punch(cookie)  # 发起签到请求
    print(result)  # 输出签到结果
