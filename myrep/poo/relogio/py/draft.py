class Notebook:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.segundo = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def __str__(self):
        return f"{self.__hora: 02d}: {self.__minuto: 02d}: {self.__segundo: 02d}"
    
    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto
    
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, hora: int):
        if hora <0 or hora >23:
            print("fail: hora invalida")
            return self.__hora == hora
        
    def setMinuto(self, minuto: int):
        if minuto <0 or minuto >59:
            print("fail: minuto invalido")
            return self.__minuto == minuto
        
    def setSegundo(self, segundo: int):
        if segundo <0 or segundo >59:
            print("fail: segundo invalido")
            return self.segundo == segundo
