import tkinter as tk
from core.faq_engine import get_answer

def start_tkinter():
    root = tk.Tk()
    root.title("FAQ Jogos - Desktop")
    root.geometry("600x500")

    frame = tk.Frame(root, padx=12, pady=12)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Pergunta:").pack(anchor="w")
    tk.Label(frame, text="Perguntas programadas:").pack(anchor="w")
    tk.Label(frame, text="qual o melhor jogo de 2024 , quando sai gta 6, quais plataformas recomendadas").pack(anchor="w")
    pergunta_entry = tk.Entry(frame, width=60)
    pergunta_entry.pack(fill="x")

    resposta_text = tk.Text(frame, wrap="word", height=8)
    resposta_text.pack(fill="both", expand=True, pady=(8,0))

    def on_respond():
        pergunta = pergunta_entry.get()
        resposta = get_answer(pergunta)
        resposta_text.delete("1.0", tk.END)
        resposta_text.insert(tk.END, resposta)

    btn = tk.Button(frame, text="Responder", command=on_respond)
    btn.pack(pady=(8,0))

    root.mainloop()

if __name__ == "__main__":
    start_tkinter()
