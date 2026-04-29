#for run that app, use command: 
# C:\Users\Wans\AppData\Roaming\Python\Python313\Scripts\streamlit.exe run app.py
#if and so if u have streamlit in your python env.

#this app running on localhost 8501



import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.set_page_config(page_title="Dashboard", layout="wide")

st.title(" Dashboard E-commerce")

# KPI
col1, col2, col3 = st.columns(3)

clients = pd.read_sql("SELECT COUNT(*) as total FROM clients", conn)
commandes = pd.read_sql("SELECT COUNT(*) as total FROM commandes", conn)
ca = pd.read_sql("SELECT SUM(montant) as total FROM commandes", conn)

col1.metric(" Clients", clients["total"][0])
col2.metric(" Commandes", commandes["total"][0])
col3.metric("CA", int(ca["total"][0] or 0))

# Graph commandes
cmd_jour = pd.read_sql("""
SELECT DATE(date_commande) as date, COUNT(*) as total
FROM commandes
GROUP BY date
ORDER BY date
""", conn)

st.subheader("📈 Commandes par jour")
st.line_chart(cmd_jour.set_index("date"))

# Top produits
top = pd.read_sql("""
SELECT p.nom, SUM(cd.quantite) as total
FROM commande_details cd
JOIN produit_variants pv ON cd.produit_variant_id = pv.id
JOIN produits p ON pv.produit_id = p.id
GROUP BY p.nom
ORDER BY total DESC
LIMIT 10
""", conn)

st.subheader("🔥 Top produits")
st.bar_chart(top.set_index("nom"))