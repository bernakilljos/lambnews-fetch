import requests,os,time
files={x:'https://r.jina.ai/https://moderngov.lambeth.gov.uk/mgAi.aspx?ID='+id for x,id in [('lic_ar_min','67121'),('lic_lav_min','67122'),('lic_aq_min','67123'),('osc_budget_min','67071'),('osc_dev_min','67072')]}
s=requests.Session(); os.makedirs('dump2',exist_ok=True)
for name,u in files.items():
 try:r=s.get(u,timeout=180); print(name,r.status_code,len(r.content)); open('dump2/'+name+'.txt','wb').write(r.content)
 except Exception as e: print(name,e);open('dump2/'+name+'.txt','w').write(str(e))
 time.sleep(3)
