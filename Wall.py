
from copy import deepcopy

class Wall:

    def __init__(self,tip):
        self.tip = tip

    def __deepcopy__(self,memo):
        id_self=id(self)
        _copy=memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.tip,memo)
            )
            memo[id_self]=_copy
        return _copy

    def Postavi(self, coord,board):
        if(self.tip=="H"):
            self.coord = coord
            board.tablaHZidova[coord[0]][coord[1]] = "==="
            board.tablaHZidova[coord[0]][coord[1]+1] = "==="
        elif(self.tip=="V"):
            self.coord = coord
            board.tablaVZidova[coord[0]][coord[1]] = "ǁ"
            board.tablaVZidova[coord[0]+1][coord[1]] = "ǁ"