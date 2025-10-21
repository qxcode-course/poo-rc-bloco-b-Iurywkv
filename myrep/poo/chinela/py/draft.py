class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: int):
        self.__tamanho = valor

chinela = Chinela()
while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())

    chinela.setTamanho(tamanho)
    print("Parabens, você comprou uma chinela do tamanho", chinela.getTamanho())J
 