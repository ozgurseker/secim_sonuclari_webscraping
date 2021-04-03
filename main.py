import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs 
from tabulate import tabulate

il = "adiyaman-2"

url = "https://www.haberturk.com/secim/secim2014/yerel-secim/sehir/adiyaman-2"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = bs(page_html, "html.parser")

il_links = list()
iller = list()
ilceler = list()
ilce_links = list()

forilces = page_soup.findAll("ul", {"class": "bottom-list hover-select"})
for k in range(len(forilces[1].findAll("li"))):
    s = str(forilces[1].findAll("li")[k].a)
    i = s.find("\"")
    s = s[i+1:]
    j = s.find("\"")
    il_links.append(s[:j])
    iller.append(s[35:j])


for k in range(len(iller)):
    il = iller[k]
    url = "https://www.haberturk.com/secim/secim2014/yerel-secim/sehir/" + il
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = bs(page_html, "html.parser")
        

    acilan_sandik_oran = page_soup.findAll("b", {"class": "genel_durum_acilan_sandik_oran"})
    s = str(acilan_sandik_oran[0])
    i = s.find("%")
    j = i-5
    open_rate = s[j:i]

    results = page_soup.findAll("table", {"class": "gray red tables buyuksehir"})

    res = results[0].tbody.findAll("tr")
    print ("\t" + il + " Merkez") 
    sonuclar = list()
    for i in range(len(res) - 1):
        sonuc = list()
        r = res[i+1]
        s = r.text.strip()
        j = s.find("\t")
        aday = s[:j]
        sonuc.append(aday)
        s = s[j:]
        s = s.strip()
        j = s.find("\n")
        parti = s[:j]
        oran = s[j:].strip()
        sonuc.append(parti)
        sonuc.append(oran)
        sonuclar.append(sonuc)
    
    

    table = tabulate(sonuclar, headers= ["Aday", "Parti", "Oran"])
    print (table)

    forilces = page_soup.findAll("ul", {"class": "bottom-list hover-select"})
    ilcelist = forilces[0].findAll("li")
    ilce1 = list()
    ilce2 = list()
    for ilce in ilcelist:
        ilce1.append(ilce.text.strip()) 
        s = str(ilce.a)
        i = s.find(">")
        s = s[9:i-1]
        ilce2.append(s)
    ilceler.append(ilce1)
    ilce_links.append(ilce2)



