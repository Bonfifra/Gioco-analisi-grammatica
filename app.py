import streamlit as st
import time

# Definizione delle frasi e delle risposte corrette per ogni livello
livelli = {
    1: [
        {"frase": "Il cane abbaia.", "soggetto": "Il cane", "predicato": "abbaia"},
        {"frase": "La mela è rossa.", "soggetto": "La mela", "predicato": "è rossa"},
    ],
    2: [
        {"frase": "Il libro di Marco è interessante.", "soggetto": "Il libro", "predicato": "è interessante", "complemento_specificazione": "di Marco"},
    ],
}

def verifica_risposta(risposta, corretta):
    return risposta.strip().lower() == corretta.strip().lower()

def mostra_frase(frase):
    st.write(f"**Frase:** {frase['frase']}")
    soggetto = st.text_input("Soggetto:")
    predicato = st.text_input("Predicato:")
    complemento = st.text_input("Complemento (se presente):")
    if st.button("Verifica"):
        if verifica_risposta(soggetto, frase["soggetto"]) and verifica_risposta(predicato, frase["predicato"]):
            st.success("Corretto! Complimenti.")
        else:
            st.error("Risposta errata. Riprova.")

livello = st.sidebar.selectbox("Seleziona il livello", list(livelli.keys()))
frase_idx = st.sidebar.number_input("Frase", min_value=0, max_value=len(livelli[livello])-1, value=0)
mostra_frase(livelli[livello][frase_idx])
