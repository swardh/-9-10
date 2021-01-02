import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
import itertools as it
import threading
import multiprocessing
import time
import setup as s


from timeit import default_timer as timer
# import LevelTwo as l2
# import GUI as g
from PyQt5.QtCore import QObject, pyqtSignal, QEvent


class MainWindow(qtw.QWidget):
    global whitelist
    whitelist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    global alla
    alla = False
    global checkhow
    checkhow = 0
    global lvl1,lvl2,lvl3
    lvl1 = True
    lvl2 = False
    lvl3 = False

    def __init__(self):
        super().__init__()
        self.setWindowTitle(">9-10")
        self.setLayout(qtw.QVBoxLayout())
        self.window()
        #tim = time.strftime("%H, %M, %S")

        self.show()



    def window(self):
        cont = qtw.QWidget()
        cont.setLayout((qtw.QGridLayout()))

        btn1 = qtw.QPushButton("ONE", )
        btn1.setStyleSheet("background-color:cyan")
        btn1.clicked.connect(lambda: btn1.setStyleSheet("background-color:red"))
        btn2 = qtw.QPushButton("TWO", )
        btn2.setStyleSheet("background-color:cyan")
        btn3 = qtw.QPushButton("THREE")
        btn3.setStyleSheet("background-color:cyan")
        btn4 = qtw.QPushButton("FOUR")
        btn4.setStyleSheet("background-color:cyan")

        lab1 = qtw.QLabel()
        lab1.setStyleSheet("QLabel { background-color : cyan; color : black; }")
        lab1.setAlignment(QtCore.Qt.AlignCenter)
        lab1.setText(str(s.a))
        lab2 = qtw.QLabel()
        lab2.setStyleSheet("background-color:cyan")
        lab2.setAlignment(QtCore.Qt.AlignCenter)
        lab2.setText(str(s.b))
        lab3 = qtw.QLabel()
        lab3.setStyleSheet("background-color:cyan")
        lab3.setAlignment(QtCore.Qt.AlignCenter)
        lab3.setText(str(s.c))
        lab4 = qtw.QLabel()
        lab4.setStyleSheet("background-color:cyan")
        lab4.setAlignment(QtCore.Qt.AlignCenter)
        lab4.setText(str(s.d))
        lab5 = qtw.QLabel()
        lab5.setStyleSheet("background-color:white")
        lab5.setAlignment(QtCore.Qt.AlignCenter)
        lab5.setText(str(s.e))
        lab6 = qtw.QLabel()
        lab6.setStyleSheet("background-color:cyan")
        lab6.setAlignment(QtCore.Qt.AlignCenter)
        lab6.setText(str(s.f))
        lab7 = qtw.QLabel()
        lab7.setStyleSheet("background-color:cyan")
        lab7.setAlignment(QtCore.Qt.AlignCenter)
        lab7.setText(str(s.g))
        lab8 = qtw.QLabel()
        lab8.setStyleSheet("background-color:cyan")
        lab8.setAlignment(QtCore.Qt.AlignCenter)
        lab8.setText(str(s.h))
        lab9 = qtw.QLabel()
        lab9.setStyleSheet("background-color:cyan")
        lab9.setAlignment(QtCore.Qt.AlignCenter)
        lab9.setText(str(s.i))
        lab10 = qtw.QLabel()
        lab10.setStyleSheet("QLabel { background-color : black; color : cyan; }")
        lab10.setAlignment(QtCore.Qt.AlignCenter)
        lab10.setText("Clicks 0")
        lab11 = qtw.QLabel()
        lab11.setStyleSheet("QLabel { background-color : black; color : cyan; }")
        lab11.setAlignment(QtCore.Qt.AlignCenter)
        lab11.setText("Clicks away")
        lab12 = qtw.QLabel()
        lab12.setStyleSheet("QLabel { background-color : black; color : cyan; }")
        lab12.setAlignment(QtCore.Qt.AlignCenter)
        lab12.setText("Level 1")


        cont.layout().addWidget(lab1, 1, 4, 4, 2)
        cont.layout().addWidget(lab2, 1, 18, 4, 2)
        cont.layout().addWidget(lab4, 18, 4, 4, 2)
        cont.layout().addWidget(lab5, 18, 18, 4, 2)
        cont.layout().addWidget(lab7, 34, 4, 4, 2)
        cont.layout().addWidget(lab8, 34, 18, 4, 2)
        cont.layout().addWidget(lab3, 1, 32, 4, 2)
        cont.layout().addWidget(lab6, 18, 32, 4, 2)
        cont.layout().addWidget(lab9, 34, 32, 4, 2)
        cont.layout().addWidget(lab10, 50, 4, 1, 2)
        cont.layout().addWidget(lab11, 50, 18, 1, 2)
        cont.layout().addWidget(lab12, 50, 32, 1, 2)

        #    cont.layout().addWidget(btn1, 0, 1, 30, 10)
        #    cont.layout().addWidget(btn2, 0, 15, 30, 10)
        #    cont.layout().addWidget(btn3, 15, 1, 30, 10)
        #    cont.layout().addWidget(btn4, 15, 15, 30, 10)
        self.layout().addWidget(cont)


        def tid():
            x = 0
            while True:
                lab12.setText(str(x))
                time.sleep(1)
                x += 1


        def settext():
            lab1.setText(str(s.a))
            lab2.setText(str(s.b))
            lab3.setText(str(s.c))
            lab4.setText(str(s.d))
            lab5.setText(str(s.e))
            lab6.setText(str(s.f))
            lab7.setText(str(s.g))
            lab8.setText(str(s.h))
            lab9.setText(str(s.i))
            lab10.setText(str("Clicks\n" + str(s.counter)))
            #lab11.setText(str("x"))


        def cleartext():

            lab1.clear()
            lab2.clear()
            lab3.clear()
            lab4.clear()
            lab5.clear()
            lab6.clear()
            lab7.clear()
            lab8.clear()
            lab9.clear()

        def restarttext():
            global restart
            global rea, reb, rec, red, ree, ref, reg, reh, rei

            if s.rea:
                lab1.setText(str(s.a))
            if s.reb:
                lab2.setText(str(s.b))
            if s.rec:
                lab3.setText(str(s.c))
            if s.red:
                lab4.setText(str(s.d))
            if s.ree:
                lab5.setText(str(s.e))
            if s.ref:
                lab6.setText(str(s.f))
            if s.reg:
                lab7.setText(str(s.g))
            if s.reh:
                lab8.setText(str(s.h))
            if s.rei:
                lab9.setText(str(s.i))

            s.restart = False
            s.rea = False
            s.reb = False
            s.rec = False
            s.red = False
            s.ree = False
            s.ref = False
            s.reg = False
            s.reh = False
            s.rei = False
            s.restart = False

        def restart():
            global a, b, c, d, e, f, g, h, i
            global restart
            global rea, reb, rec, red, ree, ref, reg, reh, rei
            s.restart = False
            if s.a > 9:
                s.a = s.a - 10
                s.rea = True
                s.restart = True
            if s.b > 9:
                s.b = s.b - 10
                s.reb = True
                s.restart = True
            if s.c > 9:
                s.c = s.c - 10
                s.rec = True
                s.restart = True
            if s.d > 9:
                s.d = s.d - 10
                s.red = True
                s.restart = True
            if s.e > 9:
                s.e = s.e - 10
                s.ree = True
                s.restart = True
            if s.f > 9:
                s.f = s.f - 10
                s.ref = True
                s.restart = True
            if s.g > 9:
                s.g = s.g - 10
                s.reg = True
                s.restart = True
            if s.h > 9:
                s.h = s.h - 10
                s.reh = True
                s.restart = True
            if s.i > 9:
                s.i = s.i - 10
                s.rei = True
                s.restart = True

            if s.a < 0:
                s.a = s.a + 10
            if s.b < 0:
                s.b = s.b + 10
            if s.c < 0:
                s.c = s.c + 10
            if s.d < 0:
                s.d = s.d + 10
            if s.e < 0:
                s.e = s.e + 10
            if s.f < 0:
                s.f = s.f + 10
            if s.g < 0:
                s.g = s.g + 10
            if s.h < 0:
                s.h = s.h + 10
            if s.i < 0:
                s.i = s.i + 10

        ##############################################################################


        def startlev3():
            global lvl2, lvl3
            lvl2 = False
            lvl3 = True
            global a, b, c, d, e, f, g, h, i
            s.level = 2
            s.lvl1 = False
            s.lvl2 = True
            print(s.level)
            s.counter = 0
            s.a = 7
            s.b = 3
            s.c = 7
            s.d = 3
            s.e = 9
            s.f = 3
            s.g = 7
            s.h = 4
            s.i = 7

        ##############################################################################

        def changecolor2():
            global a, b, c, d, e, f, g, h, i
            global ab, bb, cb, db, eb, fb, gb, hb, ib
            global hard
            global restart

            if s.a % 2 == 0:
                lab1.setStyleSheet("background-color:cyan")
                s.ab = False
            if s.b % 2 == 0:
                lab2.setStyleSheet("background-color:cyan")
                s.bb = False
            if s.c % 2 == 0:
                lab3.setStyleSheet("background-color:cyan")
                s.cb = False
            if s.d % 2 == 0:
                lab4.setStyleSheet("background-color:cyan")
                s.db = False
            if s.e % 2 == 0:
                lab5.setStyleSheet("background-color:cyan")
                s.eb = False
            if s.f % 2 == 0:
                lab6.setStyleSheet("background-color:cyan")
                s.fb = False
            if s.g % 2 == 0:
                lab7.setStyleSheet("background-color:cyan")
                s.gb = False
            if s.h % 2 == 0:
                lab8.setStyleSheet("background-color:cyan")
                s.hb = False
            if s.i % 2 == 0:
                lab9.setStyleSheet("background-color:cyan")
                s.ib = False


            if s.a % 2 == 1:
                lab1.setStyleSheet("background-color:cyan")
                s.ab = False
            if s.b % 2 == 1:
                lab2.setStyleSheet("background-color:cyan")
                s.bb = False
            if s.c % 2 == 1:
                lab3.setStyleSheet("background-color:cyan")
                s.cb = False
            if s.d % 2 == 1:
                lab4.setStyleSheet("background-color:cyan")
                s.db = False
            if s.e % 2 == 1:
                lab5.setStyleSheet("background-color:cyan")
                s.eb = False
            if s.f % 2 == 1:
                lab6.setStyleSheet("background-color:cyan")
                s.fb = False
            if s.g % 2 == 1:
                lab7.setStyleSheet("background-color:cyan")
                s.gb = False
            if s.h % 2 == 1:
                lab8.setStyleSheet("background-color:cyan")
                s.hb = False
            if s.i % 2 == 1:
                lab9.setStyleSheet("background-color:cyan")
                s.ib = False

            if s.a == 5 or s.a == 9:
                lab1.setStyleSheet("background-color:white")
                s.ab = True
            if s.b == 5 or s.b == 9:
                lab2.setStyleSheet("background-color:white")
                s.bb = True
            if s.c == 5 or s.c == 9:
                lab3.setStyleSheet("background-color:white")
                s.cb = True
            if s.d == 5 or s.d == 9:
                lab4.setStyleSheet("background-color:white")
                s.db = True
            if s.e == 5 or s.e == 9:
                lab5.setStyleSheet("background-color:white")
                s.eb = True
            if s.f == 5 or s.f == 9:
                lab6.setStyleSheet("background-color:white")
                s.fb = True
            if s.g == 5 or s.g == 9:
                lab7.setStyleSheet("background-color:white")
                s.gb = True
            if s.h == 5 or s.h == 9:
                lab8.setStyleSheet("background-color:white")
                s.hb = True
            if s.i == 5 or s.i == 9:
                lab9.setStyleSheet("background-color:white")
                s.ib = True

            if s.hard == False:
                settext()
            else:
                cleartext()

            if s.restart == True:
                restarttext()
            else:
                pass

            if s.tidtagning == True:
                t1 = threading.Thread(target=tid(), daemon=True)
                t1.start()

        def settext2():

            lab1.setText(str(s.a))
            lab2.setText(str(s.b))
            lab3.setText(str(s.c))
            lab4.setText(str(s.d))
            lab5.setText(str(s.e))
            lab6.setText(str(s.f))
            lab7.setText(str(s.g))
            lab8.setText(str(s.h))
            lab9.setText(str(s.i))

        def startlev2():
            global lvl1, lvl2
            lvl1 = False
            lvl2 = True
            global a, b, c, d, e, f, g, h, i
            s.level = 2
            s.lvl1 = False
            s.lvl2 = True
            print(s.level)
            s.counter = 0
            s.a = 1
            s.b = 4
            s.c = 1
            s.d = 4
            s.e = 3
            s.f = 4
            s.g = 1
            s.h = 1
            s.i = 1

    #        changecolor2()
    #        settext2()

        def b12(x):
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a + 2
            s.c = s.c + 1
            s.e = s.e + 2
            s.g = s.g + 1
            s.i = s.i + 2
            print("två")
            s.history.append(1)
            check2()

        def minb12(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a - 2
            s.c = s.c - 1
            s.e = s.e - 2
            s.g = s.g - 1
            s.i = s.i - 2
            check2()

        def b22(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b + 3
            s.d = s.d + 2
            s.f = s.f + 3
            s.h = s.h + 2
            s.history.append(2)
            check2()

        def minb22(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b - 3
            s.d = s.d - 2
            s.f = s.f - 3
            s.h = s.h - 2
            check2()

        def b32(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a + 1
            s.b = s.e + 2
            s.c = s.c + 3
            s.d = s.d + 1
            s.e = s.e + 2
            s.f = s.f + 3
            s.g = s.g + 1
            s.h = s.h + 2
            s.i = s.i + 3
            s.history.append(3)
            check2()

        def minb32(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a - 1
            s.b = s.e - 2
            s.c = s.c - 3
            s.d = s.d - 1
            s.e = s.e - 2
            s.f = s.f - 3
            s.g = s.g - 1
            s.h = s.h - 2
            s.i = s.i - 3
            check2()

        def b42(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            # a = a + 2
            s.e = s.e + 1
            # c = c + 2
            s.d = s.d + 1
            # e = e + 2
            s.f = s.f + 1
            # g = g + 2
            s.h = s.h + 1
            # i = i + 2
            s.history.append(4)
            check2()

        def minb42(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e - 1
            s.d = s.d - 1
            s.f = s.f - 1
            s.h = s.h - 1
            check2()

        def b52(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a + 1
            # b = b+
            s.c = s.c + 3
            # d = d+
            s.e = s.e + 1
            # f = f+
            s.g = s.g + 3
            s.i = s.i + 4
            s.history.append(5)
            check2()

        def minb52(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a - 1
            s.c = s.c - 3
            s.e = s.e - 1
            s.g = s.g - 3
            s.i = s.i - 4
            check2()

        def b62(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            # a = a + 1
            s.b = s.b + 1
            # c = c + 1
            s.d = s.d + 1
            # e = e + 1
            s.f = s.f + 1
            s.history.append(6)
            check2()

        def minb62(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b - 1
            s.d = s.d - 1
            s.f = s.f - 1
            check2()

        def bx2(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e + 1
            s.history.append("x")
            check2()

        def minbx2(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e - 1
            s.history.append("x")
            check2()

        def win2():
            global ab, bb, cb, db, eb, fb, gb, hb, ib
            msbox = qtw.QMessageBox()

            if s.ab & s.bb & s.cb & s.db & s.eb & s.fb & s.gb & s.hb & s.ib:
                msbox.setText("Nivå 2 avklarad! \nPå " + str(s.counter) + " click.")
                msbox.exec_()
                print("win")
                startlev3()
            s.ab = False
            s.bb = False
            s.cb = False
            s.db = False
            s.eb = False
            s.fb = False
            s.gb = False
            s.hb = False
            s.ib = False

        def check2():
            restart()
            changecolor2()
            win2()
            t2 = threading.Thread(target=howclose(), daemon=True)
            t2.start()
            howclose()

        # RUTA 8, UNDO
        def bmin2(x):
            try:
                print(s.history[-1])
                last = s.history[-1]

                if last == 1:
                    minb12(x)
                if last == 2:
                    minb22(x)
                if last == 3:
                    minb32(x)
                if last == 4:
                    minb42(x)
                if last == 5:
                    minb52(x)
                if last == 6:
                    minb62(x)
                if last == "x":
                    minbx2(x)

                s.history.remove(last)

            except:
                print("funkar ej")

        ###################################################################

        def changecolor():
            global a, b, c, d, e, f, g, h, i
            global ab, bb, cb, db, eb, fb, gb, hb, ib
            global hard
            global restart
            global whitelist

            if s.a % 2 == 0:
                lab1.setStyleSheet("background-color:cyan")
                s.ab = False
                whitelist[0] = 2
            if s.b % 2 == 0:
                lab2.setStyleSheet("background-color:cyan")
                s.bb = False
                whitelist[1] = 2
            if s.c % 2 == 0:
                lab3.setStyleSheet("background-color:cyan")
                s.cb = False
                whitelist[2] = 2
            if s.d % 2 == 0:
                lab4.setStyleSheet("background-color:cyan")
                s.db = False
                whitelist[3] = 2
            if s.e % 2 == 0:
                lab5.setStyleSheet("background-color:cyan")
                s.eb = False
                whitelist[4] = 2
            if s.f % 2 == 0:
                lab6.setStyleSheet("background-color:cyan")
                s.fb = False
                whitelist[5] = 2
            if s.g % 2 == 0:
                lab7.setStyleSheet("background-color:cyan")
                s.gb = False
                whitelist[6] = 2
            if s.h % 2 == 0:
                lab8.setStyleSheet("background-color:cyan")
                s.hb = False
                whitelist[7] = 2
            if s.i % 2 == 0:
                lab9.setStyleSheet("background-color:cyan")
                s.ib = False
                whitelist[8] = 2

            if s.a % 2 == 1:
                lab1.setStyleSheet("background-color:white")
                s.ab = True
                whitelist[0] = 1
            if s.b % 2 == 1:
                lab2.setStyleSheet("background-color:white")
                s.bb = True
                whitelist[1] = 1
            if s.c % 2 == 1:
                lab3.setStyleSheet("background-color:white")
                s.cb = True
                whitelist[2] = 1
            if s.d % 2 == 1:
                lab4.setStyleSheet("background-color:white")
                s.db = True
                whitelist[3] = 1
            if s.e % 2 == 1:
                lab5.setStyleSheet("background-color:white")
                s.eb = True
                whitelist[4] = 1
            if s.f % 2 == 1:
                lab6.setStyleSheet("background-color:white")
                s.fb = True
                whitelist[5] = 1
            if s.g % 2 == 1:
                lab7.setStyleSheet("background-color:white")
                s.gb = True
                whitelist[6] = 1
            if s.h % 2 == 1:
                lab8.setStyleSheet("background-color:white")
                s.hb = True
                whitelist[7] = 1
            if s.i % 2 == 1:
                lab9.setStyleSheet("background-color:white")
                s.ib = True
                whitelist[8] = 1

            if s.a == 3 or s.a == 6 or s.a == 9:
                lab1.setStyleSheet("background-color:red")
                s.ab = False
                whitelist[0] = 3
            if s.b == 3 or s.b == 6 or s.b == 9:
                lab2.setStyleSheet("background-color:red")
                s.bb = False
                whitelist[1] = 3
            if s.c == 3 or s.c == 6 or s.c == 9:
                lab3.setStyleSheet("background-color:red")
                s.cb = False
                whitelist[2] = 3
            if s.d == 3 or s.d == 6 or s.d == 9:
                lab4.setStyleSheet("background-color:red")
                s.db = False
                whitelist[3] = 3
            if s.e == 3 or s.e == 6 or s.e == 9:
                lab5.setStyleSheet("background-color:red")
                s.eb = False
                whitelist[4] = 3
            if s.f == 3 or s.f == 6 or s.f == 9:
                lab6.setStyleSheet("background-color:red")
                s.fb = False
                whitelist[5] = 3
            if s.g == 3 or s.g == 6 or s.g == 9:
                lab7.setStyleSheet("background-color:red")
                s.gb = False
                whitelist[6] = 3
            if s.h == 3 or s.h == 6 or s.h == 9:
                lab8.setStyleSheet("background-color:red")
                s.hb = False
                whitelist[7] = 3
            if s.i == 3 or s.i == 6 or s.i == 9:
                lab9.setStyleSheet("background-color:red")
                s.ib = False
                whitelist[8] = 3

            if s.hard == False:
                settext()
            else:
                cleartext()

            if s.restart == True:
                restarttext()
            else:
                pass

            # s.tidtagning = True
            # if s.tidtagning == True:
            #     t1 = threading.Thread(target=tid(), daemon=True)
            #     t1.start()

        def b1(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
#            s.tidtagning = True
            s.counter = s.counter + 1
            s.a = s.a + 1
            s.c = s.c + 1
            s.e = s.e + 1
            s.g = s.g + 1
            s.i = s.i + 1

            s.history.append(1)
            check()


        def minb1(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a - 1
            s.c = s.c - 1
            s.e = s.e - 1
            s.g = s.g - 1
            s.i = s.i - 1
            check()

        def b2(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b + 1
            s.d = s.d + 1
            s.f = s.f + 1
            s.h = s.h + 1
            s.history.append(2)
            check()

        def minb2(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b - 1
            s.d = s.d - 1
            s.f = s.f - 1
            s.h = s.h - 1
            check()

        def b3(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a + 2
            #            b = e + 2
            s.c = s.c + 2
            #            d = d + 2
            s.e = s.e + 2
            #            f = f + 2
            s.g = s.g + 2
            #            h = h + 2
            s.i = s.i + 2
            s.history.append(3)
            check()

        def minb3(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            a = a - 2
            c = c - 2
            e = e - 2
            g = g - 2
            i = i - 2
            check()

        def b4(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            # a = a + 2
            s.e = s.e + 2
            # c = c + 2
            s.d = s.d + 2
            # e = e + 2
            s.f = s.f + 2
            # g = g + 2
            s.h = s.h + 2
            # i = i + 2
            s.history.append(4)
            check()

        def minb4(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e - 2
            s.d = s.d - 2
            s.f = s.f - 2
            s.h = s.h - 2
            check()

        def b5(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a + 3
            # b = b+
            s.c = s.c + 3
            # d = d+
            s.e = s.e + 3
            # f = f+
            s.g = s.g + 3
            s.i = s.i + 3
            s.history.append(5)
            check()

        def minb5(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.a = s.a - 3
            s.c = s.c - 3
            s.e = s.e - 3
            s.g = s.g - 3
            s.i = s.i - 3
            check()

        def b6(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            # a = a + 1
            s.b = s.b + 3
            # c = c + 1
            s.d = s.d + 3
            # e = e + 1
            s.f = s.f + 3
            s.history.append(6)
            check()

        def minb6(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.b = s.b - 3
            s.d = s.d - 3
            s.f = s.f - 3
            check()

        def bx(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e + 1
            s.history.append("x")
            check()

        def minbx(x):
            global lista
            global a, b, c, d, e, f, g, h, i
            global counter
            s.counter = s.counter + 1
            s.e = s.e - 1
            s.history.append("x")
            check()

        def b1y(x):
            global a, b, c, d, e, f, g, h, i
            s.a = s.a + 1
            s.c = s.c + 1
            s.e = s.e + 1
            s.g = s.g + 1
            s.i = s.i + 1

        def b2y(x):
            global a, b, c, d, e, f, g, h, i
            s.b = s.b + 1
            s.d = s.d + 1
            s.f = s.f + 1
            s.h = s.h + 1

        def b3y(x):
            global a, b, c, d, e, f, g, h, i
            s.a = s.a + 2
            s.c = s.c + 2
            s.e = s.e + 2
            s.g = s.g + 2
            s.i = s.i + 2

        def b4y(x):
            global a, b, c, d, e, f, g, h, i
            s.e = s.e + 2
            s.d = s.d + 2
            s.f = s.f + 2
            s.h = s.h + 2

        def b5y(x):
            global a, b, c, d, e, f, g, h, i
            s.a = s.a + 3
            s.c = s.c + 3
            s.e = s.e + 3
            s.g = s.g + 3
            s.i = s.i + 3

        def b6y(x):
            global a, b, c, d, e, f, g, h, i
            s.b = s.b + 3
            s.d = s.d + 3
            s.f = s.f + 3

        def bxy(x):
            global a, b, c, d, e, f, g, h, i
            s.e = s.e + 1

        def howclose(b):
            x = 0
            global ab, bb, cb, db, eb, fb, gb, hb, ib
            global whitelist
            global checkhow
            global alla
            funcs = (b1, b2, b3, b4, b5, b6, bx)

            for i in it.product(funcs, repeat=b):
                hca = s.a
                hcb = s.b
                hcc = s.c
                hcd = s.d
                hce = s.e
                hcf = s.f
                hcg = s.g
                hch = s.h
                hci = s.i
                if b1 in i:
                    b1y(x)
                if b2 in i:
                    b2y(x)
                if b3 in i:
                    b3y(x)
                if b4 in i:
                    b4y(x)
                if b5 in i:
                    b5y(x)
                if b6 in i:
                    b6y(x)
                if bx in i:
                    bxy(x)
                changecolor()
        #        if s.ab & s.bb & s.cb & s.db & s.eb & s.fb & s.gb & s.hb & s.ib:
                if whitelist == [1,1,1,1,1,1,1,1,1]:
                    for y in i:
                        print("in y " + str(y))
                    clicksaway = (len(i))
                    lab11.setText("Clicks away\n" + str(clicksaway))
                    print("-------")
                    alla = True
                    checkhow = 0
                    restart()
                    s.a = hca
                    s.b = hcb
                    s.c = hcc
                    s.d = hcd
                    s.e = hce
                    s.f = hcf
                    s.g = hcg
                    s.h = hch
                    s.i = hci
                    changecolor()
                    return clicksaway

                else:
                    antal = len(i)
                    print(antal)
                    s.a = hca
                    s.b = hcb
                    s.c = hcc
                    s.d = hcd
                    s.e = hce
                    s.f = hcf
                    s.g = hcg
                    s.h = hch
                    s.i = hci
                    changecolor()
                    restart()
                    if antal > 3:
                        lab11.setText("More than 3\n clicks away")
                        alla = True
                        checkhow = 0
                        return
            s.a = hca
            s.b = hcb
            s.c = hcc
            s.d = hcd
            s.e = hce
            s.f = hcf
            s.g = hcg
            s.h = hch
            s.i = hci
            changecolor()
            checkhowmany()



        def win():
            global ab, bb, cb, db, eb, fb, gb, hb, ib
            global tidtagning
            global lvl1, lvl2, lvl3
            s.tidtagning = False
            msbox = qtw.QMessageBox()

            if s.ab & s.bb & s.cb & s.db & s.eb & s.fb & s.gb & s.hb & s.ib:
                if lvl1 == True:
                    msbox.setText("You Did It!!! \nPå " + str(s.counter) + " click. \nMen har du klarat UFOt?")
                    msbox.exec_()
                    lab12.setText("Level 2")
                    startlev2()
                elif lvl2 == True:
                    msbox.setText("Nivå 2 avklarad!!! \nPå " + str(s.counter) + " click. \nEn nivå kvar...")
                    msbox.exec_()
                    lab12.setText("Level 3")
                    startlev3()
                else:
                    msbox.setText("Nivå 3 också??!!! \nPå " + str(s.counter) + " click. \nDet var allt för nu.")
                    msbox.exec_()
                    lab12.setText("Overload!..!")
                    startlev2()

            s.ab = False
            s.bb = False
            s.cb = False
            s.db = False
            s.eb = False
            s.fb = False
            s.gb = False
            s.hb = False
            s.ib = False

        def checkhowmany():
            global alla
            global checkhow
            if alla == False:
                checkhow = checkhow + 1
                howclose(checkhow)


        def check():
            global alla
            alla = False
            restart()
            changecolor()
            win()
            t3 = threading.Thread(target=checkhowmany(), daemon=True)
            t3.start()
    #        checkhowmany()


        # RUTA 8, UNDO
        def bmin(x):
            try:
                print(s.history[-1])
                last = s.history[-1]

                if last == 1:
                    minb1(x)
                if last == 2:
                    minb2(x)
                if last == 3:
                    minb3(x)
                if last == 4:
                    minb4(x)
                if last == 5:
                    minb5(x)
                if last == 6:
                    minb6(x)
                if last == "x":
                    minbx(x)

                s.history.remove(last)

            except:
                print("funkar ej")


        # def tid():
        #
        #     ti = 0
        #     while True:
        #         lab11.setText(str(ti))
        #         ti = ti+1

    #    if s.lvl1 == True:
        lab1.mouseReleaseEvent = b1
        lab9.mouseReleaseEvent = b2
        lab4.mouseReleaseEvent = b3
        lab5.mouseReleaseEvent = bx
        lab6.mouseReleaseEvent = b4
        lab7.mouseReleaseEvent = b5
        lab3.mouseReleaseEvent = b6
        lab8.mouseReleaseEvent = bmin
        # if s.lvl2 == True:
        #     lab1.mouseReleaseEvent = b12
        #     lab9.mouseReleaseEvent = b22
        #     lab4.mouseReleaseEvent = b32
        #     lab5.mouseReleaseEvent = bx2
        #     lab6.mouseReleaseEvent = b42
        #     lab7.mouseReleaseEvent = b52
        #     lab3.mouseReleaseEvent = b62
        #     lab8.mouseReleaseEvent = bmin2
        checkhowmany()



startmsg = "Hej\n" \
           "Målet är att få alla rutor vita!\n" \
           "Lycka till!"


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = MainWindow()
    mw.setGeometry(400, 100, 400, 400)
    mw.setStyleSheet("background-color:black")
    app.setStyle(qtw.QStyleFactory.create('fusion'))
    box = qtw.QMessageBox(None)
    box.setText(startmsg)
    box.setGeometry(480, 250, 0, 0)
    box.exec_()

    ques = qtw.QMessageBox.question(None, "Difficulty", "Yes = Hard \nNo = Easy..?", qtw.QMessageBox.Yes,
                                    qtw.QMessageBox.No)
    if ques == qtw.QMessageBox.Yes:
        s.hard = True

    app.exec_()


