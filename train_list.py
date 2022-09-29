from datetime import datetime

from repository.hardware_repository import HardwareRepository

class TrainList:

    @staticmethod
    def first_list_conversation(name: str):

        greet = ""

        if datetime.now().hour < 12 :
            greet = "Bom dia"
        elif datetime.now().hour > 12 and datetime.now().hour < 18:
            greet = "Boa tarde"
        else:
            greet = "Boa noite"

        return [
            f"{greet}",
            f"{greet}, sou um assistente virtual!\n" +
            "Escolha uma das opções abaixo para que eu possa te ajudar :)\n" +
            "1 - Se você deseja comprar\n2 - Reclamação",
            "quem é você?",
            f"Meu nome é {name}, sou um assistente virtual :)",
            "1",
            "ok, o que você quer comprar?",
            "2",
            "ok, qual seria a sua reclamação?",
            "gostaria de fazer uma reclamação",
            "ok, qual seria a reclamação?",
            "gostaria de fazer um pedido",
            "ok, qual seria o seu pedido?",
            "Por gentileza, poderia reformular suas palavras, eu não entendi bem :("
        ]

    @staticmethod
    def placas_video():
        
        # Repositório da base de dados.
        store_bd = HardwareRepository()

        # Apenas funções da AMD.
        amd_all_placas = store_bd.filter_list(
            lambda fabricante: fabricante == "AMD",
            store_bd.placas_de_video,
            key_find="fabricante",
            key_return="name"
        )

        # Apenas funções da AMD.
        nvidia_all_placas = store_bd.filter_list(
            lambda fabricante: fabricante == "NVIDIA",
            store_bd.placas_de_video,
            key_find="fabricante",
            key_return="name"
        )

        #custo benefício
        cus_benefi_placas_video = store_bd.filter_list(
            lambda price: price < 600,
            key_find="price",
            key_return="name",
            values=store_bd.placas_de_video
        )

        #Top de linha
        top_linha_placa_de_video = store_bd.filter_list(
            lambda price: price >= 600,
            key_find="price",
            key_return="name",
            values=store_bd.placas_de_video
        )

        return [
            "gostaria de comprar uma placa de vídeo",
            "Temos várias placas de vídeo, tanto da AMD quanto da NVIDIA e, recentemente, da Intel",
            "uma placa de vídeo",
            
            "Qual fabricante ou preço? AMD, NVIDIA ou Intel?",

            "amd",
            f"Temos várias placas de vídeo da AMD {', '.join(amd_all_placas)}",
            "qual seriam as placas de vídeo da amd?",
            f"Temos várias placas de vídeo da AMD {', '.join(amd_all_placas)}",

            "nvidia",
            f"Temos várias placas de vídeo da NVIDIA {', '.join(nvidia_all_placas)}",
            "qual seriam as placas de vídeo da NVIDIA?",
            f"Temos várias placas de vídeo da NVIDIA {', '.join(nvidia_all_placas)}",

            "qual a mais indicada?",
            "Você quer uma placa de vídeo para segmento de entrada ou top de linha?",

            "custo benefício",
            f"Temos placas de vídeo como: { ', '.join(cus_benefi_placas_video)}",

            "top de linha",
            f"Temos placas de vídeo como: { ', '.join(top_linha_placa_de_video)}",

            "Ops, não entendi"
        ]

    @staticmethod
    def processadores():
        
        store_bd = HardwareRepository()

        all_processadores = store_bd.processadores

        all_processadores_intel = store_bd.filter_list(
            conditional=lambda fabricante: fabricante == "INTEL",
            key_find="fabricante",
            values=all_processadores,
            key_return="name"
        )

        all_processadores_amd = store_bd.filter_list(
            conditional=lambda fabricante: fabricante == "AMD",
            key_find="fabricante",
            values=all_processadores,
            key_return="name"
        )

        return [
            "gostaria de um processador",
            "Intel ou amd?",
            
            "intel",
            f"Temos da intel: {', '.join(all_processadores_intel)}",
            "amd",
            f"Temos processadores da AMD {', '.join(all_processadores_amd)}"
        ]