import sys
from requests_html import HTMLSession
from bs4 import BeautifulSoup
for i in range(1000,2000):
    try:
        session=HTMLSession()
        url=f'https://novelfull.com/martial-god-asura/chapter-{i}.html'
        page=session.get(url)
        soup=BeautifulSoup(page.text,features='lxml')
        r=soup.find(id='chapter-content')
        r = r.text.replace('.','.\n')
        file=open(f'D://MGA//chapter-{i}.txt','w')
        file.write(r)
        file.close()
    except:
        print(f'error in chapter {i}')
        continue