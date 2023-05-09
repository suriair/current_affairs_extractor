from daily_current_affairs import current_link_opener

news = tuple(current_link_opener())


with open('/Users/surendar/Desktop/current_affairs.txt', 'w') as file:
	for i in range(len(news)):
	    file.write(f'{news[i][0]}.\n {news[i][1]}\n')

	file.close()
