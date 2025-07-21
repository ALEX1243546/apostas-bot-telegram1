# Bot de Análise de Jogos - Telegram

Este bot responde ao comando `/analisar <jogo>` no Telegram com uma análise automática.

## Como usar no Railway

1. Suba os arquivos deste projeto para um repositório GitHub **ou ZIP para Railway**.
2. No painel do Railway, vá em Variables e adicione:

- `TELEGRAM_TOKEN`: o token real do bot

3. O Railway rodará automaticamente o bot com o comando:

```
python3 bot_telegram.py
```

E o bot ficará online 24/7, pronto para responder aos teus comandos no Telegram.