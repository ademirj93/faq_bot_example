# core/faq_engine.py
from .faq_data import faq, keywords_map

def normalize(text: str) -> str:
    return (text or "").lower().strip()

def get_answer(question: str) -> str:
    """Retorna a resposta correspondente à pergunta.

    Estratégia:
    1. tentativa de match exato (chave completa)
    2. tentativa por keyword (palavra-chave simples)
    3. fallback padrão
    """
    q = normalize(question)
    if not q:
        return "Por favor, digite uma pergunta."

    # 1) match exato
    if q in faq:
        return faq[q]

    # 2) busca por keyword
    for kw, mapped in keywords_map.items():
        if kw in q:
            return faq.get(mapped, "Desculpe, não tenho uma resposta para isso.")

    # 3) busca por aproximação: procurar se alguma chave aparece em q
    for key, ans in faq.items():
        if key in q:
            return ans

    return "Desculpe, não tenho resposta para essa pergunta."