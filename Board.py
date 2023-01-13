from Move import Potez
from SearchAlgorithms import *
from copy import copy,deepcopy

class Board():

    ##optimizuj kod tako sto ces da imas promenljivu tj niz koja sadrzi listu svih mogucih mesta gde se moze staviti ograda
    ##ovim ces ubrzati vracanje liste svih mogucih poteza, kao i proveru da li je postavljanje ograde moguce
    ##nakon svake postavke ograde je potrebno azurirati listu

    __slots__ = 'a', '__dict__'

    #def __init__(self,red,kol,game,):
    #    self.red =red
    #    self.kol=kol
    #    self.game=game
    #    self.tablaPesaka=[["  " for y in range(kol)] for x in range(red)]
    #    self.tablaVZidova=[["|" for y in range(kol-1)] for x in range(red)]
    #    self.tablaHZidova=[["---" for y in range(kol)] for x in range(red-1)]
    def __init__(self,red,kol,igraci,tablaPesaka=None,tablaVZidova=None,tablaHZidova=None):
        self.red =red
        self.kol=kol
        self.igraci=igraci
        #self.igraci = deepcopy(igraci)
        if tablaPesaka==None:
            self.tablaPesaka=[["  " for y in range(kol)] for x in range(red)]
        else:
            #self.tablaPesaka = [[tablaPesaka[x][y] for y in range(kol)] for x in range(red)]
            self.tablaPesaka=tablaPesaka

        if tablaVZidova==None:
            self.tablaVZidova=[["|" for y in range(kol-1)] for x in range(red)]
        else:
            self.tablaVZidova=tablaVZidova
            #self.tablaVZidova=[[tablaVZidova[x][y] for y in range(kol-1)] for x in range(red)]
        if tablaHZidova==None:
            self.tablaHZidova=[["---" for y in range(kol)] for x in range(red-1)]
        else:
            self.tablaHZidova=tablaHZidova
            #self.tablaHZidova=[[tablaHZidova[x][y] for y in range(kol)] for x in range(red-1)]

    def __copy__(self):
        return type(self)(self.red,self.kol,self.igraci,self.tablaPesaka,self.tablaVZidova,self.tablaHZidova)
    def __deepcopy__(self,memo):
        id_self=id(self)
        _copy=memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.red,memo),
                deepcopy(self.kol,memo),
                deepcopy(self.igraci,memo),
                deepcopy(self.tablaPesaka,memo),
                deepcopy(self.tablaVZidova,memo),
                deepcopy(self.tablaHZidova,memo),
            )
            memo[id_self]=_copy
        return _copy

    def Crtaj(self):
        kar='1'
        print("  ",end=" ")
        for x in range(self.kol):
            print(" ", end=" ")
            if(x>8):
                print(chr(ord(kar)+x+7), end=" ")
            else:
                print(chr(ord(kar)+x), end=" ")
        print(" \n", end=" ")

        print("  ",end=" ")
        for x in range(self.kol):
            print("===", end=" ")
        print(" \n", end=" ")

        for x in range(self.red):
            if(x>8):
                print(chr(ord(kar)+x+7),end=" ")
            else:
                print(chr(ord(kar)+x),end=" ")
            print("ǁ", end=" ")
            for y in range(self.kol):
                print(self.tablaPesaka[x][y],end="")
                if(y<(self.kol-1)):
                    print(self.tablaVZidova[x][y],end=" ")
            print("ǁ", end=" ")
            if(x>8):
                print(chr(ord(kar)+x+7), end=" ")
            else:
                print(chr(ord(kar)+x), end=" ")
            print("\n", end=" ")
            if(x<(self.red-1)):
                print("  ",end=" ")
                for y in range(self.kol):
                    print(self.tablaHZidova[x][y],end=" ")
                print("\n", end=" ")

        print("  ",end=" ")
        for x in range(self.kol):
            print("===", end=" ")
        print(" \n", end=" ")

        print(" ",end=" ")
        for x in range(self.kol):
            print(" ", end=" ")
            if(x>8):
                print(chr(ord(kar)+x+7), end=" ")
            else:
                print(chr(ord(kar)+x), end=" ")
        print(" \n", end=" ")   


    def CheckIfPawnOnCoord(self, coord):
        if(self.tablaPesaka[coord[0]][coord[1]]!="  "):
            return True
        return False

    def CheckIfCanMoveTop(self, coord):
        if(coord[0]<2):
            return False
        return True
    def CheckIfCanMoveTopOne(self, coord):
        if(coord[0]<1):
            return False
        return True
    def CheckIfCanMoveLeft(self, coord):
        if(coord[1]<2):
            return False
        return True
    def CheckIfCanMoveLeftOne(self, coord):
        if(coord[1]<1):
            return False
        return True
    def CheckIfCanMoveBelow(self, coord):
        if(coord[0]<(self.red-2)):
            return True
        return False
    def CheckIfCanMoveBelowOne(self, coord):
        if(coord[0]<(self.red-1)):
            return True
        return False
    def CheckIfCanMoveRight(self, coord):
        if(coord[1]<(self.kol-2)):
            return True
        return False
    def CheckIfCanMoveRightOne(self, coord):
        if(coord[1]<(self.kol-1)):
            return True
        return False
    def CheckIfHWallBelowCoord(self,coord):
        if(self.tablaHZidova[coord[0]][coord[1]]=="===" or self.tablaHZidova[coord[0]+1][coord[1]]=="==="):
            return True
        return False
    def CheckIfHWallAboveCoord(self,coord):
        if(self.tablaHZidova[coord[0]-1][coord[1]]=="===" or self.tablaHZidova[coord[0]-2][coord[1]]=="==="):
            return True
        return False
    def CheckIfVWallLeftOfCoord(self,coord):
        if(self.tablaVZidova[coord[0]][coord[1]-1]=="ǁ" or self.tablaVZidova[coord[0]][coord[1]-2]=="ǁ"):
            return True
        return False
    def CheckIfVWallRightOfCoord(self,coord):
        if(self.tablaVZidova[coord[0]][coord[1]]=="ǁ" or self.tablaVZidova[coord[0]][coord[1]+1]=="ǁ"):
            return True
        return False
    def CheckIfWallTopLeft(self,coord):
        if(self.tablaHZidova[coord[0]-1][coord[1]]=="===" and self.tablaHZidova[coord[0]-1][coord[1]-1]=="==="):
            return True
        if(self.tablaVZidova[coord[0]][coord[1]-1]=="ǁ" and self.tablaVZidova[coord[0]-1][coord[1]-1]=="ǁ"):
            return True
        if(self.tablaHZidova[coord[0]-1][coord[1]]=="===" and  self.tablaVZidova[coord[0]][coord[1]-1]):
            return True
        if( self.tablaVZidova[coord[0]-1][coord[1]-1]=="ǁ" and self.tablaHZidova[coord[0]-1][coord[1]-1]=="==="):
            return True
        return False
    def CheckIfWallTopRight(self,coord):
        if(self.tablaHZidova[coord[0]-1][coord[1]]=="===" and self.tablaHZidova[coord[0]-1][coord[1]+1]=="==="):
            return True
        if(self.tablaVZidova[coord[0]][coord[1]]=="ǁ" and self.tablaVZidova[coord[0]-1][coord[1]]=="ǁ"):
            return True
        if(self.tablaHZidova[coord[0]-1][coord[1]]=="===" and self.tablaVZidova[coord[0]][coord[1]]=="ǁ"):
            return True
        if(self.tablaHZidova[coord[0]-1][coord[1]+1]=="===" and self.tablaVZidova[coord[0]-1][coord[1]]=="ǁ"):
            return True
        return False
    def CheckIfWallBottomLeft(self,coord):
        if(self.tablaHZidova[coord[0]][coord[1]]=="===" and self.tablaHZidova[coord[0]][coord[1]-1]=="==="):
            return True
        if(self.tablaVZidova[coord[0]][coord[1]-1]=="ǁ" and self.tablaVZidova[coord[0]+1][coord[1]-1]=="ǁ"):
            return True
        if(self.tablaHZidova[coord[0]][coord[1]]=="===" and self.tablaVZidova[coord[0]][coord[1]-1]=="ǁ"):
            return True
        if(self.tablaHZidova[coord[0]][coord[1]-1]=="===" and self.tablaVZidova[coord[0]+1][coord[1]-1]=="ǁ"):
            return True
        return False
    def CheckIfWallBottomRight(self,coord):
        if(self.tablaHZidova[coord[0]][coord[1]]=="===" and self.tablaHZidova[coord[0]][coord[1]+1]=="==="):
            return True
        if(self.tablaVZidova[coord[0]][coord[1]]=="ǁ" and self.tablaVZidova[coord[0]+1][coord[1]]=="ǁ"):
            return True
        if(self.tablaVZidova[coord[0]][coord[1]]=="ǁ" and self.tablaHZidova[coord[0]][coord[1]]=="==="):
            return True
        if(self.tablaHZidova[coord[0]][coord[1]+1]=="===" and self.tablaVZidova[coord[0]+1][coord[1]]=="ǁ"):
            return True
        return False


    def CheckIfHWallTouchesTwoOrMorePoz(self,coord):
        num = 0
        if(coord[1]==0 or coord[1]==(self.kol-2)):
            num=num+1
        if(coord[1]-1>=0 and self.tablaHZidova[coord[0]][coord[1]-1]=="==="):
            num=num+1
        if(coord[1]+2<=self.kol-1 and self.tablaHZidova[coord[0]][coord[1]+2]=="==="):
            num=num+1
        if(self.tablaVZidova[coord[0]][coord[1]]=="ǁ"):
            num=num+1
        if(coord[1]+1<self.kol-1 and self.tablaVZidova[coord[0]][coord[1]+1]=="ǁ"):
            num=num+1
        if(coord[1]-1>=0 and self.tablaVZidova[coord[0]][coord[1]-1]=="ǁ"):
            num=num+1            
        if(coord[0]+1<=self.red-1 and self.tablaVZidova[coord[0]+1][coord[1]]=="ǁ"):
            num=num+1
        if(coord[0]+1<=self.red-1 and coord[1]+1<self.kol-1 and self.tablaVZidova[coord[0]+1][coord[1]+1]=="ǁ"):
            num=num+1
        if(coord[0]+1<=self.red-1 and coord[1]-1>=0 and self.tablaVZidova[coord[0]+1][coord[1]-1]=="ǁ"):
            num=num+1
        if(num>=2):
            return True
        return False
    def CheckIfVWallTouchesTwoOrMorePoz(self,coord):
        num = 0
        if(coord[0]==0 or coord[0]==(self.red-2)):
            num=num+1
        if(coord[0]-1>=0 and self.tablaVZidova[coord[0]-1][coord[1]]=="ǁ"):
            num=num+1
        if(coord[0]+2<=self.red-1 and self.tablaVZidova[coord[0]+2][coord[1]]=="ǁ"):
            num=num+1
        if(self.tablaHZidova[coord[0]][coord[1]]=="==="):
            num=num+1
        if(coord[0]+1<self.red-1 and self.tablaHZidova[coord[0]+1][coord[1]]=="==="):
            num=num+1
        if(coord[0]-1>=0 and self.tablaHZidova[coord[0]-1][coord[1]]=="==="):
            num=num+1            
        if(coord[1]+1<=self.kol-1 and self.tablaHZidova[coord[0]][coord[1]+1]=="==="):
            num=num+1
        if(coord[0]-1>=0 and coord[1]+1<=self.kol-1  and self.tablaHZidova[coord[0]-1][coord[1]+1]=="==="):
            num=num+1
        if(coord[0]+1<self.red-1 and coord[1]+1<=self.kol-1 and self.tablaHZidova[coord[0]+1][coord[1]+1]=="==="):
            num=num+1
        if(num>=2):
            return True
        return False


    def ReturnValidMovesForPawn(self,coord,endPoints):
        validMoves=[]
        #GornjiPotez
        if(self.CheckIfCanMoveTop(coord)):
            TopCoord = (coord[0]-2,coord[1])
            if(self.CheckIfHWallAboveCoord(coord)==False):
                if(self.CheckIfPawnOnCoord(TopCoord)==False or TopCoord in endPoints):
                    validMoves.append(TopCoord)
                elif(self.CheckIfPawnOnCoord((coord[0]-1,coord[1]))==False):
                    validMoves.append((coord[0]-1,coord[1]))
        #GornjiZaJedan
        if(self.CheckIfCanMoveTopOne(coord)):
            TopCoord = (coord[0]-1,coord[1])
            if(self.tablaHZidova[coord[0]-1][coord[1]]!="==="):
                if(TopCoord in endPoints and TopCoord not in validMoves):
                    validMoves.append(TopCoord)
        #DonjiPotez
        if(self.CheckIfCanMoveBelow(coord)):
            BottomCoord = (coord[0]+2,coord[1])
            if(self.CheckIfHWallBelowCoord(coord)==False):
                if(self.CheckIfPawnOnCoord(BottomCoord)==False or BottomCoord in endPoints):
                    validMoves.append(BottomCoord)
                elif(self.CheckIfPawnOnCoord((coord[0]+1,coord[1]))==False):
                    validMoves.append((coord[0]+1,coord[1]))
        #DonjiZaJedan
        if(self.CheckIfCanMoveBelowOne(coord)):
            BottomCoord = (coord[0]+1,coord[1])
            if(self.tablaHZidova[coord[0]][coord[1]]!="==="):
                if(BottomCoord in endPoints and BottomCoord not in validMoves):
                    validMoves.append(BottomCoord)
        #LeviPotez
        if(self.CheckIfCanMoveLeft(coord)):
            LeftCoord = (coord[0],coord[1]-2)
            if(self.CheckIfVWallLeftOfCoord(coord)==False):
                if(self.CheckIfPawnOnCoord(LeftCoord)==False or LeftCoord in endPoints):
                    validMoves.append(LeftCoord)
                elif(self.CheckIfPawnOnCoord((coord[0],coord[1]-1))==False):
                    validMoves.append((coord[0],coord[1]-1))
        #LevoZaJedan
        if(self.CheckIfCanMoveLeftOne(coord)):
            LeftCoord = (coord[0],coord[1]-1)
            if(self.tablaVZidova[coord[0]][coord[1]-1]!="ǁ"):
                if(LeftCoord in endPoints and LeftCoord not in validMoves):
                    validMoves.append(LeftCoord)
        #DesniPotez
        if(self.CheckIfCanMoveRight(coord)):
            RightCoord = (coord[0],coord[1]+2)
            if(self.CheckIfVWallRightOfCoord(coord)==False):
                if(self.CheckIfPawnOnCoord(RightCoord)==False or RightCoord in endPoints):
                    validMoves.append(RightCoord)
                elif(self.CheckIfPawnOnCoord((coord[0],coord[1]+1))==False):
                    validMoves.append((coord[0],coord[1]+1))
        #DesnoZaJedan
        if(self.CheckIfCanMoveRightOne(coord)):
            RightCoord = (coord[0],coord[1]+1)
            if(self.tablaVZidova[coord[0]][coord[1]]!="ǁ"):
                if(RightCoord in endPoints and RightCoord not in validMoves):
                    validMoves.append(RightCoord)
        #LevoGore
        if(self.CheckIfCanMoveLeftOne(coord) and self.CheckIfCanMoveTopOne(coord)):
            TopLeft = (coord[0]-1,coord[1]-1)
            if(self.CheckIfWallTopLeft(coord)==False):
                if(self.CheckIfPawnOnCoord(TopLeft)==False or TopLeft in endPoints):
                    validMoves.append(TopLeft)
        #DesnoGore
        if(self.CheckIfCanMoveRightOne(coord) and self.CheckIfCanMoveTopOne(coord)):
            TopRight = (coord[0]-1,coord[1]+1)
            if(self.CheckIfWallTopRight(coord)==False):
                if(self.CheckIfPawnOnCoord(TopRight)==False or TopRight in endPoints):
                    validMoves.append(TopRight)
        #LevoDole
        if(self.CheckIfCanMoveLeftOne(coord) and self.CheckIfCanMoveBelowOne(coord)):
            BottomLeft = (coord[0]+1,coord[1]-1)
            if(self.CheckIfWallBottomLeft(coord)==False):
                if(self.CheckIfPawnOnCoord(BottomLeft)==False or BottomLeft in endPoints):
                    validMoves.append(BottomLeft)
        #DesnoGore
        if(self.CheckIfCanMoveRightOne(coord) and self.CheckIfCanMoveBelowOne(coord)):
            BottomRight = (coord[0]+1,coord[1]+1)
            if(self.CheckIfWallBottomRight(coord)==False):
                if(self.CheckIfPawnOnCoord(BottomRight)==False or BottomRight in endPoints):
                    validMoves.append(BottomRight)
        return validMoves

    def CheckIfPawnCanMove(self,startCoord,endCoord,endPoz):
        endCoords = self.ReturnValidMovesForPawn(self,startCoord,endPoz)
        if(startCoord in endCoords):
            return True
        return False

    def CheckIfCanPlaceHWall(self,coord):
        if(coord[0]>=(self.red-1) or coord[1]>=(self.kol-1)):
            return False
        if(self.tablaHZidova[coord[0]][coord[1]]=="---" and self.tablaHZidova[coord[0]][coord[1]+1]=="---"):
            if(self.tablaVZidova[coord[0]][coord[1]]=="|" and self.tablaVZidova[coord[0]+1][coord[1]]=="|"):
                if self.CheckIfHWallTouchesTwoOrMorePoz(coord):
                    if self.CheckIfHWallPathBlocking(coord):
                        return True
                else:
                    return True
        return False
    def CheckIfCanPlaceVWall(self,coord):
        if(coord[0]>=(self.red-1) or coord[1]>=(self.kol-1)):
            return False
        if(self.tablaVZidova[coord[0]][coord[1]]=="|" and self.tablaVZidova[coord[0]+1][coord[1]]=="|"):
            if(self.tablaHZidova[coord[0]][coord[1]]=="---" or self.tablaHZidova[coord[0]][coord[1]+1]=="---"):
                if self.CheckIfVWallTouchesTwoOrMorePoz(coord):
                    if self.CheckIfVWallPathBlocking(coord):
                        return True
                else:
                    return True
        return False
    def CheckIfVWallPathBlocking(self,coord):
        check=True
        self.tablaVZidova[coord[0]][coord[1]] = "ǁ"
        self.tablaVZidova[coord[0]+1][coord[1]] = "ǁ"
        for x in self.igraci:
            for y in x.pesaci:
                if not AStar(self,y.coord,x.endPoz): 
                    check=False
        self.tablaVZidova[coord[0]][coord[1]] = "|"
        self.tablaVZidova[coord[0]+1][coord[1]] = "|"
        return check
    def CheckIfHWallPathBlocking(self,coord):
        check=True
        self.tablaHZidova[coord[0]][coord[1]] = "==="
        self.tablaHZidova[coord[0]][coord[1]+1] = "==="
        for x in self.igraci:
            for y in x.pesaci:
                if not AStar(self,y.coord,x.endPoz): 
                    check=False
        self.tablaHZidova[coord[0]][coord[1]] = "---"
        self.tablaHZidova[coord[0]][coord[1]+1] = "---"
        return check
    def Potez(self,igrac, pesak, pomerajPesaka, postavkaZida, zidOrijentacija):
        if not self.ProveriPesak(pomerajPesaka,igrac,igrac.pesaci[pesak-1]):
            print("Los pomeraj pesaka")
            return False
        if postavkaZida==None and zidOrijentacija==None and (len(igrac.Hzidovi)==0 or len(igrac.Vzidovi0)==0):
            igrac.pomeriPesaka(pomerajPesaka,pesak,self)
            return True
        elif postavkaZida==None and zidOrijentacija==None and (len(igrac.Hzidovi)!=0 or len(igrac.Vzidovi0)!=0):
            print("Potrebno je staviti zid")
            return False
        else:
            if zidOrijentacija=="H":
                if len(igrac.Hzidovi)==0:
                    print("Igrac nema vise horizontalne zidove")
                    return False
            else:
                if len(igrac.Vzidovi)==0:
                    print("Igrac nema vise vertikalne zidove")
                    return False
            if not self.ProveriZid(postavkaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
                print("Losa postavka zida")
                return False
            staraCoord = igrac.pesaci[pesak-1].coord
            igrac.pomeriPesaka(pomerajPesaka,pesak,self)
            if not self.ProveriZid(postavkaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
                print("Losa postavka zida")
                igrac.pomeriPesaka(staraCoord,pesak,self)
                return False
            igrac.postaviZid(postavkaZida,zidOrijentacija,self)
            return True
    
    def ProveriPesak(self,pomerajPesaka,igrac,pesak):
        coords = self.ReturnValidMovesForPawn(pesak.coord,igrac.endPoz)
        if pomerajPesaka in coords:
            return True
        else:
            return False
    
    def ProveriZid(self,postavkaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
        if zidOrijentacija=="H":
            if self.CheckIfCanPlaceHWall(postavkaZida):
                return True
            else:
                return False
        else:
            if self.CheckIfCanPlaceVWall(postavkaZida):
                return True
            else:
                return False

    def ProveriZidBlokiraPomeraj(self,postakvaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
        if zidOrijentacija=="H":
            if self.ProveriHZidBlokiraPomeraj(postakvaZida,igrac,pesak,pomerajPesaka,True):
                return True
            else:
                return False
        else:
            if self.ProveriVZidBlokiraPomeraj(postakvaZida,igrac,pesak,pomerajPesaka,True):
                return True
            else:
                return False

    def ProveriHZidBlokiraPomeraj(self,postakvaZida,igrac,pesak,pomerajPesaka,debug=False):
        check=True
        self.tablaHZidova[postakvaZida[0]][postakvaZida[1]] = "==="
        self.tablaHZidova[postakvaZida[0]][postakvaZida[1]+1] = "==="
        if not self.ProveriPesak(pomerajPesaka,igrac,igrac.pesaci[pesak-1]):
            if not debug:
                print("Zid blokira potez pesaka")
            check= False 
        self.tablaHZidova[postakvaZida[0]][postakvaZida[1]] = "---"
        self.tablaHZidova[postakvaZida[0]][postakvaZida[1]+1] = "---"
        return check
    
    def ProveriVZidBlokiraPomeraj(self,postakvaZida,igrac,pesak,pomerajPesaka,debug=False):
        check=True
        self.tablaVZidova[postakvaZida[0]][postakvaZida[1]] = "ǁ"
        self.tablaVZidova[postakvaZida[0]+1][postakvaZida[1]] = "ǁ"
        if not self.ProveriPesak(pomerajPesaka,igrac,igrac.pesaci[pesak-1]):
            if not debug:
                print("Zid blokira potez pesaka")
            check= False 
        self.tablaVZidova[postakvaZida[0]][postakvaZida[1]] = "|"
        self.tablaVZidova[postakvaZida[0]+1][postakvaZida[1]] = "|"
        return check    
        
        
    def ListaPoteza(self,igrac):
        igrac = self.igraci[igrac]
        potezi =[]
        listaZidova = self.ListaZidova(igrac)
        for x in igrac.pesaci:
            listaPomerajaPesaka=self.ReturnValidMovesForPawn(x.coord,igrac.endPoz)
            for y in listaPomerajaPesaka:
                if len(listaZidova)!=0:
                    for z in listaZidova:
                        potez = Potez(igrac.pesaci.index(x)+1,y,z[0],z[1])
                        potezi.append(potez)
                else:
                    potez = Potez(igrac.pesaci.index(x)+1,y,None,None)
                    potezi.append(potez)
        return potezi
    
    def ListaZidova(self,igrac):
        listaZidova = []
        putV=False
        putH=False
        if len(igrac.Vzidovi)!=0:
            putV=True
        if len(igrac.Hzidovi)!=0:
            putH=True
        for x in range(self.red):
            for y in range(self.kol):
                if(x<(self.red-1)):
                    if putH:
                        zid = ((x,y),"H")
                        listaZidova.append(zid)
                if(y<self.kol-1):
                    if putV:
                        zid = ((x,y),"V")
                        listaZidova.append(zid)
        return listaZidova
    def Pobedio(self):
        if self.igraci[0].jePobedio():
            return 0
        if self.igraci[1].jePobedio():
            return 1
        return 2



    def PotezNoDebug(self,igrac, pesak, pomerajPesaka, postavkaZida, zidOrijentacija):
        if not self.ProveriPesak(pomerajPesaka,igrac,igrac.pesaci[pesak-1]):
            return False
        if postavkaZida==None and zidOrijentacija==None and (len(igrac.Hzidovi)==0 or len(igrac.Vzidovi0)==0):
            igrac.pomeriPesaka(pomerajPesaka,pesak,self)
            return True
        elif postavkaZida==None and zidOrijentacija==None and (len(igrac.Hzidovi)!=0 or len(igrac.Vzidovi0)!=0):
            return False
        else:
            if zidOrijentacija=="H":
                if len(igrac.Hzidovi)==0:
                    return False
            else:
                if len(igrac.Vzidovi)==0:
                    return False
            if not self.ProveriZid(postavkaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
                return False
            staraCoord = igrac.pesaci[pesak-1].coord
            igrac.pomeriPesaka(pomerajPesaka,pesak,self)
            if not self.ProveriZid(postavkaZida,zidOrijentacija,igrac,pesak,pomerajPesaka):
                igrac.pomeriPesaka(staraCoord,pesak,self)
                return False
            igrac.postaviZid(postavkaZida,zidOrijentacija,self)
            return True

