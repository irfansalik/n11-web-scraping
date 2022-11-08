from pyexpat import model
from re import T
import requests
from bs4 import BeautifulSoup
import pprint


pp=pprint.PrettyPrinter(indent=4)


marka=["Lenovo","Dell","Acer"]
liste=[]
x=0
while x<3:


    i=1

    while i<2:


        lenovo = requests.get(f"https://www.n11.com/bilgisayar/dizustu-bilgisayar?m={marka[x]}&pg={i}").content

        soup=BeautifulSoup(lenovo,"html.parser")
        list = soup.find_all("li",{"class":"column"},limit=200)

       
        for li in list:
            


            Productname = li.h3.text
            link = li.a.get("href")
            
            price = li.find("div",{"class":"priceContainer"}).find("span",{"class":"newPrice cPoint priceEventClick"}).text.strip()
            
            # print(Productname)
            liste.append(str(Productname)+" "+ link+" "+price)
         
        i+=1
    x+=1


liste2=[]
son={}
for i in liste:
    liste2.append(i.split()) #bilgisayarın herkelimesini parçaladık
kacBil=len(liste2) #kaç bilgisayar çektik



from asyncio.windows_events import NULL


class biln11:
    def __init__ (self, marka=NULL, model=NULL, islemci=NULL, ram=NULL,
         bellek=NULL, ekranB=NULL, link=NULL, fiyat=NULL):
        self.marka=marka
        self.model=model
        self.islemci=islemci
        self.ram=ram
        self.bellek=bellek
        self.ekranB=ekranB
        self.link=link
        self.fiyat=fiyat
                
n11bil=[]
Tekranb=0           

for j in range(kacBil):
    a=0
    isb=1
    gbf=1
    for i in range(len(liste2[j])):
        if "\"" in liste2[j][i]:
            Tekranb=i
    for i in range(len(liste2[j])): #bir bilgisayarın kelimeleri
        if gbf:
            if "GB" in liste2[j][i]:
                
                Tram=a
                gbf=0


        if isb :
            if ("i3-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("i5-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("i7-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("R3-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("R5-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("R7-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif ("R9-") in liste2[j][i]:
                isb=0
                Tislemci=a
            elif "Ryzen" in liste2[j][i]:
                isb=0
                Tislemci=a+2
            else:
                Tislemci=0
            
        a+=1
        
            
            

    n11bil.append(biln11(marka=liste2[j][0], model=liste2[j][1]+" "+liste2[j][2], 
    islemci=liste2[j][Tislemci], ram=liste2[j][Tram-1]+" "+liste2[j][Tram], ekranB=liste2[j][Tekranb],
     bellek=liste2[j][Tram+1]+" "+liste2[j][Tram+2]+" "+liste2[j][Tram+3],
     link=liste2[j][-3], fiyat=liste2[j][-2]+liste2[j][-1],))
    
    
        

pp.pprint(liste)