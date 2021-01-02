import time
import threading
class setup():

    tidtagning = False

    global whitetuple
    whitetuple = (0,0,0,0,0,0,0,0,0)
    global a, b, c, d, e, f, g, h, i

    # RÄKNARE FÖR VARJE RUTA
    a = 0
    b = 0
    c = 0
    d = 0
    e = 2
    f = 0
    g = 0
    h = 0
    i = 0


    global start
    start = time.strftime("%S")
    global counter
    counter = 0

    # BOOLEAN OM RUTA ÄR VIT ELLER EJ
    #    global ab,bb,cb,db,eb,fb,gb,hb,ib
    ab = False
    bb = False
    cb = False
    db = False
    eb = False
    fb = False
    gb = False
    hb = False
    ib = False

    global rea,reb,rec,red,ree,ref,reg,reh,rei
    rea = False
    reb = False
    rec = False
    red = False
    ree = False
    ref = False
    reg = False
    reh = False
    rei = False

    # VARJE VAL FÖRS IN I DENNA LISTAN
    global history
    history = []
    # SVÅRIGHETSGRAD
    global hard
    hard = False
    # OM HARD, SETTEXT VID OMRÄKNING
    global restart
    restart = False

    global level
    level = 1

    global lvl1
    lvl1 = True
    global lvl2
    lvl2 = False

    def __init__(self):
        print("hej")

