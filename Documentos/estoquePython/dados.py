estoque = []
registroDeVendas = []
caixa = 0

import json
import os

ARQUIVO = 'estoque.json'

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar():
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

estoque = carregar()
caixa = carregar()
