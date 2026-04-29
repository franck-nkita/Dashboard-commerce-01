import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.title(" Stocks")

stocks = pd.read_sql("""
SELECT pv.id, SUM(s.quantite) as total
FROM stocks s
JOIN produit_variants pv ON s.produit_variant_id = pv.id
GROUP BY pv.id
""", conn)

st.dataframe(stocks)

# Alertes
alert = stocks[stocks["total"] < 10]

st.subheader(" Stock faible")
st.dataframe(alert)