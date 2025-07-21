from telegram import Bot
from analise import carregar_jogos, gerar_mensagem
from publicador_utils import jogos_relevantes
import settings
import time

def publicar_analises():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    canal = settings.CHANNEL_ID

    jogos = carregar_jogos()
    selecionados = jogos_relevantes(jogos)

    if not selecionados:
        print("[INFO] Nenhum jogo das principais ligas nas próximas 1h.")
        return

    for jogo in selecionados:
        msg = gerar_mensagem(jogo)
        bot.send_message(chat_id=canal, text=msg)
        print(f"[PUBLICADO] {jogo.nome}")

if __name__ == "__main__":
    while True:
        try:
            print("[PUBLICADOR] A verificar jogos...")
            publicar_analises()
        except Exception as e:
            print(f"[ERRO] {e}")
        time.sleep(1800)  # Espera 30 min e repete
