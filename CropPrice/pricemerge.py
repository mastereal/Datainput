import os
import re
import pandas as pd
from pandas import DataFrame, Series
from collections import Counter

filelist=os.listdir("./Afterclean/")
typelist=[]
for filename in filelist:
    check=re.match("([A-Z][A-Z])_([A-Z][A-Z0-9])",filename)
    typecode=check.group(2)
    typelist.append(typecode)
count=Counter(typelist)
print(count)

ProMatch=["AH","JS","ZJ","JX"]
TypeMatch=["BO","R1","WA","WO"]
