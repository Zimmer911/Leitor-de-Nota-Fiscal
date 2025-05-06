import re

def extract_fields(text):
    """
    Função para extrair campos relevantes de um texto:
    - CNPJs (com ou sem formatação)
    - Datas no formato dd/mm/aaaa
    - Valores monetários precedidos de R$
    """

    data = {
        # Regex para encontrar CNPJs com ou sem formatação:
        # Ex: 12.345.678/0001-90 ou 12345678000190
        "cnpjs": re.findall(r'\d{2}[.\-]?\d{3}[.\-]?\d{3}[\/]?\d{4}[\-]?\d{2}', text),

        # Regex para encontrar datas no formato: 01/01/2024
        "datas": re.findall(r'\d{2}/\d{2}/\d{4}', text),

        # Regex para encontrar valores como R$1200, R$ 1.200,00 etc
        "valores": re.findall(r'R\$ ?\d{1,3}(?:\.\d{3})*,?\d{2}', text)
    }

    return data
