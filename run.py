import requests,os,urllib.parse,time
files={
'osc_savings':'https://moderngov.lambeth.gov.uk/documents/s173488/OSC%20Savings%20Cover%20Report%20-%2026%20January%202026.pdf',
'osc_mtfs':'https://moderngov.lambeth.gov.uk/documents/s173489/MTFS2Feb%20Final.pdf',
'osc_append1':'https://moderngov.lambeth.gov.uk/documents/s173490/Appendix%201%20-%20Saving%20Proposals%202026-30.pdf',
'osc_engage':'https://moderngov.lambeth.gov.uk/documents/s173491/Appendix%202%20-%20Budget%20Engagement%20Report.pdf',
'developer':'https://moderngov.lambeth.gov.uk/documents/s173205/FINAL%20OSC%20Developer%20Contributions%20CIL%20NCIL%20and%20s106%20FY25-26%20-%2026.01.26.pdf',
'plan_clapham':'https://moderngov.lambeth.gov.uk/documents/s173129/346%20Clapham%20Road%20ref%2024-01346-FUL%20PAC%20Report.pdf',
'plan_sauna':'https://moderngov.lambeth.gov.uk/documents/s173124/Clapham%20Sauna%202025%20PAC%20final_.pdf',
'plan_thorn':'https://moderngov.lambeth.gov.uk/documents/s173125/2%20Thornlaw%20Road%20ref.%202402054FUL%20-%20PAC%20report%20FINAL.pdf',
'plan_chapel':'https://moderngov.lambeth.gov.uk/documents/s173142/PAC%20Land%20off%20Chapel%20Road%202502646FUL%20FINAL.pdf',
'plan_cleeve':'https://moderngov.lambeth.gov.uk/documents/s173128/PAC%20report%20-%201%20Cleevedale%20Place%20WTU.1%202402311FUL.pdf',
'lic_ar':'https://moderngov.lambeth.gov.uk/documents/s173228/Cleared%20Report%20-%20AR%20Norwood%20Food%20and%20Wine.pdf',
'lic_lav':'https://moderngov.lambeth.gov.uk/documents/s173233/La%20Vuelta%20-%20Committee_Report_2025.pdf',
'lic_aq':'https://moderngov.lambeth.gov.uk/documents/s173237/Aquarium%20cleard%20report%20-%20Copy.pdf',
'corp_stat':'https://moderngov.lambeth.gov.uk/documents/s173338/Councils%20Response%20to%20Statutory%20Recommendations.pdf',
'corp_audit':'https://moderngov.lambeth.gov.uk/documents/s173331/Management%20Update%20on%20Limited%20Assurance%20Reports.pdf',
'corp_tax':'https://moderngov.lambeth.gov.uk/documents/s173347/Tax%20Base%20Report%202026-27.pdf',
'corp_fraud':'https://moderngov.lambeth.gov.uk/documents/s173345/Counter%20Fraud%20Progress%20Report%202025-26.pdf'
}
s=requests.Session(); os.makedirs('dump',exist_ok=True)
for name,url in files.items():
 target='https://r.jina.ai/'+url
 try:
  r=s.get(target,timeout=150,headers={'User-Agent':'curl/8.1','Accept':'text/plain'})
  print('OK',name,r.status_code,len(r.content),target); open('dump/'+name+'.txt','wb').write(r.content)
 except Exception as e:
  print('ERR',name,e); open('dump/'+name+'.txt','w').write(str(e))
 time.sleep(2)
