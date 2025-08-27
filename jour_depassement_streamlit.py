import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime 
import streamlit as st

df = pd.read_excel("C:/Users/buket/Desktop/Epitech/projet_depassement_terre/donnees_propres_streamlit.xlsx")

df.rename(columns={
    "Unnamed: 0": "Country",
    "Ecological Footprint of Production (global hectares per person)": "Ecological Footprint of Production",
    "Ecological Footprint of Consumption (global hectares per person)": "Ecological Footprint of Consumption",
    "Biocapacity (global hectares per person)": "Biocapacity",
    "Year": "Year"
}, inplace=True)

df = df.drop(index=0) # pour supprimer une ligne 

df["Jour_deficit"] = 365 * (df["Biocapacity"] / (df["Ecological Footprint of Production"] + df["Ecological Footprint of Consumption"]))

df["Year"] = df["Year"].astype(int)

df["Date_deficit"] = df.apply(
    lambda row: pd.Timestamp(row["Year"], 1, 1) + pd.to_timedelta(row["Jour_deficit"], unit="D"),
    axis=1
)
df["Date_deficit"] = df["Date_deficit"].dt.date # pour arrêter d'afficher l'heure et juste avoir la date 

df["Jour_depassement"] = 365 * (1.5 / (df["Ecological Footprint of Production"] + df["Ecological Footprint of Consumption"])) # le 1.5 fait ici référence à la biocapacité mondiale en 2022 et 2024 c'est la même

df["Date_depassement"] = df.apply(
    lambda row: pd.Timestamp(row["Year"], 1, 1) + pd.to_timedelta(row["Jour_depassement"], unit="D"),
    axis=1
)

df["Date_depassement"] = df["Date_depassement"].dt.date # pour arrêter d'afficher l'heure

df["Date_depassement"] = pd.to_datetime(df["Date_depassement"])  # transforme en format datetime pour matplotlib 

df = df.drop(index=1) # pour supprimer la ligne sur les données de la terre 

print(df)

df_sorted = df.sort_values("Date_depassement")

top10 = df_sorted.head(10)
bottom10 = df_sorted.tail(10)

df_visu = pd.concat([top10, bottom10]) # pour voir les 10 premiers et 10 derniers pays 

# Pour Streamlite

st.title("Visualisation du jour de dépassement par pays")

# Pour selectionner une année
annee = sorted(df["Year"].unique())
annee_selectionnee = st.sidebar.selectbox("Choisissez une année :", annee)

# Pour filtrer les données selon l'année 
df_filtrer = df[df["Year"] == annee_selectionnee]

# Pour selectionner un pays 
pays_dispos = sorted(df["Country"].unique())
pays_selectionnee = st.sidebar.multiselect("Choisissez un ou plusieurs pays :", pays_dispos, default=pays_dispos[:5])

# Pour filtrer les donnes selon le pays 
df_filtre = df_filtrer[df_filtrer["Country"].isin(pays_selectionnee)]

fig, ax = plt.subplots(figsize=(20, 10)) # taille du graphique 

ax.barh(df_filtre["Country"], pd.to_datetime(df_filtre["Date_depassement"]))

ax.set_xlabel("Date du dépassement", fontsize =20)
ax.set_ylabel("Pays", fontsize=20)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

ax.set_xlim(datetime.datetime(2022, 1, 1), datetime.datetime(2025, 11, 30))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

ax.set_title("Jour du dépassement par pays", fontsize=25)
 
ax.tick_params(axis='x', labelsize=12) # pour reduire la taille des mots 
ax.tick_params(axis='y', labelsize=32)

plt.tight_layout()

st.pyplot(fig)


