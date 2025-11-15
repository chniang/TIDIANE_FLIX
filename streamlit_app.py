# streamlit_app.py
# Interface Streamlit pour TidianeFlix + Visualisations Plotly

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px
from pathlib import Path
import os
from datetime import datetime

# -------------------------
# CONFIGURATION
# -------------------------

DB_USER = os.getenv('TIDIANE_DB_USER', 'root')
DB_PASSWORD = os.getenv('TIDIANE_DB_PASSWORD', '')
DB_HOST = os.getenv('TIDIANE_DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('TIDIANE_DB_PORT', '3306')
DB_NAME = os.getenv('TIDIANE_DB_NAME', 'tidiane_flix')

SQLALCHEMY_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

# -------------------------
# UTILITAIRES
# -------------------------

@st.cache_resource
def get_engine(url=SQLALCHEMY_URL):
    return create_engine(url, pool_pre_ping=True)

@st.cache_data(ttl=60)
def run_query(query, params=None):
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn, params=params)
    return df

@st.cache_data(ttl=60)
def get_table(table_name, limit=1000):
    q = f"SELECT * FROM {table_name} LIMIT :limit"
    return run_query(q, {'limit': limit})

# Insert ticket
def insert_ticket(prix, date_achat, id_client, id_projection):
    engine = get_engine()
    insert_sql = text("""
        INSERT INTO ticket (prix, date_achat, id_client, id_projection)
        VALUES (:prix, :date_achat, :id_client, :id_projection)
    """)
    with engine.begin() as conn:
        res = conn.execute(insert_sql, {
            'prix': float(prix),
            'date_achat': date_achat,
            'id_client': int(id_client),
            'id_projection': int(id_projection)
        })
        return res.lastrowid if hasattr(res, "lastrowid") else None

# -------------------------
# UI
# -------------------------

def sidebar_navigation():
    st.sidebar.title('TidianeFlix')
    page = st.sidebar.radio('Navigation', [
        'Accueil', 'Films', 'Projections', 'Vendre un ticket', 'Clients', 'Tickets', 'Stats', 'SQL brut'
    ])
    return page


def show_header():
    st.title('🎬 TidianeFlix — Tableau de bord')
    st.write('Interface simple pour explorer la base de données de la billetterie.')

# -------------------------
# PAGES
# -------------------------

def page_home():
    show_header()
    st.markdown('**Bienvenue** — utilise le menu latéral pour naviguer.')

    col1, col2, col3 = st.columns(3)

    try:
        total_films = run_query('SELECT COUNT(*) as n FROM film').iloc[0]['n']
        total_clients = run_query('SELECT COUNT(*) as n FROM client').iloc[0]['n']
        total_tickets = run_query('SELECT COUNT(*) as n FROM ticket').iloc[0]['n']
    except:
        st.error("Erreur de connexion DB.")
        return

    col1.metric("Films", total_films)
    col2.metric("Clients", total_clients)
    col3.metric("Tickets vendus", total_tickets)

    st.subheader("Dernières projections")
    dfp = run_query("""
        SELECT p.id_projection, p.date_projection, p.heure,
               f.titre, s.nom_salle 
        FROM projection p
        JOIN film f ON p.id_film = f.id_film
        JOIN salle s ON p.id_salle = s.id_salle
        ORDER BY p.date_projection DESC LIMIT 10
    """)
    st.dataframe(dfp)


def page_films():
    st.header("📽️ Films")
    df = get_table("film")
    st.dataframe(df)


def page_projections():
    st.header("🕒 Projections")

    df = run_query("""
        SELECT p.id_projection, p.date_projection, p.heure,
               f.titre, s.nom_salle
        FROM projection p
        JOIN film f ON p.id_film = f.id_film
        JOIN salle s ON p.id_salle = s.id_salle
        ORDER BY p.date_projection, p.heure
    """)
    st.dataframe(df)

    films = run_query("SELECT id_film, titre FROM film")
    options = {row.id_film: row.titre for _, row in films.iterrows()}

    film_id = st.selectbox("Filtrer par film", [None] + list(options.keys()),
                           format_func=lambda x: options.get(x, "—") if x else "—")

    if film_id:
        df2 = run_query("SELECT * FROM projection WHERE id_film = :id", {"id": film_id})
        st.subheader("Résultats filtrés")
        st.dataframe(df2)


def page_sell_ticket():
    st.header("💳 Vendre un ticket")

    clients = run_query("SELECT id_client, nom, prenom FROM client")
    clients["label"] = clients["nom"] + " " + clients["prenom"]

    client_id = st.selectbox(
        "Client",
        [None] + clients.id_client.tolist(),
        format_func=lambda x: clients.loc[clients.id_client == x, "label"].values[0]
        if x else "—"
    )

    projections = run_query("""
        SELECT p.id_projection, p.date_projection, p.heure, f.titre
        FROM projection p JOIN film f ON p.id_film = f.id_film
        ORDER BY p.date_projection DESC
    """)
    projections["label"] = projections["titre"] + " — " + projections["date_projection"].astype(str)

    proj_id = st.selectbox(
        "Projection",
        [None] + projections.id_projection.tolist(),
        format_func=lambda x: projections.loc[projections.id_projection == x, "label"].values[0]
        if x else "—"
    )

    prix = st.number_input("Prix (FCFA)", 1000.0, 100000.0, 3000.0, 500.0)
    date_achat = st.date_input("Date d'achat", datetime.now().date())

    if st.button("Enregistrer"):
        if not client_id or not proj_id:
            st.error("Sélectionne un client et une projection.")
        else:
            tid = insert_ticket(prix, date_achat, client_id, proj_id)
            st.success(f"Ticket enregistré (id={tid})")


def page_clients():
    st.header("👥 Clients")
    df = get_table("client")
    st.dataframe(df)


def page_tickets():
    st.header("🎟️ Tickets")
    df = run_query("""
        SELECT t.id_ticket, t.prix, t.date_achat,
               c.nom, c.prenom, f.titre
        FROM ticket t
        JOIN client c ON t.id_client = c.id_client
        JOIN projection p ON t.id_projection = p.id_projection
        JOIN film f ON p.id_film = f.id_film
        ORDER BY t.date_achat DESC
        LIMIT 500
    """)
    st.dataframe(df)


# -------------------------
# PAGE STATS AVEC VISUALISATIONS
# -------------------------

def page_stats():
    st.header("📊 Statistiques — Visualisations interactives")

    # --- Revenus par film ----------------------------------------
    df_rev = run_query("""
        SELECT f.titre, SUM(t.prix) as total_revenu, COUNT(*) as nb_tickets
        FROM ticket t
        JOIN projection p ON t.id_projection = p.id_projection
        JOIN film f ON p.id_film = f.id_film
        GROUP BY f.id_film
        ORDER BY total_revenu DESC
    """)

    st.subheader("💰 Revenus par film (bar chart)")
    fig1 = px.bar(df_rev, x="titre", y="total_revenu", text="total_revenu",
                  title="Revenus totaux par film")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("🧩 Répartition des revenus (Treemap)")
    fig2 = px.treemap(df_rev, path=["titre"], values="total_revenu",
                      title="Contribution de chaque film au revenu total")
    st.plotly_chart(fig2, use_container_width=True)

    # --- Salles --------------------------------------------------
    df_salles = run_query("""
        SELECT s.nom_salle, COUNT(p.id_projection) as nb_projections
        FROM projection p
        JOIN salle s ON p.id_salle = s.id_salle
        GROUP BY s.id_salle
        ORDER BY nb_projections DESC
    """)

    st.subheader("🏟️ Salles les plus utilisées")
    fig3 = px.bar(df_salles, x="nom_salle", y="nb_projections",
                  title="Nombre de projections par salle")
    st.plotly_chart(fig3, use_container_width=True)

    # --- Timeline projections ------------------------------------
    st.subheader("📆 Timeline des projections")

    df_proj = run_query("""
        SELECT p.date_projection, f.titre
        FROM projection p
        JOIN film f ON p.id_film = f.id_film
    """)

    fig4 = px.histogram(df_proj, x="date_projection", color="titre",
                        title="Nombre de projections par date")
    st.plotly_chart(fig4, use_container_width=True)

    # --- Genres --------------------------------------------------
    try:
        df_genre = run_query("SELECT genre, COUNT(*) as total FROM film GROUP BY genre")
        st.subheader("🎭 Répartition des genres de films")
        fig5 = px.pie(df_genre, values="total", names="genre")
        st.plotly_chart(fig5, use_container_width=True)
    except:
        st.info("Genres non disponibles.")


# -------------------------
# SQL BRUT
# -------------------------

def page_sql_raw():
    st.header("🛠️ SQL brut")
    sql = st.text_area("Requête SELECT")
    if st.button("Exécuter"):
        if not sql.strip().lower().startswith("select"):
            st.error("Uniquement SELECT autorisé.")
        else:
            df = run_query(sql)
            st.dataframe(df)

# -------------------------
# MAIN
# -------------------------

def main():
    st.set_page_config(page_title="TidianeFlix", layout="wide")
    page = sidebar_navigation()

    if page == "Accueil":
        page_home()
    elif page == "Films":
        page_films()
    elif page == "Projections":
        page_projections()
    elif page == "Vendre un ticket":
        page_sell_ticket()
    elif page == "Clients":
        page_clients()
    elif page == "Tickets":
        page_tickets()
    elif page == "Stats":
        page_stats()
    elif page == "SQL brut":
        page_sql_raw()

if __name__ == "__main__":
    main()
