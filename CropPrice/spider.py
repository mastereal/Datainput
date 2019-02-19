import re
import urllib
from urllib import request

def download(AreaIDSelect1,AreaNextSelect1,Grain1,SWYear="1736",SWmonth="1",EWYear="1911",EWMonth="12"):
    url="http://mhdb.mh.sinica.edu.tw/foodprice/excel.php?SWYear="+SWYear+"&SWMonth="+SWmonth+"&EWYear="+EWYear+"&EWMonth="+EWMonth+"&AreaIDSelect1="+AreaIDSelect1+"&AreaNextSelect1="+AreaNextSelect1+"&AreaIDSelect2=ZL&AreaNextSelect2=all&Grain1="+Grain1+"&Grain2=WO&chart=1&ifContrast=none"
    filename=AreaIDSelect1+"_"+AreaNextSelect1+"_"+Grain1+".csv"
    urllib.request.urlretrieve(url,filename)
matchlist=["JS","AH","ZJ","JX"]
Grainlist=[]
with open("grainlist.txt",'r',encoding="utf-8-sig") as f:
    linelist = f.readlines()
for str_grain in linelist:
    grainmatch=re.search(r"(?:\")([A-Z][A-Z0-9])(?:\")",str_grain)
    graintype=grainmatch.group(1)
    print(graintype)
    Grainlist.append(graintype)
for pro in matchlist:
    for grain in Grainlist:
        download(pro,"all",grain)