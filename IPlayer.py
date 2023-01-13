
from copy import deepcopy

class IPlayer:

    __slots__ = 'a', '__dict__'

    def __init__(self,tip,pesaci=None,Hzidovi=None,Vzidovi=None,endPoz=None):
        self.tip=tip
        if pesaci==None:
            self.pesaci= []
        else:
            self.pesaci=pesaci
        if Hzidovi==None:
            self.Hzidovi=[]
        else:
            self.Hzidovi = Hzidovi
        if Vzidovi==None:
            self.Vzidovi=[]
        else:
            self.Vzidovi=Vzidovi
        if endPoz==None:
            self.endPoz=[]
        else:
            self.endPoz=endPoz

    def __deepcopy__(self,memo):
        id_self=id(self)
        _copy=memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.tip,memo),
                deepcopy(self.pesaci,memo),
                deepcopy(self.Hzidovi,memo),
                deepcopy(self.Vzidovi,memo),
                deepcopy(self.endPoz,memo)
            )
            memo[id_self]=_copy
        return _copy
    def odigraj(self,tabla,playerNum):
        pass
    def pomeriPesaka(self, coord, pesak,tabla):
        if(pesak==1):
            self.pesaci[0].Postavi(coord,tabla)
        else:
            self.pesaci[1].Postavi(coord,tabla)
    def postaviZid(self, coord, zid,tabla):
        if(zid=="H"):
            Hzid = self.Hzidovi.pop()
            Hzid.Postavi(coord,tabla)
        else:
            Vzid = self.Vzidovi.pop()
            Vzid.Postavi(coord,tabla)
    def jePobedio(self):
        for endPoz in self.endPoz:
            if(self.pesaci[0].coord==endPoz or self.pesaci[1].coord==endPoz):
                return True
        return False