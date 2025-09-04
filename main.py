import threading
import asyncio
import tkinter as tk
from tkinter import simpledialog
from interfaces import tkinter_app, flask_app, discord_bot, telegram_bot

def get_tokens_gui():
    
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    discord_token = simpledialog.askstring("Discord Token", "Digite a API Key do Discord:", parent=root)
    telegram_token = simpledialog.askstring("Telegram Token", "Digite a API Key do Telegram:", parent=root)

    root.destroy()  # Fecha a janela
    return discord_token, telegram_token

def start_all(start_discord_bot=False, start_telegram_bot=False):
    threads = []

    # Inicia interface Tkinter principal
    t_tk = threading.Thread(target=tkinter_app.start_tkinter, name='tkinter')
    threads.append(t_tk)

    # Inicia Flask
    t_flask = threading.Thread(
        target=lambda: flask_app.start_flask(host='127.0.0.1', port=5000, debug=False),
        name='flask'
    )
    threads.append(t_flask)

    # Solicita os tokens via GUI
    discord_token, telegram_token = None, None
    if start_discord_bot or start_telegram_bot:
        discord_token, telegram_token = get_tokens_gui()

    # Bot Discord
    if start_discord_bot and discord_token:
        t_disc = threading.Thread(
            target=lambda: discord_bot.start_discord(discord_token),
            name='discord'
        )
        threads.append(t_disc)

    # Bot Telegram
    if start_telegram_bot and telegram_token:
        t_tel = threading.Thread(
            target=lambda: asyncio.run(telegram_bot.start_telegram(telegram_token)),
            name='telegram'
        )
        threads.append(t_tel)

    # Inicia todas as threads
    for t in threads:
        t.daemon = True
        t.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Encerrando...')

if __name__ == '__main__':
    start_all(start_discord_bot=True, start_telegram_bot=True)
