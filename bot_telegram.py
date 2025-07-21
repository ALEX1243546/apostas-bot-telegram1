from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from analise import carregar_jogos, gerar_mensagem
from cache import salvar_jogos, carregar_jogos_do_cache
import settings
import schedule
import time
import threading
import os

CAMINHO_CACHE = "jogos_cache.json"

def limpar_cache():
    if os.path.exists(CAMINHO_CACHE):
        os.remove(CAMINHO_CACHE)
        print("[CACHE] Arquivo de cache removido às 00:00")

def iniciar_agendador():
    schedule.every().day.at("00:00").do(limpar_cache)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(60)

    t = threading.Thread(target=loop, daemon=True)
    t.start()

def atualizar(update: Update, context: CallbackContext):
    update.message.reply_text("🔄 Atualizando jogos da API...")
    try:
        jogos = carregar_jogos()
        salvar_jogos(jogos)
        update.message.reply_text(f"✅ Atualizado com {len(jogos)} jogos.")
    except Exception as e:
        update.message.reply_text(f"❌ Erro ao atualizar: {e}")

def analisar(update: Update, context: CallbackContext):
    jogos = carregar_jogos_do_cache()
    if not jogos:
        update.message.reply_text("⚠️ Nenhum jogo disponível. Usa /atualizar primeiro.")
        return

    if not context.args:
        update.message.reply_text("❗ Usa: /analisar <nome do jogo>")
        return

    termo = " ".join(context.args).lower()
    filtrados = [j for j in jogos if termo in j.nome.lower()]

    if not filtrados:
        update.message.reply_text(f"🔍 Jogo '{termo}' não encontrado.")
        return

    for jogo in filtrados:
        msg = gerar_mensagem(jogo)
        update.message.reply_text(msg)

def listar(update: Update, context: CallbackContext):
    jogos = carregar_jogos_do_cache()
    if not jogos:
        update.message.reply_text("⚠️ Nenhum jogo disponível.")
        return

    nomes = "\n".join([f"• {j.nome} ({j.liga})" for j in jogos])
    update.message.reply_text(f"📅 Jogos disponíveis:\n\n{nomes}")

def main():
    updater = Updater(settings.TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("atualizar", atualizar))
    dp.add_handler(CommandHandler("analisar", analisar))
    dp.add_handler(CommandHandler("listar", listar))

    iniciar_agendador()

    print("[BOT] A iniciar polling...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
