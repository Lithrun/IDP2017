# Apparaat naam ('Loopband'), zwaarte opties([ 1, 10 ]), afbeelding ('loopband.jpg'), caloriën / s (0.12)
apparaten_lst = [
    ['Loopband',[1,10],'loopband.jpg',0.15],
    ['Fiets',[1,25],'fiets.jpg',0.03],
]

def getApparaatList(apparaat_naam):
    global apparaten_lst
    for apparaat in apparaten_lst:
        if apparaat[0] == apparaat_naam:
            return apparaat
    print('Het opgegeven apparaatnaam bestaat niet')
    return False

def bepaalCalorien(apparaat_naam, zwaarte, tijd_sec):
    apparaat_lst = getApparaatList(apparaat_naam)
    zwaarte_min = apparaat_lst[1][0]
    zwaarte_max = apparaat_lst[1][1]
    formule = apparaat_lst[3]
    zwaarte_berekening = zwaarte_min + zwaarte / (zwaarte_max - zwaarte_min)
    calorien = formule + zwaarte_berekening * tijd_sec / 10
    calorien = round(calorien,2)
    return calorien

print(bepaalCalorien('Loopband',25,3600))
