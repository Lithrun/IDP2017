# MySQL settings
username = 'benno'
global databasename
databasename = 'sportschool'
password = ''
host = ''
# Einde MySQL settings

import sqlite3
#import mysql.connector



def createTables():
    pass

#def connectToDatabase(): # My SQL
#    cnx = mysql.connector.connect(user=username, password=password,
#                              host=host,
#                              database=databasename)
#    cnx.close()

def isDatabaseConnected(databasename):
    try:
        connect = sqlite3.connect(databasename)
        return True
    except:
        return False

def startDatabase(databasename): # Maak tabellen aan als deze nog niet bestaan
    if isDatabaseConnected(databasename) == True:
        connect = sqlite3.connect(databasename)
        c = connect.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                         (gebruikersnaam text UNIQUE, email text, wachtwoord text, laatste_login_datum text)''')

        gegevens = ['test','test@gmail.com','test','11-11-2016']
        try:
            c.execute('''INSERT INTO accounts VALUES(?,?,?,?)''',gegevens)
        except:
            print('Account bestaat al')
        finally:
            connect.commit()

startDatabase(databasename)

def isLoginCorrect(gebruikersnaam,wachtwoord):
    import sqlite3
    database = databasename
    if isDatabaseConnected(database) == True:
        connect = sqlite3.connect(database)
        c = connect.cursor()
        gegevens = [gebruikersnaam, wachtwoord]
        c.execute('''SELECT * FROM accounts WHERE gebruikersnaam = ? AND wachtwoord = ?''',gegevens)
        resultaten = c.fetchall()
        # controleer of gebruikersnaam EN wachtwoord overeenkomen met de opgegeven data
        for resultaat in resultaten:
            if resultaat[0] == gebruikersnaam and resultaat[2] == wachtwoord:
                connect.close()
                return True
        return False
