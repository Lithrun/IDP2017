# GUI
from tkinter import *
import sql_sportschool as sql

root = Tk()

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

def loginGebruiker():
    pass

login = 0
while True: # Geeft een reactie per 1 seconde
        root.update_idletasks()
        root.update()
        if login == 0:
            showLoginMenu()
            login = 1



