class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: int):
        if 20<= valor >=50 and valor % 2 == 0:
        self.__tamanho = valor

        else:
        print("Erro: o tamanho deve ser um número **par** entre 20 e 50.")

chinela = Chinela()
while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())

    chinela.setTamanho(tamanho)
    print("Parabens, você comprou uma chinela do tamanho", chinela.getTamanho())J
 