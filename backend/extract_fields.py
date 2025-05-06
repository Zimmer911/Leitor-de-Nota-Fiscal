import re

def extract_fields(texto):
    campos = {
        # Aceita CNPJs com ou sem pontuação
        "cnpjs": re.findall(r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}", texto),

        # Datas continuam igual
        "datas": re.findall(r"\d{2}/\d{2}/\d{4}", texto),

        # Valores agora aceitam R$ seguido de número com ou sem vírgula/ponto
        "valores": re.findall(r"R\$ ?\d+(?:[\.,]\d{2})?", texto)
    }
    return campos
