import requests
import json


def get_data(tag='最新'):
	"""
	获取100条豆瓣电影数据
	:param tag: str 电影类型 最新/热门/经典
	:return:
	"""

	url = "https://movie.douban.com/j/search_subjects?type=movie&tag={}&page_limit=100&page_start=0".format(tag)

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
	}

	resp = requests.get(url, headers=headers)

	return resp.json()


def handel_data(movies):
	"""
	获取评分大于8.0的电影
	:param movies: dict
	:return: dict
	"""
	temp = []
	for movie in movies:
		if float(movie['rate']) > 8.0:
			print(movie)
			temp.append(movie)

	return {
		'subjects': temp
	}


def save_data(dit, filename):
	"""
	保存为json数据格式
	:param dit: dict
	:return: None
	"""
	full_filebname = filename + '.json'
	with open(full_filebname, 'w', encoding='utf-8') as fp:
		json.dump(dit, fp=fp, indent=4, ensure_ascii=False)


def main():
	# 1.获取所有电影数据
	movies = get_data()
	# 2.获取评分大于8.0的电影数据
	new_movies = handel_data(movies['subjects'])
	# 3.保存数据
	save_data(movies, filename='最新电影')
	save_data(new_movies, filename='高分电影')


if __name__ == '__main__':
	main()

	