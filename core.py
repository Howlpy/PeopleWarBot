# coding=utf-8
import twitte
import sqlite3
import random
import time
participantes = {
    
}
nicks = []
def sql_fetch(con):
    global participantes
    global nicks
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM firstwar')
 
    rows = cursorObj.fetchall()
    contador = 0
    for row in rows:
        patata = "participante"
        participante = row[2]
        participante_dict = {"ide":row[0],"id_username":row[1],"alive":row[3]}
        participantes.update({row[2]:participante_dict})
        contador += 1
    return
def cargar_datos():
    global nicks
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM firstwar')
    rows = cursorObj.fetchall()

    for row in rows:
        if row[3] == 1:
            nicks.append(row[2])
        else:
            pass
    con.close()
    return


con = sqlite3.connect('peoplewarbot.db')
cursorObj = con.cursor()
sql_fetch(con)
cargar_datos()



desastres = ["Ha ocurrido un incendio en la parte {} de la isla y han muerto: ".format(random.choice(['sur','norte','este','oeste'])),"Terremoto de {} de magnitud en el campo de batalla!! han muerto: ".format(random.randint(6,10)),"Ha habido un Tsunami en la costa {} de la isla y han muerto: ".format(random.choice(['sur','norte','este','oeste'])),"Huracan en la parte {} de la isla y han muerto: ".format(random.choice(['sur','norte','este','oeste'])),'Un volcán activo en la parte {} de la isla ha entrado en erupción y han muerto: '.format(random.choice(['sur','norte','este','oeste'])),'@{} ha utilizado un arma de destruccion masiva y han muerto: '.format(random.choice(nicks))]
gente_muerta_desastre = []
causa_muerte = {
    
    "cuchillo":['ha acuchillado en la barriga y ha dejado los intestinos colgando a','le ha clavado un cuchillo en el cuello a','ha apuñalado en las costillas a'],
    "bate":['ha reventado con un bate de beisbol la cabeza de','le ha partido las piernas con un bate a','ha aplastado con una piedra la cabeza de','ha empalado a'],
    "francotirador":['le ha pegado un tiro de francotirador en la cabeza desde {} metros a'.format(random.randint(50,300)),'ha disparado en el pecho con un rifle de francotirador desde {} metros a'.format(random.randint(50,300))],
    "pistola":['ha acribillado a balazos con una 9mm a','ha reventado con una desert eagle la cabeza de'],
    "manos":['le ha partido el cuello a',"ha asfixiado hasta la muerte a",'ha ahogado en un lago a','le ha reventado la cabeza a hostias a','ha hecho jugo con el cerebro de','ha dado una ensalada de puñetazos a'],
    "rifle_asalto":['ha reventado a balazos con un AK a','le ha volado los sesos con una m4 a','ha usado una m16 para convertir en un coladero el cuerpo de'],
    'barra_acero':['ha usado una barra de acero para hacer pure la cabeza de','utlizando una barra de acero se ha hecho una BMX con los huesos de'],
    'explosivos':['ha usado C4 para hacer volar por los aires a','ha disparado un misil contra','ha lanzado una granada a los pies de'],
    'vehiculos':['ha atropellado con un {} a'.format(random.choice(['BMW M3 E30','Jeep','Audi','Hummer','Range Rover','Golf GT']))],
    'machete':['ha usado un machete para arrancar la cabeza de','ha troceado con un machete el cuerpo de'],
    'escopetazo':['ha usado una escopeta para separar la cabeza del cuerpo de','Ha hecho un agujero con una escopeta en el cuerpo de'],
    'laser':['ha usado un arma laser para desintegrar el cuerpo de','ha usado un arma especial para convertir en {} a'.format(random.choice(['gorrino','cabra','gallina']))],
    'traicion':['se ha aliado con @{} y han matado a'.format(random.choice(nicks))],
    'arco':['ha utilizado un arco para clavar una flecha en {} desde {} metros a'.format(random.choice(['la cabeza','el corazon','el estomago']),random.randint(10,60))],
    'ballesta':['ha utilizado una ballesta para clavar un virote en {} desde {} metros a'.format(random.choice(['la cabeza','el corazon','el estomago']),random.randint(10,60))],
    'lanza':['ha usado una lanza casera para ensartar a','ha utilizado una lanza para abatir desde {} metros a'.format(random.randint(10,25))],
    'maza':['ha usado una maza para hacer salsa la cabeza de','le ha hundido el pecho con una maza a'],
    'catapulta':['construyó una catapulta casera y mató a']

}

causas_raras = {

    "naturales":['ha sufrido un infarto','ha sufrido una emboila','ha tenido un ataque epileptico','se ha desintegrado tocando la guitarra porque tenia lepra','se ha tropezado y se ha reventado la cabeza contra una piedra (La gente ciega?? yo aprendi a ver con 1 año)'],
    "drogas":['ha tenido una sobredosis de Ketamina','se quedo en el sitio tras meterse {} rayas de cocaina'.format(random.randint(15,40)),'Iba puesto de LSD y se tiro por un barranco pensando que era un dragón','Iba puesto de MDMA y se desencajo la mandibula provocandole una emorragia','Despues de chutarse {} dosis de caballo murió de sobredosis'.format(random.randint(3,6)),'se marcó un lil peep'],
    "trampas":['ha caido en una trampa para osos','ha caido en una trampa de {} de {}'.format(random.choice(['pinchos','dardos venenosos','gas']),random.choice(nicks))],
    "animales":['Ha sido atacado por una manada de lobos','ha sido atacado por un caimán y le ha hecho picadillo el cuerpo','ha sido atacado por un oso pardo','ha sido atacado por un grupo de hienas','ha sido mordido por una serpiente venenosa','ha sido atacado por una tribu de indigenas','ha sido devorado por tiburones','fué atacado por un demogorgon y murió'],
    'vehiculo':['ha tenido un accidente en moto','ha tenido un accidente en coche'],
    'intoxicacion':['ha comido carne de un animal enfermo, se ha intoxicado'],
    'agua':['estaba pescando cuando una ola lo arrastró al fondo del mar','se olvidó de hidratarse y se ha quedao mas seco que la mojama'],
    'suicidio':['se dio cuenta de que vivimos en una sociedad y se suicido','se dio cuenta de que ella no le quería y se suicido','se atragantó con una polla de un burro'],
    'nudes':['se desmayó y se abrió la cabeza al ver un nude de {}'.format(random.choice(['@ripreflex','@cartagenaostia','@ansxni','@caIcetines']))]


}


posible_desastre = False


def pelea(participante1,participante2):
    def actualizar_db(derrotado):
        con = sqlite3.connect('peoplewarbot.db')
        cursorObj = con.cursor()
        derrotado_id = participantes[derrotado]['ide']
        print(derrotado_id)
        secuencia = 'UPDATE firstwar SET alive = 0 where id = {}'.format(derrotado_id)
        cursorObj.execute(secuencia)
        con.commit()
        con.close()


    value1 = random.randint(1,100)
    value2 = random.randint(1,100)
    vencedor = ''
    derrotado = ''
    if value1 <= value2:
        vencedor = participante2
        derrotado = participante1
    else:
        vencedor = participante1
        derrotado = participante2
    actualizar_db(derrotado)
    return vencedor, derrotado

def asignar_oponentes(nicks):
    oponente1 = random.choice(nicks)
    oponente2 = random.choice(nicks)
    contador = 0
    while True:
        if oponente1 == oponente2:
            oponente2 = random.choice(nicks)
        else:
            break
    return oponente1,oponente2

def desastre(nicks,gente_muerta_desastre):
    array_random_gente_muerta = []
    def actualizar_db(derrotado):
        con = sqlite3.connect('peoplewarbot.db')
        cursorObj = con.cursor()
        derrotado_id = participantes[derrotado]['ide']
        print(derrotado_id)
        secuencia = 'UPDATE firstwar SET alive = 0 where id = {}'.format(derrotado_id)
        cursorObj.execute(secuencia)
        con.commit()
        con.close()

    num_muertos = random.randint(5,20)
    contador = 0
    desastre = random.choice(desastres)
    texto = ""
    while contador <= num_muertos:
        nick_muerto_desastre = random.choice(nicks)
        gente_muerta_desastre.append("@" + nick_muerto_desastre)
        array_random_gente_muerta.append(nick_muerto_desastre)
        contador += 1
    texto = texto.join(gente_muerta_desastre)
    tweet_a_mandar = "{}{} personas. {}".format(desastre,len(gente_muerta_desastre),texto)
    if len(tweet_a_mandar) <= 240:
        print(tweet_a_mandar)
        for nick in array_random_gente_muerta:
            actualizar_db(nick)
        twitte.tweetear(texto=tweet_a_mandar)
    else:
        print(tweet_a_mandar)
        for nick in array_random_gente_muerta:
            actualizar_db(nick)
        twitte.tweetear(texto=desastre + " Han muerto: {} personas".format(len(gente_muerta_desastre)))
        time.sleep(2)
        t = twitte.get_tweets()
        twitte.tweetear(texto=texto,id=t[0].id)

def causa_de_muerte(causa_muerte,vencedor,vencido,nicks):
    arma = random.choice(list(causa_muerte.keys()))
    arma = random.choice(list(causa_muerte.keys()))
    arma = random.choice(list(causa_muerte.keys()))
    metodo = random.choice(causa_muerte[arma])
    metodo = random.choice(causa_muerte[arma])
    metodo = random.choice(causa_muerte[arma])
    texto="El participante @{} {} @{}\n@{} ha muerto. \n\n{} Participantes restantes".format(vencedor,metodo,vencido,vencido,len(nicks))
    twitte.tweetear(texto=texto)
    #print("El participante @{} {} @{} \n @{} ha muerto. \n\n{} Participantes restantes".format(vencedor,metodo,vencido,vencido,len(nicks)))
    try:
        print("El participante @{} {} @{} \n @{} ha muerto. \n\n{} Participantes restantes".format(vencedor,metodo,vencido,vencido,len(nicks)))
    except Exception as e:
        print('ERROR: \n')
        print(e)
        print('\n')  

def muerte_causas_raras(causas_raras,nicks):
    def actualizar_db(derrotado):
        con = sqlite3.connect('peoplewarbot.db')
        cursorObj = con.cursor()
        derrotado_id = participantes[derrotado]['ide']
        print(derrotado_id)
        secuencia = 'UPDATE firstwar SET alive = 0 where id = {}'.format(derrotado_id)
        cursorObj.execute(secuencia)
        con.commit()
        con.close()
    subnormal = random.choice(nicks)
    tipo = random.choice(list(causas_raras.keys()))
    causa_final = random.choice(causas_raras[tipo])
    actualizar_db(subnormal)
    twitte.tweetear(texto="El participante @{} {} y ha muerto. \n\n Quedan {} participantes".format(subnormal,causa_final,len(nicks)))
    print("El participante @{} {}".format(subnormal,causa_final))





numero_causa_rara = random.randint(1,100)
if posible_desastre == True:
    desastre(nicks,gente_muerta_desastre)
    print('desastre')
elif numero_causa_rara <=7:
    muerte_causas_raras(causas_raras,nicks)
    print('nose')
else:
    if len(nicks) == 1:
        print("El ganador ha sido {}".format(nicks[0]))
        twitte.tweetear(texto="El Ganador de la 3a People War es... \n\n\n @{} \nEnhorabuena!!".format(nicks[0]))
    else:
        o1,o2 = asignar_oponentes(nicks)
        print("Pelea entre {} y {}".format(o1,o2))
        vencedor, vencido = pelea(o1,o2)        
        causa_de_muerte(causa_muerte,vencedor,vencido,nicks)