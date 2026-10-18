# NovaCare Logistics : gouvernance, RGPD et souveraineté numérique

Projet pratique du module **Fondamentaux de la gouvernance des données et de la cybersécurité** (EPITA, TP 3, MSCDS1).

> **Cas étudié :** NovaCare Logistics, entreprise française de logistique médicale présente en France, aux États-Unis et à Singapour. Elle utilise un cloud américain, une application contenant des données de santé, une IA d'analyse comportementale des patients, un CRM américain et un support informatique à Singapour. Plusieurs problèmes ont été détectés : absence d'analyse d'impact, fuite de données, transferts internationaux non documentés et hébergement médical non conforme.

🎬 **Vidéo de démonstration :** [Voir la vidéo](https://youtu.be/SlmAzo1ZeA0)
🌐 **Prototype en ligne :** [Ouvrir RegRadar](https://novacare-gouvernance-rgpd-agkepfxysrh749hglapdbt.streamlit.app/)

---

## Contenu du dépôt

| Dossier | Mission | Livrable |
|---|---|---|
| [`mission1-audit-rgpd/`](mission1-audit-rgpd/) | **Mission 1 : audit RGPD** | Matrice de conformité Excel : 7 risques, article RGPD, gravité (1 à 3), mesure corrective, responsable et échéance |
| [`mission2-souverainete/`](mission2-souverainete/comparatif_et_recommandation.md) | **Mission 2 : souveraineté et réglementation** | Tableau comparatif cloud américain / cloud souverain, impacts de NIS2, de l'AI Act et du Cloud Act, recommandation d'une stratégie hybride |
| [`mission3-regradar/`](mission3-regradar/) | **Mission 3 : prototype RegRadar** | Tableau de bord Streamlit présentant 3 alertes réglementaires (UE, États-Unis, APAC) et leur impact sur NovaCare |

---

## Mission 1 : audit RGPD

Sept risques identifiés, dont quatre de gravité élevée :

| N° | Risque | Article RGPD | Gravité |
|---|---|---|---|
| 1 | Absence d'analyse d'impact (AIPD) | Art. 35 | 🔴 3 |
| 2 | Fuite de données de santé | Art. 32, 33, 34 | 🔴 3 |
| 3 | Transferts hors UE non documentés | Art. 44 à 49 | 🔴 3 |
| 4 | Hébergement de santé non certifié HDS | Art. 9, 32 (+ CSP L.1111-8) | 🔴 3 |
| 5 | Profilage des patients par l'IA | Art. 9, 22, 5.1.c, 13-14 | 🟠 2 |
| 6 | Support à Singapour sans contrat de sous-traitance | Art. 28 | 🟠 2 |
| 7 | Registre des traitements incomplet | Art. 30, 5.2 | 🟢 1 |

Le détail des mesures correctives est dans le fichier Excel.

## Mission 2 : souveraineté et réglementation

**Recommandation : stratégie hybride.** Les données de santé et l'IA sont hébergées sur un cloud souverain européen certifié HDS ; les données opérationnelles non sensibles et les activités internationales restent sur le cloud américain ; chiffrement avec clés détenues par NovaCare. Voir le [document complet](mission2-souverainete/comparatif_et_recommandation.md).

## Mission 3 : prototype RegRadar

Tableau de bord de veille réglementaire : filtres par région, thème et impact, indicateurs clés, tableau de classement (pays, date, thème, impact) et fiche détaillée par alerte avec l'impact sur NovaCare et l'action recommandée.

| Région | Source officielle surveillée | Alerte | Impact |
|---|---|---|---|
| 🇪🇺 UE | EUR-Lex | Le « Digital Omnibus » IA reporte les obligations haut risque de l'AI Act | 🔴 Élevé |
| 🇺🇸 États-Unis | HHS / Federal Register | Réforme de la HIPAA Security Rule repoussée à juillet 2027 | 🟠 Moyen |
| 🇸🇬 APAC | PDPC Singapore | Nouvelles règles PDPA sur les transferts de données à l'étranger | 🟠 Moyen |

Les alertes sont stockées dans [`alertes.csv`](mission3-regradar/alertes.csv) : pour en ajouter une, il suffit d'ajouter une ligne.

### Lancer le prototype en local

```bash
pip install -r requirements.txt
streamlit run mission3-regradar/app.py
```

L'application s'ouvre dans le navigateur à l'adresse `http://localhost:8501`.

---

## Technologies

Python · Streamlit · pandas · Excel · GitHub · Streamlit Community Cloud

## Équipe

- Alexandre Houli
- Dylan Nicolle
- Eloi Oberrieder
- Marouane Tika
- Neila Sahnoun
