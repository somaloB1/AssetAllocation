import streamlit as st
import yfinance as yf

# import matplotlib.pyplot as plt






st.title("📈 Prezzi Azioni con yfinance")

ticker = st.text_input("Inserisci ticker (es. AAPL, MSFT, ENI.MI)", "AAPL")

if ticker:
    data = yf.download(ticker, period="6mo")
    st.line_chart(data["Close"])
    st.write("Ultimi dati:", data.tail())
    


#seleziono le prime 4 colonne
df_to_plot = data.iloc[:, :4]
#grafico
df_to_plot.plot()
#plt.title("Grafico delle prime 4 colonne")
#plt.xlabel("Indice")
#plt.ylabel("Valore")
#plt.show()    



# app.py
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="📈 Prezzi e Dividendi Azioni", layout="wide")
st.title("📊 Prezzi e Dividendi delle Azioni")

# Input del ticker
ticker_input = st.text_input("Inserisci ticker (es. AAPL, MSFT, ENI.MI)", "AAPL")

if ticker_input:
    # Scarica dati ultimi 6 mesi
    data = yf.Ticker(ticker_input)
    hist = data.history(period="6mo")
    
    if hist.empty:
        st.warning("Ticker non trovato o nessun dato disponibile")
    else:
        # Prezzi
        st.subheader("📈 Grafico Prezzi di Chiusura")
        st.line_chart(hist["Close"])
        
        # Dividendi
        div = data.dividends
        if div.empty:
            st.info("Nessun dividendo negli ultimi mesi")
        else:
            st.subheader("💰 Dividendi")
            div_df = pd.DataFrame(div)
            div_df.columns = ["Dividendo"]
            st.bar_chart(div_df)
            
            # Mostra tabella dividendi
            st.write("Tabella dividendi:", div_df)

        # Mostra ultime righe dei dati
        st.subheader("Ultimi dati disponibili")
        st.dataframe(hist.tail(5))
