import os
import requests
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Jogo:
    nome: str
    data: datetime
    liga: str
    estatisticas: dict

API_URL = "https://api.football-data.org/v4/matches"
HEADERS = {"X-Auth-Token": os.getenv("API_FOOTBALL_DATA")}


def carregar_jogos():
    response = requests.get(API_URL, headers=HEADERS, params={"status": "SCHEDULED"})
    if response.status_code != 200:
        print("Erro ao buscar jogos da API:", response.text)
        return []

    data = response.json()
    jogos = []

    for m in data.get("matches", []):
        comp = m.get("competition", {}).get("name", "Desconhecida")
        utc = m.get("utcDate")
        dt = datetime.fromisoformat(utc.replace("Z", "+00:00"))
        nome = f"{m['homeTeam']['name']} vs {m['awayTeam']['name']}"

        jogos.append(
            Jogo(
                nome=nome,
                data=dt,
                liga=comp,
                estatisticas={"golos": "-", "cantos": "-"}  # API gratuita não inclui estatísticas completas
            )
        )

    return jogos
