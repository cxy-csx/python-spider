import requests
import os
import xml.etree.ElementTree as ET
from io import StringIO


# 配置
key = "5f63b9602b5b0fb228aaa3963c5f9e84"
book_catalog_url = "http://apis.juhe.cn/goodbook/catalog?key={}&dtype=xml".format(key)
catalog_cache_file_path = "cache/catalog.xml"


def get_book_catalog():
    # 图书分类数据请求
    if not os.path.exists(catalog_cache_file_path):
        print('网络请求...')
        resp = requests.get(book_catalog_url)
        with open(catalog_cache_file_path, 'w', encoding='utf-8') as fp:
            fp.write(resp.text)


def parse_data():
    # xml格式数据解析
    obj = ET.parse(catalog_cache_file_path)  # xml.etree.ElementTree.ElementTree
    catalogs = obj.find("result").findall("item")
    catalog_infos = []
    for catalog in catalogs:
        catalog_id = catalog.find("id").text
        catalog_text = catalog.find("catalog").text
        catalog_infos.append({
            'catalog_id': catalog_id,
            'catalog_title': catalog_text
        })

    return catalog_infos


def get_book_detail(catalog_id):
    # 图书详情数据请求
    book_detail_url = "http://apis.juhe.cn/goodbook/query?key={}&catalog_id={}&pn=1&rn=15&dtype=xml".format(key, catalog_id)
    resp = requests.get(book_detail_url)
    # 构建节点树对象
    obj = ET.parse(StringIO(resp.text))
    books = obj.find("result").find("data").findall("item")
    return books


def generate_book_detail_html(books):

    words = ["title", "img", "sub1", "catalog", "tags", "bytime", "sub2"]

    for book in books:
        title = book.find("title").text
        with open("book_temp/book_detail_temp.html", "r", encoding="utf-8") as temp_fp, open(
                "book_generate_dir/{}.html".format(title), "w", encoding="utf-8") as detail_fp:
            book_detail_str = temp_fp.read()
            for word in words:
                book_detail_str = book_detail_str.replace("{{" + word + "}}", book.find(word).text)
            # 详情页面生成并写入
            detail_fp.write(book_detail_str)


def generate_book_catalog_html(books):

    book_box = """
        <div class="box">
            <a href="{}">
                <img src="{}" alt="">
                <h4>{}</h4>
            </a>
        </div>
    """
    all_box = ""
    for book in books:
        title = book.find("title").text
        link = "{}.html".format(title)
        img_url = book.find("img").text
        all_box += book_box.format(link, img_url, title)

    with open("book_temp/book_catalog_temp.html", "r", encoding="utf-8") as catalog_fp:
        res = catalog_fp.read().replace("{{content_list}}", all_box)
        # 生成列表详情页面index.html
        with open("book_generate_dir/index.html", "w", encoding="utf-8") as f:
            f.write(res)


def main():
    # 1.获取图书分类信息
    get_book_catalog()
    # 2.解析xml数据,获取图书id
    catalog_infos = parse_data()
    for catalog_info in catalog_infos:
        print(catalog_info['catalog_title'], catalog_info['catalog_id'])
    catalog_id = input('请输入图书id: ')
    # 3.获取图书详情数据
    books = get_book_detail(catalog_id)
    # 5.生成图书列表页面
    generate_book_catalog_html(books)
    # 4.生成图书详情页面
    generate_book_detail_html(books)


if __name__ == '__main__':
    main()


















