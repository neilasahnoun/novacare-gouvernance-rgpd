"""RegRadar : prototype de veille réglementaire pour NovaCare Logistics.

Lancer en local :  streamlit run mission3-regradar/app.py
"""
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent / "alertes.csv"
IMPACT_ORDER = ["Élevé", "Moyen", "Faible"]
IMPACT_ICON = {"Élevé": "🔴", "Moyen": "🟠", "Faible": "🟢"}
REGION_FLAG = {"UE": "🇪🇺", "États-Unis": "🇺🇸", "APAC": "🇸🇬"}


@st.cache_data
def load_alerts(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str).fillna("")
    df["impact"] = pd.Categorical(df["impact"], categories=IMPACT_ORDER, ordered=True)
    return df.sort_values(["impact", "date"], ascending=[True, False]).reset_index(drop=True)


st.set_page_config(page_title="RegRadar · NovaCare", page_icon="📡", layout="wide")

st.title("📡 RegRadar")
st.caption(
    "Prototype de veille réglementaire pour **NovaCare Logistics** "
    "(logistique médicale : France, États-Unis, Singapour)."
)

alerts = load_alerts(DATA_FILE)

# --- Filtres --------------------------------------------------------------
st.sidebar.header("Filtres")
regions = st.sidebar.multiselect("Région", sorted(alerts["region"].unique()), default=sorted(alerts["region"].unique()))
themes = st.sidebar.multiselect("Thème", sorted(alerts["theme"].unique()), default=sorted(alerts["theme"].unique()))
impacts = st.sidebar.multiselect(
    "Impact", [i for i in IMPACT_ORDER if i in set(alerts["impact"].astype(str))],
    default=[i for i in IMPACT_ORDER if i in set(alerts["impact"].astype(str))],
)
st.sidebar.divider()
st.sidebar.markdown(
    "**Sources surveillées**\n\n"
    "- 🇪🇺 EUR-Lex (Journal officiel de l'UE)\n"
    "- 🇺🇸 HHS / Federal Register\n"
    "- 🇸🇬 PDPC Singapore"
)

view = alerts[
    alerts["region"].isin(regions)
    & alerts["theme"].isin(themes)
    & alerts["impact"].astype(str).isin(impacts)
]

# --- Indicateurs ----------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Alertes affichées", len(view))
c2.metric("Impact élevé", int((view["impact"] == "Élevé").sum()))
c3.metric("Régions couvertes", view["region"].nunique())
c4.metric("Dernière mise à jour", view["date"].max() if len(view) else "–")

if view.empty:
    st.info("Aucune alerte ne correspond aux filtres choisis.")
    st.stop()

# --- Tableau de classement -------------------------------------------------
st.subheader("Classement des alertes")
table = view[["region", "pays", "date", "theme", "impact", "titre", "url_verification"]].copy()
table["impact"] = table["impact"].astype(str).map(lambda i: f"{IMPACT_ICON.get(i, '')} {i}")
st.dataframe(
    table,
    hide_index=True,
    use_container_width=True,
    column_config={
        "region": "Région",
        "pays": "Pays",
        "date": "Date",
        "theme": "Thème",
        "impact": "Impact",
        "titre": st.column_config.TextColumn("Alerte", width="large"),
        "url_verification": st.column_config.LinkColumn("Source", display_text="Lire"),
    },
)

chart_col, note_col = st.columns([2, 1])
with chart_col:
    st.markdown("**Alertes par niveau d'impact**")
    counts = view["impact"].value_counts().reindex(IMPACT_ORDER, fill_value=0)
    st.bar_chart(counts.rename("Nombre d'alertes"))
with note_col:
    st.markdown("**Échelle d'impact**")
    st.markdown(
        "- 🔴 **Élevé** : action nécessaire, risque de non-conformité majeur\n"
        "- 🟠 **Moyen** : à anticiper dans les 6 à 12 mois\n"
        "- 🟢 **Faible** : à surveiller"
    )

# --- Fiches détaillées -----------------------------------------------------
st.subheader("Détail et impact sur NovaCare")
for _, a in view.iterrows():
    impact = str(a["impact"])
    with st.container(border=True):
        st.markdown(f"#### {IMPACT_ICON.get(impact, '')} {a['titre']}")
        st.caption(f"{REGION_FLAG.get(a['region'], '')} {a['pays']} · {a['date']} · {a['theme']} · Impact **{impact}**")
        st.write(a["resume"])
        left, right = st.columns(2)
        with left:
            st.markdown("**Impact potentiel pour NovaCare**")
            st.write(a["impact_novacare"])
        with right:
            st.markdown("**Action recommandée**")
            st.write(a["action"])
        st.markdown(
            f"Source officielle à surveiller : [{a['source_officielle']}]({a['url_source_officielle']}) · "
            f"[Article de vérification]({a['url_verification']})"
        )

st.divider()
st.caption("Projet pédagogique : EPITA, TP 3, MSCDS1. Données d'exemple collectées en octobre 2026.")
