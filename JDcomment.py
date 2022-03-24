import requests
from lxml import etree

url = 'https://club.jd.com/comment/productPageComments.action'
# '?callback=fetchJSON_comment98&productId=100007735968&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
params = {
    # 'callback': 'fetchJSON_comment98',
    'productId': '100007735968',
    'score': '0',
    'sortType': '5',
    'page': '0',
    'pageSize': '10',
    'isShadowSku': '0',
    'fold': '1',
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'Host': 'club.jd.com',
    'Referer': 'https://item.jd.com/',
}
page_text = requests.get(url = url,params = params, headers = headers).json()
for comment in page_text['comments']:
    content = comment['content']
    star = comment['score']
    name = comment['nickname']
    model = comment['productColor']
    time = comment['creationTime']
    print(name,star,content,model,time)
# tree = etree.parse(page_text)
# div_list = tree.xpath('/html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div')
# print(div_list)