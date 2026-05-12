import requests,os
from bs4 import BeautifulSoup
base='https://moderngov.lambeth.gov.uk'
s=requests.Session();
urls=['/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026','/mgCalendarMonthView.aspx?GL=1&bcr=1&month=1&year=2026','/mgCalendarMonthView.aspx?bcr=1&date=2026-01-28','/mgCalendarMonthView.aspx?GL=1&bcr=1']
os.makedirs('dump',exist_ok=True)
for i,u in enumerate(urls):
 r=s.get(base+u); print(u,r.status_code,len(r.content),r.url)
 open('dump/cal%d.html'%i,'wb').write(r.content)
