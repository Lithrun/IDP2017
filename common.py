def getCurrentDate():
    import datetime
    nu = datetime.datetime.now()
    datum = nu.strftime('%d-%m-%Y')
    return datum

def getListSize(list):
    var = len(list)
    if var:
        return var
    return False

def isInt(integer):
    try:
        integer = int(integer)
        return True
    except:
        return False
