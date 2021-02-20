
import requests
import time
import csv
import pdfkit
import re


def get_articles(url):

    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36",
        "Host": "mp.weixin.qq.com",
        "cookie": "ua_id=UsOqPPnFUHh6d1sQAAAAAMNS2beMiLij99TJrBU8Xfo=;uuid=c34e31e0c4250b848ac26c2a408585ff;rand_info=CAESIFjlzYGbONX5qIfq3/au0Ef7P35lGHrhCKQ2PBOnfhRR;slave_bizuin=3556303056;data_bizuin=3537456602;bizuin=3556303056;data_ticket=vqOKIZdGaTGkt0rVocUnHcXaVcWDREvcTMW2LwqizlFkPjHT0VRVNwFGetFwpnW2;slave_sid=d0d2SUhyQk1ySUJHR0thQUhqSUduSWpkX09uQXN1YTA3M19KMGtXQ25aNzBIanlHaG96OEE2T3Y3Qk5aeWNLNTNQTldzWDJuZ1hyV3ZaSDFiV0JYZlI3bGFIX0U4eWdRNjlaOWY4VFVia0xqZzNDQjNudlFpOXQ5enVZQlp2ZnhHalZialY5ckszSnZBVnJK;slave_user=gh_c05fc02889f7;xid=616e6e1cb00aaa6e575a3fc370906145;openid2ticket_o2k3Z0pn-dGDlcI2z47X7DSheqn0=;mm_lang=zh_CN",
        "Referer": "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA5MzUwNjUzMA==&scene=124&uin=MzYzMjM3MDM5OQ%3D%3D&key=eb4b4be22fc814549e61386975e4170e22f42bdf14988467d888f3520344a36a3aa1eaa52a7cc11d1d7a124a1e1ce9babf0dcf56107f9da6c4f2570a7ca1607205f6d20d31e0c39cd9a0808afda06bc2&devicetype=Windows+10&version=62080079&lang=zh_CN&a8scene=7&pass_ticket=JyPWffZVh72os2YdgnS%2B0msYQjvM7%2BeeKPct%2Bs1OIj4Urqe6C9%2BLwCgJE21G2yRe&winzoom=1"
    }
    response = requests.get(url, headers=headers)
    articles = []
    for article in response.json()["app_msg_list"]:
        title = article["title"]
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(article["create_time"]))
        link = re.findall('http://.*&chksm', article["link"])[0]
        articles.append(
            {
                "title": title,
                "create_time": create_time,
                "link": link
            }
        )
    return articles


def main():
    articles = []
    i = 0
    while True:
        url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={}&count=5&fakeid=&type=9&query=&token=1993527289&lang=zh_CN&f=json&ajax=1".format(i * 5)
        article = get_articles(url)
        if article:
            articles.extend(article)
        else:
            break
        i += 1
        print('正在抓取第%s页的数据，目前总共爬取了%s篇文章' % (i, len(articles)))
        time.sleep(0.5)

    # 数据保存为csv格式
    print('正在保存数据...')
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\gmbjzg\software\wkhtmltopdf\wkhtmltopdf.exe')
    with open('哥们并肩走过公众号.csv', 'a', encoding='utf_8_sig', newline='') as fp:
        csv_writer = csv.DictWriter(fp, fieldnames=['title', 'create_time', 'link'])
        csv_writer.writeheader()
        for article in articles:
            print('正在写入%s' % article['title'])
            csv_writer.writerow(article)
            try:
                pdfkit.from_url(article['link'], '%s.pdf' % article['title'], configuration=config)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()


