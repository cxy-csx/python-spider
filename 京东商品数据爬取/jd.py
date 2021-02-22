import requests
from bs4 import BeautifulSoup


def get_shop_data(k):

    url = 'https://search.jd.com/Search?keyword=%s' % k
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)

    return resp.text


def parse_data(html_str):
    html = BeautifulSoup(html_str, 'lxml')
    divs = html.select('div.gl-i-wrap')
    goods = []
    for div in divs:
        price = div.select_one('strong>i').text
        desc = "".join(div.select_one('div.p-name em').text.split())
        link = 'http://' + div.select_one('div.p-name a').get('href').split('//')[-1]
        goods.append({
            'price': price,
            'desc': desc,
            'link': link
        })
    print(len(goods))
    return goods


def main():
    # 1.请输入搜索关键字
    k = input('请输入搜索关键字: ')
    # 2.检索商品
    html_str = get_shop_data(k)
    # 3.解析数据
    goods = parse_data(html_str)
    # 4.价格排序
    goods.sort(key=lambda item: float(item['price']))
    print(goods)


if __name__ == '__main__':
    main()
