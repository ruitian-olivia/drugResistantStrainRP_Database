import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://ardb.cbcb.umd.edu/browsespecies.shtml")
soup = BeautifulSoup(r.text)
data = soup.select("ul > ul > ul > ul > ul > ul > li")

species = []
url = []
for i in data:
    name = i.find("a").contents[0][:-1]
    href = str(i).split("\"")[1]
    species.append(name)
    url.append(href)
hotDF = pd.DataFrame()
hotDF['Species'] = species
hotDF['URL'] = url
hotDF.to_csv('./drug_resistance.csv', index=False)