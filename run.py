import requests,os,traceback
urls=['https://r.jina.ai/https://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1%26bcr=1%26M=1%26Y=2026',
'https://r.jina.ai/http://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1%26bcr=1%26M=1%26Y=2026',
'http://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026',
'https://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026',
'https://r.jina.ai/https://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026',
'https://r.jina.ai/http://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026',
'https://r.jina.ai/https://moderngov.lambeth.gov.uk/mgCalendarMonthView.aspx?GL=1%26bcr=1%26date=2026-01-28']
s=requests.Session();os.makedirs('dump',exist_ok=True)
for i,u in enumerate(urls):
 try:
  r=s.get(u,timeout=30,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36','Accept':'text/html,application/xhtml+xml'})
  print('OK',u,r.status_code,len(r.content),r.url); open('dump/r%d.txt'%i,'wb').write(r.content)
 except Exception as e:
  print('ERR',u,e); open('dump/r%d.txt'%i,'w').write(str(e))
