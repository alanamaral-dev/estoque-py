estoque = []
registroDeVendas = []
caixa = 0

import json
import os

ARQUIVO_ESTOQUE = "estoque.json"
ARQUIVO_VENDAS = "vendas.json"
ARQUIVO = 'caixa.json'

def carregar_caixa():
    if os.path.exists("caixa.json"):
        with open("caixa.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)["caixa"]
    return 0.0

def salvar_caixa(caixa):
    with open("caixa.json", "w", encoding="utf-8") as arquivo:
        json.dump({"caixa": caixa}, arquivo, indent=4)
#============================================================================
def carregar(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)



estoque = carregar(ARQUIVO_ESTOQUE)
registroDeVendas = carregar(ARQUIVO_VENDAS)
caixa = carregar_caixa()
