import sys
from SearchAlgorithms import *
from Board import *
from copy import deepcopy
from os import system
from Move import Potez
from copy import copy,deepcopy

class GameContext:
    

    def __init__(self,naPotezu,TrenutnoStanje):
        self.naPotezu = naPotezu
        self.TrenutnoStanje=TrenutnoStanje


    def PromeniStanje(self,potez):
        result=True
        potez.prethodnoStanje = self
        potez.narednoStanje = GameContext(copy(self.naPotezu),deepcopy(self.TrenutnoStanje))
        #potez.narednoStanje = GameContext(self.naPotezu,Board(self.TrenutnoStanje.red,self.TrenutnoStanje.kol,self.TrenutnoStanje.igraci,self.TrenutnoStanje.tablaPesaka,self.TrenutnoStanje.tablaVZidova,self.TrenutnoStanje.tablaHZidova))
        result = potez.narednoStanje.TrenutnoStanje.PotezNoDebug(potez.narednoStanje.TrenutnoStanje.igraci[potez.narednoStanje.naPotezu],potez.pawnNum,potez.pawnMove,potez.wallPlacing,potez.wallType)
        potez.narednoStanje.Next()
        return result
    
    def Next(self):
        num = self.naPotezu
        num=num+1
        num=num%2
        self.naPotezu=num

    def ListaPoteza(self):
        potezi = self.TrenutnoStanje.ListaPoteza(self.naPotezu)
        poteziKrajnji=[]
        for x in potezi:
            if self.PromeniStanje(x):
                poteziKrajnji.append(x)
        return poteziKrajnji

    def Proceni(self,stanje):
        prviIgrac = stanje.TrenutnoStanje.igraci[0]
        drugiIgrac = stanje.TrenutnoStanje.igraci[1]
        putPrvi=None
        putDrugi=None
        if prviIgrac.jePobedio():
            return 10000
        if drugiIgrac.jePobedio():
            return -10000
        for x in prviIgrac.pesaci:
            if putPrvi==None:
                putPrvi=len(BFS_WithPath(stanje.TrenutnoStanje,x.coord,prviIgrac.endPoz))
            else:
                putPriv = len(BFS_WithPath(stanje.TrenutnoStanje,x.coord,prviIgrac.endPoz))
                putPrvi = min(putPrvi,putPriv)
        for x in drugiIgrac.pesaci:
            if putDrugi==None:
                putDrugi=len(BFS_WithPath(stanje.TrenutnoStanje,x.coord,drugiIgrac.endPoz))
            else:
                putPriv = len(BFS_WithPath(stanje.TrenutnoStanje,x.coord,drugiIgrac.endPoz))
                putDrugi = min(putDrugi,putPriv)
        return putDrugi-putPrvi


    def VratiPotez(self,depth):
        Potezi = self.ListaPoteza()
        alpha = -sys.maxsize
        beta = sys.maxsize
        if(self.naPotezu==0):
            bestValue = -sys.maxsize
            najboljiPotez = None
            for p in Potezi:
                val = self.AlphaBeta(p.narednoStanje,depth-1,alpha,beta)
                if val > bestValue:
                    bestValue=val
                    najboljiPotez=p
                alpha = max(bestValue,alpha)
                if(p.narednoStanje.TrenutnoStanje.Pobedio()==0):
                    return p
                if (beta<=alpha):
                    break
            return najboljiPotez
        else:
            bestValue=sys.maxsize
            najboljiPotez=None
            for p in Potezi:
                val = self.AlphaBeta(p.narednoStanje,depth-1,alpha,beta)
                if val < bestValue:
                    bestValue=val
                    najboljiPotez=p
                beta = min(bestValue,beta)
                if(p.narednoStanje.TrenutnoStanje.Pobedio()==1):
                    return p
                if (beta<=alpha):
                    break
            return najboljiPotez
    def AlphaBeta(self,Stanje,depth,alpha,beta):
        if depth==0:
            return self.Proceni(Stanje)
        jePobedio = Stanje.TrenutnoStanje.Pobedio()
        if jePobedio!=2:
            if jePobedio==0:
                return 10000
            else:
                return -10000
        Potezi = Stanje.ListaPoteza()
        if len(Potezi)==0:
            return self.Proceni()
        if(Stanje.naPotezu==0):
            bestValue=-sys.maxsize
            for p in Potezi:
                val = self.AlphaBeta(p.narednoStanje,depth-1,alpha,beta)
                if val > bestValue:
                    bestValue=val
                if bestValue>alpha:
                    alpha=bestValue
                if alpha>=beta:
                    break
            return bestValue
        else:
            bestValue=sys.maxsize
            for p in Potezi:
                val = self.AlphaBeta(p.narednoStanje,depth-1,alpha,beta)
                if val < bestValue:
                    bestValue=val
                if bestValue<beta:
                    beta=bestValue
                if alpha>=beta:
                    break
            return bestValue


        


    