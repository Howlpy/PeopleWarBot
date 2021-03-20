import sqlite3
#script para cargar los usernames en la base de datos xD

def patata():

    con = sqlite3.connect('peoplewarbot.db')
    cursorObj = con.cursor()
    file = open("twiteros.txt","r")
    users = file.readlines()

    for user in users:
        user_base = user.split(',')
        user = user_base[1]
        ide = user_base[0]
        try:
            user = user.replace("\n", " ")
        except:
            pass
        entities = (ide,user,True)    
        cursorObj.execute('''INSERT INTO firstwar(id_username, username, alive) VALUES(? ,?, ?)''', entities)
        con.commit()

'''con = sqlite3.connect('peoplewarbot.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE firstwar(id integer PRIMARY KEY, id_username integer, username text, alive bool)")

con.commit()'''
patata()
