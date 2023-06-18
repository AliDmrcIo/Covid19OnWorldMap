import pandas
import folium #folium kütüphanesi aslında javascript html ve css dillerinin python'a çevrildiği kütüphanedir

veri=pandas.read_excel("world_coronavirus_cases.xlsx")
worldMap=folium.Map(tiles="Cartodb dark_matter")

enlemler=list(veri["Enlem"])
boylamlar=list(veri["Boylam"])
vaka=list(veri["Toplam Vaka"])
vefat=list(veri["Vefat Edenler"])
aktifler=list(veri["Aktif Vakalar"])
testler=list(veri["Toplam Test"])
nufus=list(veri["Nüfus"])


vakaSayisiHaritasi=folium.FeatureGroup(name="Toplam Vaka Sayisi Haritasi")
#bu sağ üstteki o kutucuğun içerisindeki katmanların açılmasını sağlıyor
olumOraniHaritasi=folium.FeatureGroup(name="Olum orani haritasi")
aktifVakaHaritasi=folium.FeatureGroup(name="Aktif Vaka Haritasi")
testOraniHaritasi=folium.FeatureGroup(name="Test Oranı Haritasi")
nufusDagilimHaritasi=folium.FeatureGroup(name="Nufus dagilim haritasi")


def vakaSayisiRenk(vaka):
    if int(vaka)<100000:
        return "green"
    elif int(vaka)<300000:
        return "white"
    elif int(vaka)<750000:
        return "orange"
    else:
        return "red"

def vakaSayisiRadius(vaka):
    if int(vaka) < 100000:
        return 40000
    elif int(vaka) < 300000:
        return 100000
    elif int(vaka) < 750000:
        return 200000
    else:
        return 400000

def olumOraniRadius(vaka,vefat):
    if (vaka/vefat)*100 < 2.5:
        return 40000
    elif (vaka/vefat)*100 < 5:
        return 100000
    elif (vaka/vefat)*100 < 7.5:
        return 200000
    else:
        return 400000

def olumOraniRenk(vaka,vefat):
    if (vaka/vefat)*100 < 2.5:
        return "green"
    elif (vaka/vefat)*100 < 5:
        return "white"
    elif (vaka/vefat)*100 < 7.5:
        return "orange"
    else:
        return "red"


def aktifVakaRadius(aktifVaka):
    if int(aktifVaka) < 100000:
        return 40000
    elif int(aktifVaka) < 300000:
        return 100000
    elif int(aktifVaka) < 750000:
        return 200000
    else:
        return 400000

def aktifVakaRenk(aktifVaka):
    if int(aktifVaka)<100000:
        return "green"
    elif int(aktifVaka)<300000:
        return "white"
    elif int(aktifVaka)<750000:
        return "orange"
    else:
        return "red"

def testOraniRadius(nufusSayisi,testSayisi):
    if (testSayisi/nufusSayisi)*100 < 2.5:
        return 40000
    elif (testSayisi/nufusSayisi)*100 < 5:
        return 100000
    elif (testSayisi/nufusSayisi)*100 < 7.5:
        return 200000
    else:
        return 400000

def testOraniRenk(nufusSayisi,testSayisi):
    if (testSayisi/nufusSayisi)*100 < 2.5:
        return "green"
    elif (testSayisi/nufusSayisi)*100 < 5:
        return "white"
    elif (testSayisi/nufusSayisi)*100 < 7.5:
        return "orange"
    else:
        return "red"


for i,j,k in zip(enlemler,boylamlar,vaka):
    vakaSayisiHaritasi.add_child(folium.Circle(location=(i,j), radius=vakaSayisiRadius(k),
                                     color=vakaSayisiRenk(k),
                                     fill_color=vakaSayisiRenk(k),
                                     fill_opacity=0.3))

for i,j,k,z in zip(enlemler,boylamlar,vaka,vefat):
    olumOraniHaritasi.add_child(folium.Circle(location=(i,j), radius=olumOraniRadius(z,k),
                                               color=olumOraniRenk(z,k),
                                               fill_color=olumOraniRenk(z,k),fill_opacity=0.3))


for i,j,k in zip(enlemler,boylamlar,aktifler):
    aktifVakaHaritasi.add_child(folium.Circle(location=(i,j), radius=aktifVakaRadius(k),
                                               color=aktifVakaRenk(k),
                                               fill_color=aktifVakaRenk(k),fill_opacity=0.3))


for i,j,k,z in zip(enlemler,boylamlar,testler,nufus):
    testOraniHaritasi.add_child(folium.Circle(location=(i,j), radius=testOraniRadius(z,k),
                                               color=testOraniRenk(z,k),
                                               fill_color=testOraniRenk(z,k),fill_opacity=0.3))




nufusDagilimHaritasi.add_child(folium.GeoJson(data=(open("world.json","r", encoding="utf-8-sig").read()),
                            style_function= lambda x : {
                            'fillColor':'green' if x["properties"]["POP2005"]<20000000
                            else 'white'  if 20000000 <= x["properties"]["POP2005"]<=50000000
                            else 'orange' if 50000000 <= x["properties"]["POP2005"]<=100000000
                            else 'red'}))
#bunu yaparak ülkelerin sınırlarını işaretlemiş ve ülkeleri de nufuslarına göre boyamış olduk
#folium kütüphanesinin geojson dosyalarının üzerinde estetik değişiklikler yapmamızı sağlayan modülü GeoJson
#ancak bunu kullanmak için elimizde sadece json uzantılı dosya olması yetmez, geojson dosyamız olmalı
#folium.GeoJson(open) yaparak geojson dosyamızı açtık ve r ile readable yaptık onu. .read() yapmazsak çalışmazdı
#lambda ile değer(x) alan style_function ile haritamızı renklendirdik. fillcolor dediğimizde,
#iç rengini şu şartla(if x["properties"]["POP2005"]<20000000)) boya demiş oldu
#örneğin x(ülke) green yap ancak ülke nüfusu 20m'dan az ise.
#

worldMap.add_child(vakaSayisiHaritasi) #bu, vakaSayisiHaritasi değişkenini worldmap'in alt kümesi yapıyor gibi
worldMap.add_child(olumOraniHaritasi)
worldMap.add_child(aktifVakaHaritasi)
worldMap.add_child(testOraniHaritasi)
worldMap.add_child(nufusDagilimHaritasi)

worldMap.add_child(folium.LayerControl()) #bu sağ üstteki o kutucuğun açılmasını sağlıyor.1 tane yazılması enough


worldMap.save("worldMap.html")
