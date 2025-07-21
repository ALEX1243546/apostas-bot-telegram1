from datetime import datetime, timedelta

PRINCIPAIS_LIGAS = [
    "Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"
]

def jogos_relevantes(jogos):
    agora = datetime.now()
    limite = agora + timedelta(hours=1)
    return [
        j for j in jogos
        if agora < j.data <= limite and j.liga in PRINCIPAIS_LIGAS
    ]
