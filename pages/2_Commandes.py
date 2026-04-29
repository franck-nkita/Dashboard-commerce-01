import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.title(" Commandes")

cmd = pd.read_sql("""
SELECT c.id, cl.nom, c.date_commande, c.montant, c.statut
FROM commandes c
JOIN clients cl ON c.client_id = cl.id
ORDER BY c.date_commande DESC
LIMIT 100
""", conn)

st.dataframe(cmd)

# Statuts
statut = pd.read_sql("""
SELECT statut, COUNT(*) as total
FROM commandes
GROUP BY statut
""", conn)

st.subheader(" Commandes par statut")
st.bar_chart(statut.set_index("statut"))