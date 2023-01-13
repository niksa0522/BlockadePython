from IPlayer import *

class Human(IPlayer):
    def odigraj(self,tabla,playerNum):
        while True:
            potez= input("Unesi potez: ")
            x = potez.replace("[","")
            y=x.replace("]","")
            z=y.split()
            if(z[0]!=self.tip):
                print("Los igrac")
                continue
            pesak=None
            if(z[1]=="1"):
                pesak = 1
            elif(z[1]=="2"):
                pesak = 2
            else:
                print("Los pesak izabran")
                continue
            pomerajPesaka=None
            if z[2].isnumeric() and z[3].isnumeric:
                pomerajPesaka=(int(z[2])-1,int(z[3])-1)
            else:
                print("Kordinate pomeraja pesaka nisu brojevi")
                continue
            zid=None
            postakvaZida=None
            if len(z)>4:
                if(z[4]=="H"):
                    zid="H"
                elif(z[4]=="V"):
                    zid="V"
                else:
                    print("Los zid izabran")
                    continue
                if z[5].isnumeric() and z[6].isnumeric:
                    postakvaZida = (int(z[5])-1,int(z[6])-1)
                else:
                    print("Kordinate pomeraja pesaka nisu brojevi")
                    continue
            if tabla.Potez(self,pesak,pomerajPesaka,postakvaZida,zid)==True:
                return True
