import streamlit as st
import time
import pandas as pd

# Funzione per verificare le risposte
def verifica_risposta(risposta, corretta):
    return risposta.strip().lower() == corretta.strip().lower()

# Funzione per formattare il tempo in minuti e secondi
def formatta_tempo(tempo_totale):
    minuti = int(tempo_totale // 60)
    secondi = int(tempo_totale % 60)
    return f"{minuti}:{secondi:02d}"  # Formato MM:SS

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
        {"frase": "La penna del maestro è sul tavolo.", "soggetto": "La penna", "predicato": "è", "complemento_specificazione": "del maestro"},
        {"frase": "Il libro di Marco è interessante.", "soggetto": "Il libro", "predicato": "è interessante", "complemento_specificazione": "di Marco"},
        {"frase": "Il gatto di Lucia è bianco.", "soggetto": "Il gatto", "predicato": "è bianco", "complemento_specificazione": "di Lucia"},
        {"frase": "La penna di Paolo è nuova.", "soggetto": "La penna", "predicato": "è nuova", "complemento_specificazione": "di Paolo"},
        {"frase": "Il fiore del giardino è bello.", "soggetto": "Il fiore", "predicato": "è bello", "complemento_specificazione": "del giardino"}
    ],
    3: [
        {"frase": "La città di Roma è bella.", "soggetto": "La città", "predicato": "è bella", "complemento_denominazione": "di Roma"},
        {"frase": "Il lago di Garda è di origine glaciale.", "soggetto": "Il lago", "predicato": "è di origine glaciale", "complemento_denominazione": "di Garda"},
        {"frase": "Luca nuotò nel lago di Bracciano.", "soggetto": "Luca", "predicato": "nuotò", "complemento_denominazione": "di Bracciano"},
        {"frase": "Mario è della città di Bergamo.", "soggetto": "Mario", "predicato": "è", "complemento_denominazione": "di Bergamo"},
        {"frase": "La città di Venezia è una città lagunare.", "soggetto": "La città", "predicato": "è una città lagunare", "complemento_denominazione": "di Venezia"}
    ],
    4: [
        {"frase": "Marco regala un libro a Lucia.", "soggetto": "Marco", "predicato": "regala", "complemento_oggetto": "un libro", "complemento_termine": "a Lucia"},
        {"frase": "Il professore spiega la lezione agli studenti.", "soggetto": "Il professore", "predicato": "spiega", "complemento_oggetto": "la lezione", "complemento_termine": "agli studenti"},
        {"frase": "Io do un regalo a te.", "soggetto": "Io", "predicato": "do", "complemento_oggetto": "un regalo", "complemento_termine": "a te"},
        {"frase": "La mamma prepara la cena per la famiglia.", "soggetto": "La mamma", "predicato": "prepara", "complemento_oggetto": "la cena", "complemento_termine": "per la famiglia"},
        {"frase": "Il postino consegna una lettera a Maria.", "soggetto": "Il postino", "predicato": "consegna", "complemento_oggetto": "una lettera", "complemento_termine": "a Maria"}
    ],
    5: [
        {"frase": "La torta è stata mangiata da Marco.", "soggetto": "La torta", "predicato": "è stata mangiata", "complemento_agente": "da Marco"},
        {"frase": "Il libro è stato scritto da uno scrittore famoso.", "soggetto": "Il libro", "predicato": "è stato scritto", "complemento_agente": "da uno scrittore famoso"},
        {"frase": "La casa è stata costruita da un architetto.", "soggetto": "La casa", "predicato": "è stata costruita", "complemento_agente": "da un architetto"},
        {"frase": "La mela è stata colta da un contadino.", "soggetto": "La mela", "predicato": "è stata colta", "complemento_agente": "da un contadino"},
        {"frase": "Il disegno è stato fatto da un artista.", "soggetto": "Il disegno", "predicato": "è stato fatto", "complemento_agente": "da un artista"}
    ],
    6: [
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
    if "risposta_corretta" not in st.session_state:
        st.session_state.risposta_corretta = False

    # Mostra il cronometro in tempo reale
    cronometro = st.sidebar.empty()
    tempo_trascorso = time.time() - st.session_state.inizio
    if tempo_trascorso > 60:
        cronometro.write(f"⏱️ Tempo trascorso: {formatta_tempo(tempo_trascorso)}")
    else:
        cronometro.write(f"⏱️ Tempo trascorso: {int(tempo_trascorso)} secondi")

    livello = st.session_state.livello_corrente
    frase_idx = st.session_state.frase_corrente
    frase = livelli[livello][frase_idx]

    st.write(f"### Livello {livello}")
    st.write(f"**Frase:** {frase['frase']}")

    # Messaggi specifici per ogni livello
    if livello == 1:
        st.write("⚠️ **Nota:** In questo livello, il complemento presente è il **Complemento Oggetto**.")
    elif livello == 2:
        st.write("⚠️ **Nota:** In questo livello, il complemento presente è il **Complemento di Specificazione**.")
    elif livello == 3:
        st.write("⚠️ **Nota:** In questo livello, il complemento presente è il **Complemento di Denominazione**.")
    elif livello == 4:
        st.write("⚠️ **Nota:** In questo livello, i complementi presenti sono il **Complemento Oggetto** e il **Complemento di Termine**.")
    elif livello == 5:
        st.write("⚠️ **Nota:** In questo livello, il complemento presente è il **Complemento d'Agente o di Causa Efficiente**.")
    elif livello == 6:
        st.write("⚠️ **Nota:** In questo livello, il complemento presente è il **Complemento Predicativo del Soggetto o dell'Oggetto**.")

    # Input per soggetto e predicato
    soggetto = st.text_input("Soggetto:", key=f"soggetto_{livello}_{frase_idx}", value="")
    predicato = st.text_input("Predicato:", key=f"predicato_{livello}_{frase_idx}", value="")

    # Input per i complementi (gestione diversa per ogni livello)
    if livello == 2:
        complemento_specificazione = st.text_input("Complemento di Specificazione:", key=f"complemento_specificazione_{livello}_{frase_idx}", value="")
    elif livello == 3:
        complemento_denominazione = st.text_input("Complemento di Denominazione:", key=f"complemento_denominazione_{livello}_{frase_idx}", value="")
    elif livello == 4:
        complemento_oggetto = st.text_input("Complemento Oggetto:", key=f"complemento_oggetto_{livello}_{frase_idx}", value="")
        complemento_termine = st.text_input("Complemento di Termine:", key=f"complemento_termine_{livello}_{frase_idx}", value="")
    elif livello == 5:
        complemento_agente = st.text_input("Complemento d'Agente o di Causa Efficiente:", key=f"complemento_agente_{livello}_{frase_idx}", value="")
    elif livello == 6:
        complemento_predicativo = st.text_input("Complemento Predicativo del Soggetto o dell'Oggetto:", key=f"complemento_predicativo_{livello}_{frase_idx}", value="")

    if st.button("Verifica", key=f"verifica_{livello}_{frase_idx}"):
        if not verifica_risposta(soggetto, frase["soggetto"]):
            st.error("Soggetto errato! Riprova.")
        elif not verifica_risposta(predicato, frase["predicato"]):
            st.error("Predicato errato! Riprova.")
        elif livello == 2 and "complemento_specificazione" in frase and not verifica_risposta(complemento_specificazione, frase["complemento_specificazione"]):
            st.error("Complemento di specificazione errato! Riprova.")
        elif livello == 3 and "complemento_denominazione" in frase and not verifica_risposta(complemento_denominazione, frase["complemento_denominazione"]):
            st.error("Complemento di denominazione errato! Riprova.")
        elif livello == 4:
            if "complemento_oggetto" in frase and not verifica_risposta(complemento_oggetto, frase["complemento_oggetto"]):
                st.error("Complemento oggetto errato! Riprova.")
            elif "complemento_termine" in frase and not verifica_risposta(complemento_termine, frase["complemento_termine"]):
                st.error("Complemento di termine errato! Riprova.")
        elif livello == 5 and "complemento_agente" in frase and not verifica_risposta(complemento_agente, frase["complemento_agente"]):
            st.error("Complemento d'agente errato! Riprova.")
        elif livello == 6 and "complemento_predicativo" in frase and not verifica_risposta(complemento_predicativo, frase["complemento_predicativo"]):
            st.error("Complemento predicativo errato! Riprova.")
        else:
            st.success("Corretto! Complimenti.")
            st.session_state.risposta_corretta = True

    # Mostra il pulsante "Successiva" solo se la risposta è corretta
    if st.session_state.risposta_corretta:
        if st.button("Successiva", key=f"successiva_{livello}_{frase_idx}"):
            st.session_state.punteggio += 1
            st.session_state.frase_corrente += 1
            st.session_state.risposta_corretta = False

            # Passa alla frase successiva o al livello successivo
            if st.session_state.frase_corrente >= len(livelli[livello]):
                st.session_state.livello_corrente += 1
                st.session_state.frase_corrente = 0
                if st.session_state.livello_corrente > len(livelli):
                    fine = time.time()
                    tempo_totale = fine - st.session_state.inizio
                    st.write(f"### 🎉 Hai completato tutti i livelli in {formatta_tempo(tempo_totale)}!")
                    # Salva il punteggio nella classifica
                    if "classifica" not in st.session_state:
                        st.session_state.classifica = pd.DataFrame(columns=["Username", "Tempo"])
                    st.session_state.classifica = st.session_state.classifica.append(
                        {"Username": st.session_state.username, "Tempo": formatta_tempo(tempo_totale)}, ignore_index=True
                    )
                    st.write("### 🏆 Classifica")
                    st.write(st.session_state.classifica.sort_values(by="Tempo"))
                    if st.button("Ricomincia"):
                        st.session_state.livello_corrente = 1
                        st.session_state.frase_corrente = 0
                        st.session_state.punteggio = 0
                        st.session_state.inizio = time.time()
                        st.session_state.risposta_corretta = False
                        st.session_state.pagina_corrente = "username"  # Torna alla pagina iniziale
                    return
                st.balloons()  # Effetto visivo
                st.write(f"🎉 **Complimenti! Passi al livello {st.session_state.livello_corrente}.**")

# Interfaccia iniziale
st.title("🎮 Gioco di Analisi Logicaa")
st.write("Benvenuto! Inserisci il tuo username per iniziare.")

# Inizializza lo stato dell'app
if "pagina_corrente" not in st.session_state:
    st.session_state.pagina_corrente = "username"

# Pagina per l'inserimento dell'username
if st.session_state.pagina_corrente == "username":
    username = st.text_input("Username:")
    if st.button("Inizia il gioco"):
        if username and username.strip():  # Verifica che l'username non sia vuoto
            st.session_state.username = username.strip()
            st.session_state.pagina_corrente = "gioco"  # Passa alla pagina del gioco

# Pagina del gioco
if st.session_state.pagina_corrente == "gioco":
    gioco()
