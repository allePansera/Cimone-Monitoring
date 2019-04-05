import pzgram
import request
import urllib
import bs4 as bs
import datetime

contUsi = 0



bot = pzgram.Bot("821759300:AAFObxDxOpQkuhalssk39Pz1FHMFN5CWhPI")


class Telegram:
    def __init__(self,periodo,clima,temp,wind):

        self.temp = temp
        self.wind = wind
        self.clima = clima
        self.periodo = periodo
    def send(self):
        pzgram.Chat(bot, 693507806).send(self.periodo+"\n\n"+self.clima+"\n"+self.temp+"\n"+self.wind+"\n")


def sendLive():
    urllib.request.urlretrieve("https://www.cimonesci.it/cams/passo_lupo.jpg", "img.png")
    pzgram.Chat(bot, 693507806).send_photo("./img.png", caption="Passo del Lupo")

def Today():
    pzgram.Chat(bot, 693507806).send(datetime.date.today())

    headers = {}
    headers[
    "user-agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    url = "https://www.cimonesci.it/meteo/"
    req = urllib.request.Request(url, headers=headers)

    resp = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(resp, "lxml")
    find = soup.find("div", attrs={"id": "3-0"})
    day = find.find("table", attrs={"class":"contenitore-meteo"})


    data = day.find_all("tr")
    cont = 1

    lista = data[0]
    lista2 = data[1]
    lista3 = data[2]
    lista4 = data[6]
    periodoGiornata = lista.find_all("td")
    clima = lista2.find_all("td")
    temp = lista3.find_all("td")
    wind = lista4.find_all("td")
    ##bottoni che mostrano la foto attuale delle piste (sotto bottoni)
    ##scegliere la data di controllo
    while (cont < 5):
        periodo2 = periodoGiornata[cont].get_text().strip()

        clima2 ="CLIMA :::: " + clima[cont].get_text().strip()

        #urllib.request.urlretrieve(clima[cont].find("img", src = True)["src"] , "img.png")
        temp2 = "TEMPERATURA :::: " + temp[cont].get_text().strip()
        wind2 = "VENTO ::::: "+ wind[cont].get_text().strip()

        t = Telegram(periodo2, clima2, temp2, wind2)
        t.send()
        cont += 1

    print("I")

########################################################
def Today2():
    pzgram.Chat(bot, 693507806).send(datetime.date.today() + datetime.timedelta(days=1))
    headers = {}
    headers[
        "user-agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    url = "https://www.cimonesci.it/meteo/"

    req = urllib.request.Request(url, headers=headers)

    resp = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(resp, "lxml")
    find = soup.find("div", attrs={"id":"3-1"})
    day = find.find("table", attrs={"class": "contenitore-meteo"})

    data = day.find_all("tr")
    cont = 1

    lista = data[0]
    lista2 = data[1]
    lista3 = data[2]
    lista4 = data[6]
    periodoGiornata = lista.find_all("td")
    clima = lista2.find_all("td")
    temp = lista3.find_all("td")
    wind = lista4.find_all("td")
    ##bottoni che mostrano la foto attuale delle piste (sotto bottoni)
    ##scegliere la data di controllo
    while (cont < 5):
        periodo2 = periodoGiornata[cont].get_text().strip()

        clima2 = "CLIMA :::: " + clima[cont].get_text().strip()

        # urllib.request.urlretrieve(clima[cont].find("img", src = True)["src"] , "img.png")
        temp2 = "TEMPERATURA :::: " + temp[cont].get_text().strip()
        wind2 = "VENTO ::::: " + wind[cont].get_text().strip()

        t = Telegram(periodo2, clima2, temp2, wind2)
        t.send()
        cont += 1

    print("I")

########################################################
def Today3():
    pzgram.Chat(bot, 693507806).send(datetime.date.today() + datetime.timedelta(days=2))

    headers = {}
    headers[
        "user-agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    url = "https://www.cimonesci.it/meteo/"
    req = urllib.request.Request(url, headers=headers)

    resp = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(resp, "lxml")
    find = soup.find("div", attrs={"id": "3-2"})
    day = find.find("table", attrs={"class": "contenitore-meteo"})

    data = day.find_all("tr")
    cont = 1

    lista = data[0]
    lista2 = data[1]
    lista3 = data[2]
    lista4 = data[6]
    periodoGiornata = lista.find_all("td")
    clima = lista2.find_all("td")
    temp = lista3.find_all("td")
    wind = lista4.find_all("td")
    ##bottoni che mostrano la foto attuale delle piste (sotto bottoni)
    ##scegliere la data di controllo
    while (cont < 5):
        periodo2 = periodoGiornata[cont].get_text().strip()

        clima2 = "CLIMA :::: " + clima[cont].get_text().strip()

        # urllib.request.urlretrieve(clima[cont].find("img", src = True)["src"] , "img.png")
        temp2 = "TEMPERATURA :::: " + temp[cont].get_text().strip()
        wind2 = "VENTO ::::: " + wind[cont].get_text().strip()

        t = Telegram(periodo2, clima2, temp2, wind2)
        t.send()
        cont += 1

    print("I")

########################################################
def Today4():
    pzgram.Chat(bot, 693507806).send(datetime.date.today() + datetime.timedelta(days=3))
    headers = {}
    headers[
        "user-agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    url = "https://www.cimonesci.it/meteo/"
    req = urllib.request.Request(url, headers=headers)

    resp = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(resp, "lxml")
    find = soup.find("div", attrs={"id": "3-1"})
    day = find.find("table", attrs={"class": "contenitore-meteo"})

    data = day.find_all("tr")
    cont = 1

    lista = data[0]
    lista2 = data[1]
    lista3 = data[2]
    lista4 = data[6]
    periodoGiornata = lista.find_all("td")
    clima = lista2.find_all("td")
    temp = lista3.find_all("td")
    wind = lista4.find_all("td")
    ##bottoni che mostrano la foto attuale delle piste (sotto bottoni)
    ##scegliere la data di controllo
    while (cont < 5):
        periodo2 = periodoGiornata[cont].get_text().strip()

        clima2 = "CLIMA :::: " + clima[cont].get_text().strip()

        # urllib.request.urlretrieve(clima[cont].find("img", src = True)["src"] , "img.png")
        temp2 = "TEMPERATURA :::: " + temp[cont].get_text().strip()
        wind2 = "VENTO ::::: " + wind[cont].get_text().strip()

        t = Telegram(periodo2, clima2, temp2, wind2)
        t.send()
        cont += 1

    print("I")
###############################################################
def main():
    #definire che o si scegli di vedere i dati oppure si vogliono vedere le web cam


    button1 = pzgram.create_button("data1", data="#3-0")
    button2 = pzgram.create_button("data2", data="#3-1")
    button3 = pzgram.create_button("data3", data="#3-2")
    button4 = pzgram.create_button("data4", data="#3-3")
    buttonlive = pzgram.create_button("live", data="send")

    k = [[buttonlive,button1,button2, button3, button4]]

    keyboard = pzgram.create_inline(k)

    pzgram.Chat(bot, 693507806).send("Seleziona la data che ti interessa: ", reply_markup=keyboard)

    bot.set_query({"#3-0": Today, "#3-1": Today2, "#3-2": Today3, "#3-3": Today4, "send": sendLive})


bot.set_commands({"info": main})

bot.run()

