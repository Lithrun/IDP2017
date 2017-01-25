# Apparaat naam (string), zwaarte opties([ min_zwaarte, max_zwaarte, stap naar volgende zwaarte ]), afbeelding ('loopband.jpg'), caloriën / s (float)
global apparaten_lst
apparaten_lst = [
    ['Loopband',[1,10,1],'apparaten/loopband.jpg',0.15],
    ['Fiets',[1,15,1],'apparaten/fiets.jpg',0.20],
    ['Roeien',[1,4,1],'apparaten/roeien.jpg',0.33],
    ['Crosstrainer',[1,10,1],'apparaten/crosstrainer.jpg',0.20],
    ['Gewicht Heffen',[10,80,10],'apparaten/gewichten.jpg',0.40],
    ['Legextension', [10,80,10], 'apparaten/legextension.jpg', 0.15],
    ['Legpress',[15,80,5],'apparaten/legpress.jpg',0.15],
    ['Stairclimber',[1,7,1],'apparaten/stairclimber.jpg',0.07]
]

def getApparaatListFromNaam(apparaat_naam):
    global apparaten_lst
    for apparaat in apparaten_lst:
        if apparaat[0] == apparaat_naam:
            return apparaat
    print('Het opgegeven apparaatnaam bestaat niet')
    return False

def getApparaatListFromIndex(index):
    global apparaten_lst
    for apparaat in apparaten_lst:
        if apparaten_lst.index(apparaat) == index:
            return apparaat
    print('Het opgegeven index nummer bestaat niet')
    return False

#BEREKENDE CALORIEN IS NIET GELIJK AAN DE REALITEIT
def bepaalCalorien(apparaat_naam, zwaarte, tijd_sec):
    apparaat_lst = getApparaatListFromNaam(apparaat_naam)
    zwaarte_min = apparaat_lst[1][0]
    zwaarte_max = apparaat_lst[1][1]
    formule = apparaat_lst[3]
    zwaarte_berekening = zwaarte_min + zwaarte / (zwaarte_max - zwaarte_min)
    calorien = formule + zwaarte_berekening * tijd_sec / 10
    #calorien = round(calorien,2)
    return calorien
