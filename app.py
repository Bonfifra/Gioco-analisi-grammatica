import streamlit as st
import time
import pandas as pd

# Funzione per verificare le risposte
def verifica_risposta(risposta, corretta):
    return risposta.strip().lower() == corretta.strip().lower()

# Definizione delle frasi per ogni livello
livelli = {
    1: [
        {"frase": "Il cane abbaia.", "soggetto": "Il cane", "predicato": "abbaia"},
        {"frase": "La mela è rossa.", "soggetto": "La mela", "predicato": "è rossa"},
        {"frase": "Marco legge un libro.", "soggetto": "Marco", "predicato": "legge", "complemento_oggetto": "un libro"},
        {"frase": "Il sole splende.", "soggetto": "Il sole", "predicato": "splende"},
        {"frase": "La torta è deliziosa.", "soggetto": "La torta", "predicato": "è deliziosa"}
    ],
    2: [
        {"frase": "Il libro di Marco è interessante.", "soggetto": "Il libro", "predicato": "è interessante", "complemento_specificazione": "di Marco"},
        {"frase": "La città di Roma è antica.", "soggetto": "La città", "predicato": "è antica", "complemento_specificazione": "di Roma"},
        {"frase": "Il gatto di Lucia è bianco.", "soggetto": "Il gatto", "predicato": "è bianco", "complemento_specificazione": "di Lucia"},
        {"frase": "La penna di Paolo è nuova.", "soggetto": "La penna", "predicato": "è nuova", "complemento_specificazione": "di Paolo"},
        {"frase": "Il fiore del giardino è bello.", "soggetto": "Il fiore", "predicato": "è bello", "complemento_specificazione": "del giardino"}
    ],
    3: [
        {"frase": "Marco regala un libro a Lucia.", "soggetto": "Marco", "predicato": "regala", "complemento_oggetto": "un libro", "complemento_termine": "a Lucia"},
        {"frase": "Il professore spiega la lezione agli studenti.", "soggetto": "Il professore", "predicato": "spiega", "complemento_oggetto": "la lezione", "complemento_termine": "agli studenti"},
        {"frase": "Io do un regalo a te.", "soggetto": "Io", "predicato": "do", "complemento_oggetto": "un regalo", "complemento_termine": "a te"},
        {"frase": "La mamma prepara la cena per la famiglia.", "soggetto": "La mamma", "predicato": "prepara", "complemento_oggetto": "la cena", "complemento_termine": "per la famiglia"},
        {"frase": "Il postino consegna una lettera a Maria.", "soggetto": "Il postino", "predicato": "consegna", "complemento_oggetto": "una lettera", "complemento_termine": "a Maria"}
    ],
    4: [
        {"frase": "La torta è stata mangiata da Marco.", "soggetto": "La torta", "predicato": "è stata mangiata", "complemento_agente": "da Marco"},
        {"frase": "Il libro è stato scritto da uno scrittore famoso.", "soggetto": "Il libro", "predicato": "è stato scritto", "complemento_agente": "da uno scrittore famoso"},
        {"frase": "La casa è stata costruita da un architetto.", "soggetto": "La casa", "predicato": "è stata costruita", "complemento_agente": "da un architetto"},
        {"frase": "La mela è stata colta da un contadino.", "soggetto": "La mela", "predicato": "è stata colta", "complemento_agente": "da un contadino"},
        {"frase": "Il disegno è stato fatto da un artista.", "soggetto": "Il disegno", "predicato": "è stato fatto", "complemento_agente": "da un artista"}
    ],
    5: [
        {"frase": "Marco è considerato un genio.", "soggetto": "Marco", "predicato": "è considerato", "complemento_predicativo": "un genio"},
        {"frase": "La torta sembra deliziosa.", "soggetto": "La torta", "predicato": "sembra", "complemento_predicativo": "deliziosa"},
        {"frase": "Il professore ha nominato Lucia rappresentante.", "soggetto": "Il professore", "predicato": "ha nominato", "complemento_oggetto": "Lucia", "complemento_predicativo": "rappresentante"},
        {"frase": "I ragazzi hanno eletto Marco capogruppo.", "soggetto": "I ragazzi", "predicato": "hanno eletto", "complemento_oggetto": "Marco", "complemento_predicativo": "capogruppo"},
        {"frase": "La mamma ha trovato la casa accogliente.", "soggetto": "La mamma", "predicato": "ha trovato", "complemento_oggetto": "la casa", "complemento_predicativo": "accogliente"}
    ]
}

# Funzione principale del gioco
def gioco():
    if "livello_corrente" not in st.session_state:
        st.session_state.livello_corrente = 1
    if "frase_corrente" not in st.session_state:
        st.session_state.frase_corrente = 0
    if "punteggio" not in st.session_state:
        st.session_state.punteggio = 0
    if "inizio" not in st.session_state:
        st.session_state.inizio = time.time()

    livello = st.session_state.livello_corrente
    frase_idx = st.session_state.frase_corrente
    frase = livelli[livello][frase_idx]

    st.write(f"### Livello {livello}")
    st.write(f"**Frase:** {frase['frase']}")

    soggetto = st.text_input("Soggetto:", key=f"soggetto_{livello}_{frase_idx}")
    predicato = st.text_input("Predicato:", key=f"predicato_{livello}_{frase_idx}")
    complemento = st.text_input("Complemento (se presente):", key=f"complemento_{livello}_{frase_idx}")

    if st.button("Verifica", key=f"verifica_{livello}_{frase_idx}"):
        if not verifica_risposta(soggetto, frase["soggetto"]):
            st.error("Soggetto errato! Riprova.")
        elif not verifica_risposta(predicato, frase["predicato"]):
            st.error("Predicato errato! Riprova.")
        elif "complemento_oggetto" in frase and not verifica_risposta(complemento, frase["complemento_oggetto"]):
            st.error("Complemento oggetto errato! Riprova.")
        elif "complemento_specificazione" in frase and not verifica_risposta(complemento, frase["complemento_specificazione"]):
            st.error("Complemento di specificazione errato! Riprova.")
        elif "complemento_termine" in frase and not verifica_risposta(complemento, frase["complemento_termine"]):
            st.error("Complemento di termine errato! Riprova.")
        elif "complemento_agente" in frase and not verifica_risposta(complemento, frase["complemento_agente"]):
            st.error("Complemento d'agente errato! Riprova.")
        elif "complemento_predicativo" in frase and not verifica_risposta(complemento, frase["complemento_predicativo"]):
            st.error("Complemento predicativo errato! Riprova.")
        else:
            st.success("Corretto! Complimenti.")
            st.session_state.punteggio += 1
            st.session_state.frase_corrente += 1

            if st.session_state.frase_corrente >= len(livelli[livello]):
                st.session_state.livello_corrente += 1
                st.session_state.frase_corrente = 0
                if st.session_state.livello_corrente > len(livelli):
                    fine = time.time()
                    tempo_totale = fine - st.session_state.inizio
                    st.write(f"### 🎉 Hai completato tutti i livelli in {tempo_totale:.2f} secondi!")
                    
                    # Salva il punteggio nella classifica
                    if "classifica" not in st.session_state:
                        st.session_state.classifica = pd.DataFrame(columns=["Username", "Tempo"])
                    st.session_state.classifica = st.session_state.classifica.append(
                        {"Username": st.session_state.username, "Tempo": tempo_totale}, ignore_index=True
                    )
                    st.write("### 🏆 Classifica")
                    st.write(st.session_state.classifica.sort_values(by="Tempo"))
                    return

                st.write(f"Complimenti! Passi al livello {st.session_state.livello_corrente}.")

# Interfaccia iniziale
st.title("🎮 Gioco di Analisi Logica")
st.write("Benvenuto! Inserisci il tuo username per iniziare.")

if "username" not in st.session_state:
    username = st.text_input("Username:")
    if username:
        st.session_state.username = username
        st.experimental_rerun()  # Ricarica l'app per avviare il gioco
else:
    gioco()
