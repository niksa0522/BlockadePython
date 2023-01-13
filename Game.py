
from Board import *
from AI import *
from GameContext import GameContext
from Human import *
from Pawn import *
from Wall import *


class Game():
    def __init__(self,red,kol,brojZidova,pocPoz,igraPrvi):
        self.brojZidova = brojZidova
        self.pocPoz=[]
        
        for x in pocPoz:
            pozx=x[0]-1
            pozy=x[1]-1
            self.pocPoz.append((pozx,pozy))
        igraci = []
        if(igraPrvi==True):
            igrac = Human("X")
            HP1 = Pawn(igrac,"X1")
            HP2 = Pawn(igrac,"X2")
            igrac.pesaci.append(HP1)
            igrac.pesaci.append(HP2)
            igrac.endPoz.append(self.pocPoz[2])
            igrac.endPoz.append(self.pocPoz[3])
            igraci.append(igrac)
            
            bot = Human("O")
            AIP1 = Pawn(bot,"Y1")
            AIP2 = Pawn(bot,"Y2")
            bot.pesaci.append(AIP1)
            bot.pesaci.append(AIP2)
            bot.endPoz.append(self.pocPoz[0])
            bot.endPoz.append(self.pocPoz[1])
            igraci.append(bot)

        else:
            bot = Human("X")
            AIP1 = Pawn(bot,"X1")
            AIP2 = Pawn(bot,"X2")
            bot.pesaci.append(AIP1)
            bot.pesaci.append(AIP2)
            bot.endPoz.append(self.pocPoz[2])
            bot.endPoz.append(self.pocPoz[3])
            igraci.append(bot)

            igrac = Human("O")
            HP1 = Pawn(igrac,"Y1")
            HP2 = Pawn(igrac,"Y2")
            igrac.pesaci.append(HP1)
            igrac.pesaci.append(HP2)
            igrac.endPoz.append(self.pocPoz[0])
            igrac.endPoz.append(self.pocPoz[1])
            igraci.append(igrac)

        tabla = Board(red,kol,igraci)

        self.tabla=tabla
        self.igraci = igraci
        #self.tabla.igraci = igraci

    def pocni(self):
        for x in range(self.brojZidova):
            self.igraci[0].Hzidovi.append(Wall("H"))
            self.igraci[0].Vzidovi.append(Wall("V"))
            self.igraci[1].Hzidovi.append(Wall("H"))
            self.igraci[1].Vzidovi.append(Wall("V"))
        self.igraci[0].pesaci[0].Postavi(self.pocPoz[0],self.tabla)
        self.igraci[0].pesaci[1].Postavi(self.pocPoz[1],self.tabla)
        self.igraci[1].pesaci[0].Postavi(self.pocPoz[2],self.tabla)
        self.igraci[1].pesaci[1].Postavi(self.pocPoz[3],self.tabla)
        self.tabla.Crtaj()


        playerNum=0
        finished=False
        while not finished:
            trenutniIgrac = self.igraci[playerNum]
            trenutniIgrac.odigraj(self.tabla,playerNum)
            self.tabla.Crtaj()
            if trenutniIgrac.jePobedio():
                finished=True
                print("Igrac " + trenutniIgrac.tip + " je pobedio")
            playerNum=(playerNum+1)%2
            #break

    def odigrajPotez(self, potez):
        x = potez.replace("[","")
        y=x.replace("]","")
        z=y.split()
        igrac = None
        if(z[0]=="X"):
            igrac = self.igraci[0]
        elif(z[0]=="O"):
            igrac = self.igraci[1]
        else:
            print("greska u potezu")
            return
        pesak=None
        if(z[1]=="1"):
            pesak = 1
        elif(z[1]=="2"):
            pesak = 2
        else:
            print("greska u potezu")
            return
        #igrac.pomeriPesaka((int(z[2])-1,int(z[3])-1),pesak)
        pomerajPesaka=(int(z[2])-1,int(z[3])-1)
        zid=None
        postakvaZida=None
        if len(z)>4:
            if(z[4]=="H"):
                zid="H"
            elif(z[4]=="V"):
                zid="V"
            else:
                print("greska u potezu")
                return
            postakvaZida = (int(z[5])-1,int(z[6])-1)
        #igrac.postaviZid((int(z[5])-1,int(z[6])-1),zid)
        self.tabla.Potez(igrac,pesak,pomerajPesaka,postakvaZida,zid)

    

        



igra = Game(11,14,2,[(4,4),(8,4),(4,11),(8,11)],True)
igra.pocni()
#igra.odigrajPotez("[X 1] [4 6] [H 10 1]")
igra.odigrajPotez("[O 1] [4 9] [V 8 10]")
igra.odigrajPotez("[O 1] [6 9] [V 10 10]")
igra.odigrajPotez("[O 1] [6 11] [H 7 11]")
igra.tabla.Crtaj()
igra.odigrajPotez("[O 1] [4 11] [V 8 12]")
igra.odigrajPotez("[O 1] [5 10] [V 10 12]")
igra.tabla.Crtaj()
igra.odigrajPotez("[O 1] [6 11] [H 1 1]")
igra.odigrajPotez("[O 1] [5 12] [H 1 3]")
igra.odigrajPotez("[O 1] [4 11] [H 2 1]")
igra.tabla.Crtaj()
igra.odigrajPotez("[O 2] [8 9] [H 1 1]")
igra.odigrajPotez("[O 1] [6 9] [H 11 10]")
igra.tabla.Crtaj()
#print(igra.igraci[0].jePobedio())

#context= GameContext(0,igra.tabla)
#potez = Potez(1,(3,7),(2,2),"H")
#context.PromeniStanje(potez)
#potez.narednoStanje.TrenutnoStanje.Crtaj()
#lista=context.ListaPoteza()
#lista[0].narednoStanje.TrenutnoStanje.Crtaj()


            

        

