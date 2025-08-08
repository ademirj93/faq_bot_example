import threading
import os
from interfaces import tkinter_app, flask_app
from interfaces import discord_bot, telegram_bot


def start_all(simultaneous=True, start_discord_bot=False, start_telegram_bot=False):
    threads = []

    # Tkinter (tem que rodar na thread principal em algumas plataformas; funciona em thread separada
    # na maioria dos casos, mas se der problema, execute tkinter sozinho)
    t_tk = threading.Thread(target=tkinter_app.start_tkinter, name='tkinter')
    threads.append(t_tk)

    # Flask
    t_flask = threading.Thread(target=lambda: flask_app.start_flask(host='127.0.0.1', port=5000, debug=False), name='flask')
    threads.append(t_flask)

    # Discord (opcional)
    if start_discord_bot:
        discord_token = os.getenv('DISCORD_TOKEN') or 'SEU_TOKEN_DISCORD'
        t_disc = threading.Thread(target=lambda: discord_bot.start_discord(discord_token), name='discord')
        threads.append(t_disc)

    # Telegram (opcional)
    if start_telegram_bot:
        telegram_token = os.getenv('TELEGRAM_TOKEN') or 'SEU_TOKEN_TELEGRAM'
        t_tel = threading.Thread(target=lambda: telegram_bot.start_telegram(telegram_token), name='telegram')
        threads.append(t_tel)

    # Start threads
    for t in threads:
        t.daemon = True
        t.start()

    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Encerrando...')

if __name__ == '__main__':
    # altere os flags abaixo conforme quiser iniciar bots
    start_all(simultaneous=True, start_discord_bot=False, start_telegram_bot=False)