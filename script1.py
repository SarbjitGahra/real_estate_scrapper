import requests
from bs4 import BeautifulSoup
import pandas
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
l =[]
for page in range (0, 30 , 10):
    url =base_url+str(page)+".html"
    #req = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
    req =requests.get(url)
    req_content= req.content
    soup = BeautifulSoup(req_content, "html.parser")
    print (req)
    all=soup.findAll("div", {"class" :"propertyRow"})
    for item in all:
        d={}
        try :
            d["price"] =item.find("h4", {"class": "propPrice"}).text.replace("\n","").replace(" ","")
            d["Addresse"] =item.findAll("span",{"class": "propAddressCollapse"})[0].text
            d["neighbhourhood"] =item.findAll("span",{"class": "propAddressCollapse"})[1].text            
            d["Beds"] =item.find("span",{"class": "infoBed"}).find("b").text
            d["Bathrooms"] =item.find("span",{"class": "infoValueFullBath"}).find("b").text
            d["area"] =item.find("span",{"class": "infoSqFt"}).text
        except:
            pass
        l.append(d)
df=pandas.DataFrame(l)
print (df)
df.to_csv("output.csv")