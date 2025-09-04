# core/faq_engine.py
from .faq_data import faq, keywords_map

def normalize(text: str) -> str:
    return (text or "").lower().strip()

def get_answer(question: str) -> str:
    q = normalize(question)
    if not q:
        return "Por favor, digite uma pergunta."

    if q in faq:
        return faq[q]

    for kw, mapped in keywords_map.items():
        if kw in q:
            return faq.get(mapped, "Desculpe, não tenho uma resposta para isso.")

    for key, ans in faq.items():
        if key in q:
            return ans

    return "Desculpe, não tenho resposta para essa pergunta."
