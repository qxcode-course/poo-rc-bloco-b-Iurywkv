class Notebook:
    def __init__(self):
        self.__ligado = False

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True 
            print("Notebook ligado")
        else:
            print("O notebook já está ligado")

    def mostrar(self):
        if self.__ligado:
            print("Status: Ligado")
        else:
            print("Status: Desligado")

    def usar(self, tempo):
        if self.__ligado:
            print(f"Usando por {tempo} minutos")
        else:
            print("Erro: ligue o notebook primeiro")

    def getLigado(self):
        return self.__ligado

    def setLigado(self, valor: bool):
        self.__ligado = valor  

notebook = Notebook()
notebook.mostrar()
notebook.usar(10)
notebook.ligar()
notebook.mostrar()
notebook.usar(10)
notebook.desligar()