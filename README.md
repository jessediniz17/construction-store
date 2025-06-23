
💬 FAQ Chatbot for Construction Store

This project is part of a college assignment where I developed a website for a construction materials store. As part of its update, I implemented an FAQ chatbot to strengthen my AI development skills.

🧠 About the Project

The chatbot was built using Python and the sentence-transformers library to generate text embeddings. A predefined list of FAQs is available, and the chatbot compares user input to these questions using cosine similarity (via scikit-learn). If the similarity score is 60% or higher, the chatbot returns the related answer. Otherwise, it replies that no appropriate answer was found.

🖥️ Technologies Used

Python

sentence-transformers – for generating text embeddings

scikit-learn (sklearn) – for cosine similarity calculations

Streamlit – for building the interactive web interface

Streamlit Session State – to store and display conversation history

⚙️ Key Features

Real-time FAQ chatbot

Embedding-based similarity matching

Interactive UI with chat history

Easy to expand with more questions and answers

🚀 How to Use

Clone the repository

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py


____________________________________________________

💬 Chatbot de FAQ para Loja de Materiais de Construção

Este projeto faz parte de um trabalho da faculdade em que desenvolvi um site para uma loja de materiais de construção. Como parte da atualização do sistema, implementei um chatbot de FAQ com o objetivo de aprimorar minhas habilidades em desenvolvimento de projetos de IA.

🧠 Sobre o Projeto

O chatbot foi desenvolvido em Python, utilizando a biblioteca sentence-transformers para gerar embeddings de texto. Há uma lista de perguntas e respostas pré-definidas, e o chatbot compara a entrada do usuário com essas perguntas utilizando similaridade de cosseno (com a biblioteca scikit-learn). Se a similaridade for igual ou maior que 60%, o chatbot retorna a resposta correspondente. Caso contrário, informa que não encontrou uma resposta adequada.

🖥️ Tecnologias Utilizadas

Python

sentence-transformers – para geração de embeddings de texto

scikit-learn (sklearn) – para cálculo de similaridade de cosseno

Streamlit – para criação da interface web interativa

Streamlit Session State – para armazenar e exibir o histórico de conversas

⚙️ Funcionalidades Principais

Chatbot de FAQ em tempo real

Correspondência baseada em embeddings

Interface interativa com histórico da conversa

Fácil expansão com novas perguntas e respostas

🚀 Como Usar

Clone o repositório

Instale as dependências:
pip install -r requirements.txt

Execute o app com Streamlit:
streamlit run app.py

