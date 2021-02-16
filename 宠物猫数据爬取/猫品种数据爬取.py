
import requests
from lxml import etree
import re


def get_detail_url():
    """
    获取所有猫品种详情链接
    :return: 所有猫品种详情链接 list
    """
    url = 'http://www.maomijiaoyi.com/index.php?/pinzhongdaquan_1.html'

    resp = requests.get(url)

    # 1、解析为html文档
    html = etree.HTML(resp.text)

    # 2、提取所有url详情链接
    all_a = html.xpath('//div[@class="pinzhong_left"]/a')

    urls = []
    for a in all_a:
        full_url = 'http://www.maomijiaoyi.com' + a.xpath('@href')[0]
        urls.append(full_url)

    return urls


def get_info(obj, i=1):
    """
    封装xpath方法
    :return:
    """
    if obj.xpath('div')[i].xpath('text()'):
        return re.sub(r'\s', '', "".join(obj.xpath('div')[i].xpath('text()')))
        # return obj.xpath('div')[i].xpath('text()')[0].strip()
    else:
        return ''


def get_info_love(obj, i=2):
    """
    定义一个偏函数，用于数据处理
    :return:
    """
    return get_info(obj, i)


def deal_data(obj):
    """
    详细信息数据处理
    :param obj:
    :return:
    """

    return re.sub(r'\s', '', "".join(obj.xpath('.//p//text()')))


def get_details(url):
    """
    获取猫品种的详细信息
    :return:
    """
    # url = 'http://www.maomijiaoyi.com/index.php?/pinzhong_37.html'

    resp = requests.get(url)

    # 1、解析为html文档
    html = etree.HTML(resp.text)

    # 2、提取信息
    # 2.1提取基本信息
    infos = html.xpath('//div[@class="right"]/div[@class="details"]/div')
    res_infos = []
    for i in range(len(infos)):
        res_infos.append(get_info(infos[i]))

    # 2.2提取属性信息
    attrs = html.xpath('//div[@class="right"]/div[@class="shuxing"]/div')
    res_attrs = []
    for i in range(len(attrs)):
        res_attrs.append(get_info_love(attrs[i]))

    # 2.3获取详细信息
    contents = html.xpath('//div[@class="content"]/div[@class="property_list"]/div')
    res_contents = []
    for i in range(len(contents)):
        res_contents.append(deal_data(contents[i]))

    # 2.4获取图片url
    imgs = html.xpath('//div[@class="left"]/div[@class="big_img"]//img/@src')
    img_url = []
    for img in imgs:
        full_url = 'http://www.maomijiaoyi.com' + img
        img_url.append(full_url)

    # 3、构建完整数据结构
    full_info = {
        'base_info': {
            'name': res_infos[0],
            'sub_name': res_infos[1],
            'ancestor': res_infos[2],
            'area': res_infos[3],
            'origin': res_infos[4],
            'shape': res_infos[5],
            'source_use': res_infos[6],
            'today_use': res_infos[7],
            'height': res_infos[8],
            'group': res_infos[9],
            'weight': res_infos[10],
            'age': res_infos[11]
        },
        'attr_info': {
            'introduce': res_attrs[0],
            'hair': res_attrs[1],
            'color': res_attrs[2],
            'header': res_attrs[3],
            'eye': res_attrs[4],
            'ear': res_attrs[5],
            'tail': res_attrs[6],
            'chest': res_attrs[7],
            'neck': res_attrs[8],
            'foreleg': res_attrs[9],
            'hindleg': res_attrs[10],
        },
        'detail_info': {
            'message': res_contents[0],
            'fci': res_contents[1],
            'personality': res_contents[2],
            'life': res_contents[3],
            'specialty': res_contents[4],
            'feed': res_contents[5],
            'select': res_contents[6],
        },
        'img_url': img_url
    }
    return full_info


def main():
    urls = get_detail_url()
    for url in urls:
        print(get_details(url))


if __name__ == '__main__':
    main()

