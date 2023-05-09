from bs4 import BeautifulSoup
import requests
import pprint

web_address = requests.get('https://byjusexamprep.com/current-affairs#daily-current-affairs')

soup = BeautifulSoup(web_address.text,'html.parser')

def current_link_grabber():
	current_affairs_link_save = []
	current_affairs_today = soup.select('#__next > section > section > div.fwc-2.flex.flex-grow-1.justify-between.mt3 > main > div.custom-html-style.mb3.ph3.ph0-l.overflow-x-visible > ul:nth-child(12) li a')
	for i in current_affairs_today:
		current_affairs_link = i.attrs
		current_affairs_link_save.append(current_affairs_link['href'])
	return current_affairs_link_save

def current_date():
	date = []
	for i in range(len(current_link_grabber())):
		d = current_link_grabber()[i].split('-')[-2:-5:-1]
		date.append(d)
	return date

def current_link_opener():
	news_title = []
	news_describe = []
	for i in current_link_grabber():
		link_opener = requests.get(i)
		soup = BeautifulSoup(link_opener.text, 'html.parser')
		
		title_list = soup.select('#__next > section > section > div > div.flex-row-l.flex-column.fixed-width-container.flex.flex-grow-1.justify-between.mt2 > div.post_articleMain__1KWsN.mr4-l.mr0.exam-category-main > div.relative.flex.flex-column.w-100 > div.relative.transition-all > div > div.custom-html-style.mb3.ph3.ph0-l.overflow-x-visible.new-html-styles.post-body.article-content.overflow-y-hidden.ph3-3.roboto > h3')
		for j in range(len(title_list)):
			title = title_list[j].getText()
			news_title.append(title)
		

		full_news_link = soup.select('#__next > section > section > div > div.flex-row-l.flex-column.fixed-width-container.flex.flex-grow-1.justify-between.mt2 > div.post_articleMain__1KWsN.mr4-l.mr0.exam-category-main > div.relative.flex.flex-column.w-100 > div.relative.transition-all > div > div.custom-html-style.mb3.ph3.ph0-l.overflow-x-visible.new-html-styles.post-body.article-content.overflow-y-hidden.ph3-3.roboto > ul')
		for z in range(len(full_news_link)):
			full_news = full_news_link[z].getText()
			news_describe.append(full_news)
		
	current_affairs = zip(news_title, news_describe)
	return current_affairs
