import requests,os,traceback, re
pairs=[('licsub','116','17395'),('overview','113','17385'),('planning','600','17465'),('pensions','733','17451'),('corp','115','17474')]
urls=['https://r.jina.ai/https://moderngov.lambeth.gov.uk/ieListDocuments.aspx?CId='+c+'%26MId='+m for _,c,m in pairs]
s=requests.Session();os.makedirs('dump',exist_ok=True)
for (name,c,m),u in zip(pairs,urls):
 try:
  r=s.get(u,timeout=120,headers={'User-Agent':'Mozilla/5.0','Accept':'text/plain'})
  print('OK',name,r.status_code,len(r.content),r.url); open('dump/'+name+'.txt','wb').write(r.content)
 except Exception as e:
  print('ERR',name,e); open('dump/'+name+'.txt','w').write(str(e))
