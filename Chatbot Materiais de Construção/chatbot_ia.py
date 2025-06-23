# chatbot_ia.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from faq_data import faq_data

# Carregar o modelo de embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # leve e eficiente

# Extrair apenas as perguntas do FAQ
faq_questions = [item["question"] for item in faq_data]

# Gerar embeddings para todas as perguntas do FAQ
faq_embeddings = model.encode(faq_questions)

def responder_pergunta(pergunta_usuario):
    # Gerar embedding da pergunta do usuário
    pergunta_embedding = model.encode([pergunta_usuario])

    # Calcular similaridade de cosseno entre a pergunta do usuário e o FAQ
    similaridades = cosine_similarity(pergunta_embedding, faq_embeddings)[0]

    # Identificar a pergunta mais semelhante
    indice_mais_proximo = np.argmax(similaridades)
    similaridade_maxima = similaridades[indice_mais_proximo]

    # Definir um limiar de confiança (threshold)
    if similaridade_maxima < 0.6:
        return "Desculpe, não encontrei uma resposta adequada. Você poderia reformular a pergunta?"

    return faq_data[indice_mais_proximo]["answer"]

if __name__ == "__main__":
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Chatbot: Até mais!")
            break
        resposta = responder_pergunta(pergunta)
        print("Chatbot:", resposta)