Jour du dépassement par pays

Voici un projet d'analyse de données avec comme thématique le jour du dépassement. 
Source données : Data Footprint

En 2025, le jour du dépassement de la terre est le 24 juillet. En partant de là, je voulais connaitre le jour de dépassement des différents pays. Lesquels sont les plus pollueurs ? 

Pour cela, il faut déjà commencer par définir le jour du dépassement national : 
Il s'agit de la date à laquelle les ressources annuelles de la planète seraient épuisées 
si tout le monde sur Terre vivait au même niveau de consommation que les habitants de ce pays particulier.

Calcul : 
365 * biocapacité mondiale / empreinte du pays 

Voici l'une des données qui ressort de mon analyse. En 2022, si tout le monde vivait comme un qatari, le jour du dépassement de la terre serait le 19 janvier. 
Pour retrouver les 10 pays les plus consommateurs et les 10 pays les moins consommateurs de l'année 2022, consulter mon code : jour_depassement.py 

J'ai également réalisé une interface dynamique avec Streamlit pour comparer le jour du dépassement des différents pays pour l'année 2022 et 2024. 

Pour utiliser mon travail, télécharger les bases de données et remplacer les lignes :
- df = pd.read_excel("C:/Users/buket/Desktop/Epitech/projet_depassement_terre/donnees_propres_streamlit.xlsx") dans jour_depassement_streamlit.py
- df = pd.read_excel("C:/Users/buket/Desktop/Epitech/projet_depassement_terre/donnees_propres.xlsx") dans jour_depassement

Par les bons noms et empalcements de fichiers qui se trouvent sur votre ordinateur. 

Ensuite, installez Streamlit avec cette commande :
pip install streamlit

Une fois votre code "jour_depassement_streamlit.py" copié dans votre IDE, lancez cette commande : streamlit run app.py

