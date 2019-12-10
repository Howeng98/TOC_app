import requests
from bs4 import BeautifulSoup


#tag = "#b5#b6#b7#b8#hb#b9#ba#bb"
res = requests.get("https://www.dcard.tw/f/food")
soup = BeautifulSoup(res.text, "html.parser")

#print("-----------------------------")
value = soup.find_all('a',class_='PostEntry_root_V6g0rd')
#value = value.find_all(class_='PostEntry_root_V6g0rd')
print(value)
for v in value:
    print(v.text)
    print("\n")
    
