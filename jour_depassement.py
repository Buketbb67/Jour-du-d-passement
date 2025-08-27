import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

df = pd.read_excel("C:/Users/buket/Desktop/Epitech/projet_depassement_terre/donnees_propres.xlsx")

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

df["Date_depassement"] = pd.to_datetime(df["Date_depassement"])  # Corrige le format date

df_sorted = df.sort_values("Date_depassement")

top10 = df_sorted.head(10)
bottom10 = df_sorted.tail(10)

df_visu = pd.concat([top10, bottom10]) # pour voir les 10 premiers et 10 derniers pays 

fig, ax = plt.subplots(figsize=(12, 8))
fig.canvas.manager.set_window_title("Jour du dépassement par pays 2022")
plt.barh(df_visu["Country"], pd.to_datetime(df_visu["Date_depassement"]))

plt.xlabel("Date du dépassement")
plt.ylabel("Pays")

plt.xlim(datetime.datetime(2022, 1, 1), datetime.datetime(2023, 10, 30))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))

plt.title("Jour du dépassement pour les 10 premiers et derniers pays")

plt.tick_params(axis='x', labelsize=6) # pour ajuster la taille des mots 
plt.tick_params(axis='y', labelsize=6)

plt.tight_layout()
plt.show()


