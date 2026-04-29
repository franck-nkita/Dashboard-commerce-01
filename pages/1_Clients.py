import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.title(" Clients")

clients = pd.read_sql("SELECT * FROM clients LIMIT 100", conn)

st.dataframe(clients)

# Analyse par ville
ville = pd.read_sql("""
SELECT ville, COUNT(*) as total
FROM adresses_clients
GROUP BY ville
ORDER BY total DESC
LIMIT 10
""", conn)

st.subheader("📍 Répartition par ville")
st.bar_chart(ville.set_index("ville"))