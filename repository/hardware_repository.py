from models.hardware import PlacaDeVideo, Processadores

class HardwareRepository:

    def __init__(self):
        self.placas_de_video = []
        self.processadores = []
        self.request_database_placas_video()
        self.request_database_processadores()

    def request_database_placas_video(self):
        #AMD
        self.placas_de_video.append(PlacaDeVideo(560.90, "Radeon RX 550", "AMD", 4))
        self.placas_de_video.append(PlacaDeVideo(1000.0, "Radeon RX 6400", "AMD", 4))
        self.placas_de_video.append(PlacaDeVideo(1300.50, "Radeon RX 6500", "AMD", 8))
        self.placas_de_video.append(PlacaDeVideo(2000.7, "Radeon RX 6600", "AMD", 8))
        self.placas_de_video.append(PlacaDeVideo(4450.5, "Radeon RX 6800", "AMD", 16))

        #NVIDIA
        self.placas_de_video.append(PlacaDeVideo(560.90, "GEFORCE GTX 750TI", "NVIDIA", 2))
        self.placas_de_video.append(PlacaDeVideo(1050.0, "GEFORCE GTX 1630", "NVIDIA", 4))
    
    def request_database_processadores(self):
        #Intel
        self.processadores.append(Processadores(400, "PROCESSADOR INTEL PENTIUM GOLD G6405", "INTEL", 2))
        self.processadores.append(Processadores(700, "INTEL CORE I3-12100F", "INTEL", 4))
        self.processadores.append(Processadores(700, "INTEL CORE I3-12100F", "INTEL", 4))
        self.processadores.append(Processadores(700, "INTEL CORE I3-12100F", "INTEL", 4))
        self.processadores.append(Processadores(1000, "INTEL CORE I5-11400F", "INTEL", 6))

        #AMD
        self.processadores.append(Processadores(350, "AMD ATHLON 300GE PRO", "AMD", 2))
        self.processadores.append(Processadores(700.5, "AMD RYZEN 5 4500", "AMD", 6))
        self.processadores.append(Processadores(990, "AMD RYZEN 5 4600G", "AMD", 6))
        self.processadores.append(Processadores(1040.5, "AMD RYZEN 5 5500", "AMD", 2))

    def filter_list(self, conditional, values: list, key_find: str, key_return: str = "name"):
        filtered_list = [str((value.__dict__)[key_return]) for value in values if conditional(
            (value.__dict__)[key_find]
        )]

        return filtered_list