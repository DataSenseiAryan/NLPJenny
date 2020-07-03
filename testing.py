


from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error

def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return fetched_text


text = 'maki'
try:
	message = get_text(text)
				
except BaseException as e:
	print(e)
					
