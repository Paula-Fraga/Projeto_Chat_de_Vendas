class Hardware:

    def __init__(self, price: float, name: str, fabricante: str):
        self.price = price
        self.name = name
        self.fabricante = fabricante

class PlacaDeVideo(Hardware):

    def __init__(self, price: float, name: str, fabricante: str, memoria: int):
        super().__init__(price, name, fabricante)
        self.memoriaVideo = memoria
    
class Processadores(Hardware):

    def __init__(self, price: float, name: str, fabricante: str, quant_n: int):
        super().__init__(price, name, fabricante)
        self.quant_nucleos = quant_n