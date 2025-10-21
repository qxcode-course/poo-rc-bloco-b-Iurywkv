class Roupa:
    def __init__(self):
        self.__roupa: str = ""  
    
    def getTamanho(self) -> str:
        return self.__roupa
        
    def setTamanho(self, tamanho:str):
        if tamanho!="PP" and tamanho!="P" and tamanho!="M" and tamanho!="G" and tamanho!="GG" and tamanho!="XG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else: 
            self.__roupa = tamanho

roupa = Roupa()
while True:
    line: str = input()
    print("$" + line)
    args: list[str] = line.split()
    if args[0] == "show":
        print(f"size: ({roupa.getTamanho()})")
    if args[0] == "size":
        tamanho = args[1]
        roupa.setTamanho(tamanho)
    if args[0] == "end":
        break