from Board import *
from copy import deepcopy

class Pawn:
    def __init__(self,player,tip,coord=None):
        self.player = player
        self.tip=tip
        if coord==None:
            self.coord = None
        else:
            self.coord=coord
    
    def __deepcopy__(self,memo):
        id_self=id(self)
        _copy=memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                self.player,
                deepcopy(self.tip,memo),
                deepcopy(self.coord,memo)
            )
            memo[id_self]=_copy
        return _copy

    def Postavi(self,coord,board):
        if(self.coord == None):
            self.coord = coord
            board.tablaPesaka[coord[0]][coord[1]] = self.tip
        else:
            coords = board.ReturnValidMovesForPawn(self.coord,self.player.endPoz)
            if(coord in coords):
                board.tablaPesaka[self.coord[0]][self.coord[1]] = "  "
                self.coord = coord
                board.tablaPesaka[coord[0]][coord[1]] = self.tip
            else:
                print("Los Potez")
