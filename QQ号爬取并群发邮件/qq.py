"""
@author: 逍遥子
@weixin: 哥们并肩走过
@software: PyCharm 
@time: 2021-02-09 17:12 
@description：QQ号爬取并群发邮件
"""

import requests
import json
from sendEamil import send_email

def get_data(st):
    """
    获取数据
    :return:
    """

    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'

    headers = {
        "cookie": "_qpsvr_localtk=0.8487238345830157; RK=n0qspWrvWN; ptcz=5b9c4c61b9b5ad710bb7898ce31364000fe55f159b323789c81e85870a0807e3; p_uin=o1924086038; traceid=cf9b079a5b; uin=o1924086038; skey=@IuQIqxDwv; pt4_token=hEORO*KJYw0sVaVn2JmpaTFhFFrHj0hcAhEY5ZKbPkw_; p_skey=ADxjAos4TkCZq5hexmC*T9ud9rY5ud9anAfsdP2KJuc_",
        "origin": "https://qun.qq.com",
        "referer": "https://qun.qq.com/member.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
    }

    data = {
        "gc": "296161017",
        "st": st,
        "end": str(int(st) + 40),
        "sort": "0",
        "bkn": "2006600215"
    }

    res = requests.post(url, headers=headers, data=data)

    content = res.content.decode(res.encoding)

    # print(content)

    return content


def parse_data(content):
    """
    解析数据
    :return:
    """
    content = json.loads(content)

    users = []

    if content.get('mems'):
        for user in content['mems']:
            if user['g'] == '0':
                user['sex'] = '男'
            elif user['g'] == '1':
                user['sex'] = '女'
            else:
                user['sex'] = '未知'
            users.append({
                'name': user['card'].replace('&nbsp;', ''),
                'age': user['qage'],
                'sex': user['sex'],
                'number': user['uin']
            })

    print(users)

    return users


def write_to_file(data):
    """
    写入文件
    :return:
    """
    with open('qq.txt', 'a', encoding='utf-8') as f:
        f.write(data)


def distribution_email(email, content):
    """
    群发邮件
    :param email: 邮箱地址 str
    :param content: 发送内容 str
    :return:
    """
    send_email(email, content)


def main():
    all_user = []
    i = 0
    while True:
        content = get_data(i)
        res = parse_data(content)
        if res:
            all_user.extend(res)
        else:
            break
        i += 41
    print('总共抓取了%s条数据' % len(all_user))

    write_to_file(str(all_user))

    # for user in all_user:
    #     email = str(user['number']) + '@qq.com'
    #     content = user['name']
    #     distribution_email(email, content)


if __name__ == '__main__':
    main()

