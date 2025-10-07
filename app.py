import streamlit as st
import yfinance as yf

import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
from scipy.stats import linregress



st.title("📈 Prezzi Azioni con yfinance")

ticker = st.text_input("Inserisci ticker (es. AAPL, MSFT, ENI.MI)", "ENI.MI")

if ticker:
    data = yf.download(ticker, period="10y")
    st.line_chart(data["Close"])
    st.write("Ultimi dati:", data.tail())
    df_to_plot = data.iloc[:, :4]
    df_to_plot.plot()


#seleziono le prime 4 colonne

#grafico

#plt.title("Grafico delle prime 4 colonne")
#plt.xlabel("Indice")
#plt.ylabel("Valore")
#plt.show()    



results = {}

x = np.arange(len(df_to_plot))  # tempo come regressore
fits = {}
for col in df_to_plot.columns:
    slope, intercept, r_value, p_value, std_err = linregress(x, df_to_plot[col])
    results[col] = {
        "slope": slope,
        "intercept": intercept,
        "r2": r_value**2
    }

    y_fit = intercept + slope * x
    fits[col] = y_fit
    plt.plot(df_to_plot.index, y_fit, "-", label=f"Fit {col}")
    
res_df = pd.DataFrame(results).T
print(res_df)



# # app.py
# import streamlit as st
# import yfinance as yf
# import pandas as pd

# st.set_page_config(page_title="📈 Prezzi e Dividendi Azioni", layout="wide")
# st.title("📊 Prezzi e Dividendi delle Azioni")

# # Input del ticker
# ticker_input = st.text_input("Inserisci ticker (es. AAPL, MSFT, ENI.MI)", "AAPL")

# if ticker_input:
#     # Scarica dati ultimi 6 mesi
#     data = yf.Ticker(ticker_input)
#     hist = data.history(period="6mo")
    
#     if hist.empty:
#         st.warning("Ticker non trovato o nessun dato disponibile")
#     else:
#         # Prezzi
#         st.subheader("📈 Grafico Prezzi di Chiusura")
#         st.line_chart(hist["Close"])
        
#         # Dividendi
#         div = data.dividends
#         if div.empty:
#             st.info("Nessun dividendo negli ultimi mesi")
#         else:
#             st.subheader("💰 Dividendi")
#             div_df = pd.DataFrame(div)
#             div_df.columns = ["Dividendo"]
#             st.bar_chart(div_df)
            
#             # Mostra tabella dividendi
#             st.write("Tabella dividendi:", div_df)

#         # Mostra ultime righe dei dati
#         st.subheader("Ultimi dati disponibili")
#         st.dataframe(hist.tail(5))
