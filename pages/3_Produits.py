import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.title(" Produits")

produits = pd.read_sql("SELECT * FROM produits LIMIT 100", conn)
st.dataframe(produits)

top = pd.read_sql("""
SELECT p.nom, SUM(cd.quantite) as total
FROM commande_details cd
JOIN produit_variants pv ON cd.produit_variant_id = pv.id
JOIN produits p ON pv.produit_id = p.id
GROUP BY p.nom
ORDER BY total DESC
LIMIT 10
""", conn)

st.subheader("🔥 Produits populaires")
st.bar_chart(top.set_index("nom"))