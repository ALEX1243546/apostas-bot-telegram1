import json
from analise import Jogo
from datetime import datetime

CAMINHO_CACHE = "jogos_cache.json"

def salvar_jogos(jogos):
    with open(CAMINHO_CACHE, "w", encoding="utf-8") as f:
        json.dump([j.__dict__ for j in jogos], f, default=str, indent=2)

def carregar_jogos_do_cache():
    try:
        with open(CAMINHO_CACHE, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [
                Jogo(
                    nome=j["nome"],
                    data=datetime.fromisoformat(j["data"]),
                    liga=j["liga"],
                    estatisticas=j["estatisticas"]
                )
                for j in dados
            ]
    except FileNotFoundError:
        return []
