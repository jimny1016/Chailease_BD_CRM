import urllib.request,urllib.error
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
file=urllib.request.urlopen(quote_page)
data=file.read()
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())
print('hello world');