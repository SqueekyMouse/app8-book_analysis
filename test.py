import re
from nltk.sentiment import SentimentIntensityAnalyzer

with open('miracle_in_the_andes.txt','r') as file:
    book=file.read()
# pattern=re.compile('Chapter [0-9]+')
# search_res=re.findall(pattern,book)
# print(search_res)
pattern=re.compile('[a-zA-Z]+')
findings=re.findall(pattern,book.lower())
print(len(findings))

d={}
for word in findings:
    if word not in d.keys():
        d[word]=0
    else:
        d[word]+=1

# maxval=sorted(d.values(),reverse=True)[0]
list_of_d=[(val,key) for (key,val) in d.items()]
print(sorted(list_of_d,reverse=True)[:5])


