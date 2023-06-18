import folium
import pandas #pandas modulü dosyalarımıza ulaşmamızı sağlıyor
import xlrd

veri = pandas.read_excel("tr-cities.xlsx")

harita=folium.Map(location=(41,29), tiles="CartoDB positron")

enlemler=list(veri["Enlem"])
boylamlar=list(veri["Boylam"])
isimler=list(veri["City"])

for i,j,k in zip(enlemler,boylamlar,isimler):
    harita.add_child(folium.Marker(location=(i,j), icon=folium.Icon(color="blue"), popup=k))


harita.save("Deneme.html")