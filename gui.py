# GUI
from tkinter import *
import sql_sportschool as sql
import apparaten
import common
import hardware
import threading
from PIL import ImageTk, Image

apparaten_lst = apparaten.apparaten_lst

root = Tk()
#root.geometry("300x300")
root.title('Benno\'s Sportschool')
#root.configure(background='black')

def showLoginMenu(): # in dit menu moet de bezoeker inloggen met zijn naam en code. De aanbieder kan hier inloggen met zijn wachtwoord en gebruikersnaam. (Via SQLite3)
    global huidigMenu
    huidigMenu = 'Login Menu'

    global bovenLoginFrame
    bovenLoginFrame = Frame(master=root)
    bovenLoginFrame.pack(side=TOP)

    middenLoginFrame = Frame(master=bovenLoginFrame)
    middenLoginFrame.pack(side=BOTTOM)

    gebruikersnaamLoginFrame = Frame(master=middenLoginFrame)
    gebruikersnaamLoginFrame.pack(side=TOP)

    wachtwoordLoginFrame = Frame(master=middenLoginFrame)
    wachtwoordLoginFrame.pack(side=BOTTOM)

    global onderLoginFrame
    onderLoginFrame = Frame(master=root)
    onderLoginFrame.pack(side=BOTTOM)

    global informatieLoginLabel
    informatieLoginLabel = Label(master=bovenLoginFrame,text='Welkom bij Benno\'s sportschool \nVul uw gebruikersnaam en wachtwoord in.',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=60,height=5)
    informatieLoginLabel.pack(side=TOP)

    global gebruikersnaamLoginEntry
    gebruikersnaamLoginEntry = Entry(master=gebruikersnaamLoginFrame, bd=5)
    gebruikersnaamLoginEntry.pack(side = RIGHT)

    gebruikersnaamLabel = Label(master=gebruikersnaamLoginFrame, text="Gebruikersnaam")
    gebruikersnaamLabel.pack(side=LEFT)

    wachtwoordLabel = Label(master=wachtwoordLoginFrame, text="Wachtwoord")
    wachtwoordLabel.pack(side=LEFT)

    global wachtwoordLoginEntry
    wachtwoordLoginEntry = Entry(master=wachtwoordLoginFrame,bd=5)
    wachtwoordLoginEntry.pack(side = RIGHT)

    inlogButton = Button(master=onderLoginFrame,command=loginGebruiker,text='Login',height=3,width=20)
    inlogButton.pack(side=LEFT,pady=4,padx=25)

def hideLoginMenu():
    bovenLoginFrame.destroy()
    onderLoginFrame.destroy()

def showApparaatMenu():

    global bovenApparaatFrame
    bovenApparaatFrame = Frame(master=root)
    bovenApparaatFrame.pack(side=TOP)

    informatieLoginLabel = Label(master=bovenApparaatFrame,text='Kies een apparaat dat u wilt gebruiken.',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=60,height=5)
    informatieLoginLabel.pack(side=TOP)

    global naamApparaatLabel
    naamApparaatLabel = Label(master=bovenApparaatFrame,text='',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=60,height=5)
    naamApparaatLabel.pack(side=TOP)

    global huidigApparaat
    huidigApparaat = 'Roeien'

    naamApparaatLabel['text'] = huidigApparaat

    global middenApparaatFrame
    middenApparaatFrame = Frame(master=bovenApparaatFrame)
    middenApparaatFrame.pack(side=BOTTOM)

    volgendeButton = Button(master=middenApparaatFrame,command=volgendeApparaat,text='>',height=3,width=20)
    volgendeButton.pack(side=RIGHT,pady=4,padx=25)

    vorigeButton = Button(master=middenApparaatFrame,command=vorigeApparaat,text='<',height=3,width=20)
    vorigeButton.pack(side=LEFT,pady=4,padx=25)

    f_path = ('apparaten/roeien.jpg')

    global img
    img = ImageTk.PhotoImage(Image.open(f_path))

    global fotoLabel
    fotoLabel = Label(middenApparaatFrame,image=img)
    fotoLabel.pack(side = "bottom", fill = "both", expand = "yes")

    global onderApparaatFrame
    onderApparaatFrame = Frame(master=root)
    onderApparaatFrame.pack(side=BOTTOM)

    kiesApparaatButton = Button(master=onderApparaatFrame,command=kiesApparaat,text='Kies dit apparaat',height=3,width=20)
    kiesApparaatButton.pack(side=RIGHT,pady=4,padx=25)

    loguitButton = Button(master=onderApparaatFrame,command=loguitGebruiker,text='Loguit',height=3,width=20)
    loguitButton.pack(side=LEFT,pady=4,padx=25)


    root.mainloop() # Draw the image

def hideApparaatMenu():
    bovenApparaatFrame.destroy()
    onderApparaatFrame.destroy()

def showSportMenu():

    apparaat_lst = apparaten.getApparaatListFromNaam(huidigApparaat)

    global bovenSportFrame
    bovenSportFrame = Label(master=root)
    bovenSportFrame.pack(side=TOP)

    middenSportFrame = Label(master=bovenSportFrame)
    middenSportFrame.pack(side=BOTTOM)

    prestatieFrame = Label(master=middenSportFrame)
    prestatieFrame.pack(side=LEFT)

    zwaarteFrame = Label(master=middenSportFrame)
    zwaarteFrame.pack(side=RIGHT)

    global onderSportFrame
    onderSportFrame = Label(master=root)
    onderSportFrame.pack(side=BOTTOM)

    naamSportLabel = Label(master=bovenSportFrame,text=huidigApparaat,background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=60,height=5)
    naamSportLabel.pack(side=TOP)

    fotoLabel = Label(bovenSportFrame,image=img)
    fotoLabel.pack(side = "bottom", fill = "both", expand = "yes")

    global min_zwaarte
    min_zwaarte = apparaat_lst[1][0]

    global huidigZwaarte
    huidigZwaarte = min_zwaarte

    global max_zwaarte
    max_zwaarte = apparaat_lst[1][1]

    global stap_zwaarte
    stap_zwaarte = apparaat_lst[1][2]

    global zwaarteLabel
    zwaarteLabel = Label(master=prestatieFrame,text='Zwaarte : {}'.format(min_zwaarte),background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=40,height=1)
    zwaarteLabel.pack(side=TOP)

    global prestatiesLabel
    prestatiesLabel = Label(master=prestatieFrame,text='Tijdsduur: 00:00 \n Verbrande Caloriën : 0',background='darkgrey',foreground='black',font=('Helvetica',10,'bold italic'),width=40,height=2)
    prestatiesLabel.pack(side=BOTTOM)

    zwaarteHogerButton = Button(master=zwaarteFrame,command=zwaarteHoger,text='>',height=3,width=20)
    zwaarteHogerButton.pack(side=RIGHT,pady=4,padx=25)

    zwaarteLagerButton = Button(master=zwaarteFrame,command=zwaarteLager,text='<',height=3,width=20)
    zwaarteLagerButton.pack(side=LEFT,pady=4,padx=25)

    global startSportButton
    startSportButton = Button(master=onderSportFrame,command=startSporten,text='Start',background='green',height=3,width=20)
    startSportButton.pack(side=RIGHT,pady=4,padx=25)

    klaarSportButton = Button(master=onderSportFrame,command=klaarSport,text='Klaar',height=3,width=20)
    klaarSportButton.pack(side=LEFT,pady=4,padx=25)

def hideSportMenu():
    bovenSportFrame.destroy()
    onderSportFrame.destroy()

def zwaarteHoger():
    global huidigZwaarte

    if huidigZwaarte + stap_zwaarte > max_zwaarte:
        huidigZwaarte = max_zwaarte
    else:
        huidigZwaarte = huidigZwaarte + stap_zwaarte

    zwaarteLabel['text'] = 'Zwaarte: {}'.format(huidigZwaarte)

def zwaarteLager():
    global huidigZwaarte

    if huidigZwaarte - stap_zwaarte < min_zwaarte:
        huidigZwaarte = min_zwaarte
    else:
        huidigZwaarte = huidigZwaarte - stap_zwaarte

    zwaarteLabel['text'] = 'Zwaarte: {}'.format(huidigZwaarte)

def klaarSport():
    # sql.verstuurPrestaties()
    global verbrandeCalorien
    global tijd_s
    global tijd_min
    global totale_tijd_s
    global timer

    verbrandeCalorien = 0
    tijd_s = 0
    tijd_min = 0
    totale_tijd_s = 0
    timer = 2

    hideSportMenu()
    showApparaatMenu()

global startSport
startSport = 0

global verbrandeCalorien
verbrandeCalorien = 0

global tijd_s
tijd_s = 0

global tijd_min
tijd_min = 0

global totale_tijd_s
totale_tijd_s = 0

def startSporten():
    global startSport
    global timer

    if startSport == 0:
        hardware.lamp(hardware.GPIOLampGroen,1)
        hardware.lamp(hardware.GPIOLampRood,0)
        startSportButton['text'] = 'Stop'
        startSportButton['background'] = 'red'
        startSport = 1
        timer = 1

        threading.Timer(1,startTimer).start()

    elif startSport == 1:
        hardware.lamp(hardware.GPIOLampGroen,0)
        hardware.lamp(hardware.GPIOLampRood,1)
        timer = 2
        startSportButton['text'] = 'Start'
        startSportButton['background'] = 'green'
        startSport = 0
        # stop de timer

def startTimer():
    global timer
    while True:
        if timer == 1:
            timer = 0
            threading.Timer(1,updateTijdEnCalorien).start()

        if timer == 2:
            break

def updateTijdEnCalorien():

    global verbrandeCalorien
    oud_verbrandeCalorien = verbrandeCalorien
    nieuw_verbrandeCalorien = apparaten.bepaalCalorien(huidigApparaat, huidigZwaarte, 1)
    verbrandeCalorien = oud_verbrandeCalorien + nieuw_verbrandeCalorien

    global tijd_s
    tijd_s = tijd_s + 1

    global totale_tijd_s
    totale_tijd_s = totale_tijd_s + 1

    global tijd_min

    if tijd_s == 60:
        tijd_s = 0
        tijd_min = tijd_min + 1

    if tijd_min > 0:
        prestatiesLabel['text'] = 'Tijdsduur: {} min {} s \n Verbranden Caloriën: {} '.format(tijd_min,tijd_s,round(verbrandeCalorien,2))
    else:
        prestatiesLabel['text'] = 'Tijdsduur: {} s \n Verbranden Caloriën: {} '.format(tijd_s,round(verbrandeCalorien,2))

    global timer
    timer = 1

def volgendeApparaat():
    global huidigApparaat
    global apparaten_lst
    global fotoLabel
    apparaat_lst = apparaten.getApparaatListFromNaam(huidigApparaat)
    huidigApparaatIndex = apparaten_lst.index(apparaat_lst)

    lst_size = common.getListSize(apparaten_lst)
    if huidigApparaatIndex + 1 == lst_size:
        volgendApparaatIndex = 0
    else:
        volgendApparaatIndex = huidigApparaatIndex + 1

    volgendApparaat = apparaten.getApparaatListFromIndex(volgendApparaatIndex)

    fotoLabel.destroy()
    f_path = volgendApparaat[2]

    global img
    img = ImageTk.PhotoImage(Image.open(f_path))
    fotoLabel = Label(middenApparaatFrame,image=img)
    fotoLabel.pack(side = "bottom", fill = "both", expand = "yes")

    huidigApparaat = volgendApparaat[0]
    naamApparaatLabel['text'] = huidigApparaat

    root.mainloop()

def vorigeApparaat():
    global huidigApparaat
    global apparaten_lst
    global fotoLabel
    apparaat_lst = apparaten.getApparaatListFromNaam(huidigApparaat)
    huidigApparaatIndex = apparaten_lst.index(apparaat_lst)

    lst_size = common.getListSize(apparaten_lst)
    if huidigApparaatIndex - 1 < 0:
        volgendApparaatIndex = lst_size - 1
    else:
        volgendApparaatIndex = huidigApparaatIndex - 1

    volgendApparaat = apparaten.getApparaatListFromIndex(volgendApparaatIndex)

    fotoLabel.destroy()
    f_path = volgendApparaat[2]

    global img
    img = ImageTk.PhotoImage(Image.open(f_path))
    fotoLabel = Label(middenApparaatFrame,image=img)
    fotoLabel.pack(side = "bottom", fill = "both", expand = "yes")

    huidigApparaat = volgendApparaat[0]
    naamApparaatLabel['text'] = huidigApparaat

    root.mainloop()

def kiesApparaat():
    hideApparaatMenu()
    showSportMenu()

def loguitGebruiker():
    hideApparaatMenu()
    showLoginMenu()

def loginGebruiker():
    if sql.isLoginCorrect(gebruikersnaamLoginEntry.get(),wachtwoordLoginEntry.get()) == True:
        hideLoginMenu()
        showApparaatMenu()
    else:
        informatieLoginLabel['text'] = 'Uw inlog gegevens zijn onjuist!'

login = 0
root.update_idletasks()
root.update()
while True: # Geeft een reactie per 1 seconde
    root.update_idletasks()
    root.update()
    if login == 0:
        showLoginMenu()
        login = 1
