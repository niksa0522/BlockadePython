from copy import copy,deepcopy

class Tabla:
    __slots__ = 'a', '__dict__'
    def __init__(self,niz,niz2):
        self.niz = niz
        self.niz2=niz2
    def __copy__(self):
        return type(self)(self.niz,self.niz2)
    def __deepcopy__(self,memo):
        id_self=id(self)
        _copy=memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.niz,memo),
                self.niz2
            )
            memo[id_self]=_copy
        return _copy
    def update(self,num):
        self.niz.append(num)

class test:
    def __init__(self,test=None):
        if test==None:
            self.test="pera"
        else:
            self.test=test

tabla1 = Tabla([1,1],[1,1,1])
tabla2 = deepcopy(tabla1)
tabla2.update(5)
print(tabla1.niz)
print(tabla2.niz)

test1 = test()
test2 = test("laza")
print(test1.test)
print(test2.test)

potez = input("Unesi Potez: ")
if potez.isnumeric():
    print(int(potez))
else:
    print("nije broj")
tablaPesaka=[["  " for y in range(10)] for x in range(10)]
tablaDruga = [[tablaPesaka[x][y] for y in range(10)] for x in range(10)]
print(tablaDruga)