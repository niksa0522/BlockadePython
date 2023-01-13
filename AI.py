from GameContext import GameContext
from IPlayer import *

class AI(IPlayer):
    def odigraj(self, tabla, playerNum):
        context = GameContext(playerNum,tabla)
        potez = context.VratiPotez(3)
        tabla.Potez(self,potez.pawnNum,potez.pawnMove,potez.wallPlacing,potez.wallType)