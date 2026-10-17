# Mission 2 : souveraineté et réglementation

**Objectif :** évaluer les dépendances technologiques et réglementaires de NovaCare Logistics, puis recommander une stratégie cloud.

**Rappel du contexte :** NovaCare est une entreprise française de logistique médicale, présente en France, aux États-Unis et à Singapour. Elle utilise un cloud américain, une application contenant des données de santé, une IA qui analyse le comportement des patients, un CRM américain et un support informatique basé à Singapour.

---

## 1. Tableau comparatif : cloud américain ou cloud souverain européen

| Critère | Cloud américain (hyperscaler) | Cloud souverain européen |
|---|---|---|
| **Droit applicable** | Droit américain applicable au fournisseur, même si les serveurs sont en Europe | Droit européen et français uniquement |
| **Accès des autorités étrangères** | Le **Cloud Act** (2018) permet aux autorités américaines d'exiger les données détenues par un fournisseur américain, où qu'elles soient stockées. Les lois de renseignement (FISA section 702) s'appliquent aussi | Pas de soumission aux lois extraterritoriales non européennes (critère central de la qualification **SecNumCloud** de l'ANSSI) |
| **Transferts RGPD** | Reposent sur le **Data Privacy Framework** (DPF), validé par le Tribunal de l'UE en septembre 2025 mais **contesté en appel devant la Cour de justice** (affaire C-703/25 P). Les deux accords précédents (Safe Harbor, Privacy Shield) ont été annulés : risque juridique réel | Pas de transfert hors UE : conformité plus simple |
| **Données de santé (HDS)** | Plusieurs grands fournisseurs américains sont certifiés HDS en France, mais cela ne règle pas la question du Cloud Act | Plusieurs offres certifiées HDS, et certaines qualifiées SecNumCloud |
| **Fonctionnalités et IA** | Très riche : services d'IA avancés, outils managés, mise à l'échelle mondiale | Catalogue plus réduit, surtout pour l'IA avancée ; en progrès |
| **Couverture internationale** | Présence mondiale, utile pour les filiales aux États-Unis et à Singapour | Surtout européenne : moins adapté aux activités hors UE |
| **Coût** | Compétitif à grande échelle, mais coûts de sortie (« egress ») élevés | Souvent comparable pour l'infrastructure ; parfois plus cher pour les services avancés |
| **Dépendance (lock-in)** | Forte : services propriétaires difficiles à migrer | Plus faible si l'on privilégie des standards ouverts |
| **Image et confiance** | Risque d'image si fuite ou demande d'accès des autorités américaines | Argument de confiance auprès des hôpitaux et patients européens |

**À retenir :** le cloud américain est plus puissant et plus international, mais il expose les données de santé à un **droit étranger** et à un **cadre de transfert juridiquement fragile**. Le cloud souverain protège mieux les données sensibles, au prix de fonctionnalités plus limitées.

---

## 2. Impacts réglementaires pour NovaCare

### NIS2 (directive (UE) 2022/2555 sur la cybersécurité)

- **Pourquoi NovaCare est concernée :** la santé et les transports figurent parmi les secteurs visés par NIS2. Selon sa taille, NovaCare serait une entité **essentielle** ou **importante**.
- **Obligations principales :** gestion des risques cyber (art. 21), **notification des incidents graves** (alerte précoce sous 24 h, notification sous 72 h, rapport final sous un mois, art. 23), sécurité de la **chaîne d'approvisionnement** (donc de ses prestataires cloud, CRM et support), responsabilité personnelle des dirigeants.
- **Situation en France :** la France n'a pas encore transposé la directive (date limite : 17 octobre 2024). La Commission européenne a saisi la Cour de justice contre la France en juillet 2026, et le projet de loi « résilience » est examiné à l'Assemblée nationale depuis octobre 2026. L'ANSSI a publié en mars 2026 un référentiel (ReCyF) pour se préparer.
- **Impact pour NovaCare :** auditer ses prestataires (cloud US, support à Singapour), mettre en place une procédure de notification d'incident, préparer l'enregistrement auprès de l'ANSSI.

### AI Act (règlement (UE) 2024/1689 sur l'intelligence artificielle)

- **Pourquoi NovaCare est concernée :** son IA analyse le comportement des patients. Selon son usage exact, elle pourrait être classée **à haut risque** : par exemple si elle sert à décider de l'accès à des soins, ou si elle fait partie d'un dispositif médical.
- **Calendrier (modifié par le « Digital Omnibus » IA, en vigueur depuis le 27 juillet 2026) :** obligations de transparence (art. 50) applicables depuis le 2 août 2026 ; obligations « haut risque » reportées au **2 décembre 2027** pour les systèmes autonomes et au **2 août 2028** pour ceux intégrés à des produits réglementés (dispositifs médicaux).
- **Impact pour NovaCare :** classifier son système d'IA dès maintenant ; préparer gestion des risques, qualité et gouvernance des données d'entraînement, documentation technique, **contrôle humain** et traçabilité. Ces exigences rejoignent celles du RGPD (AIPD, art. 22).

### Cloud Act (Clarifying Lawful Overseas Use of Data Act, États-Unis, 2018)

- **Principe :** un fournisseur soumis au droit américain doit remettre aux autorités américaines les données qu'il contrôle, **même stockées en Europe**.
- **Conflit avec le RGPD :** l'art. 48 du RGPD interdit de transférer des données sur simple demande d'une autorité étrangère, sans accord international.
- **Impact pour NovaCare :** ses données de santé hébergées sur le cloud américain et ses données clients dans le CRM américain sont exposées. C'est l'argument principal pour sortir les données de santé du cloud américain.

---

## 3. Recommandation : une stratégie **hybride**

| Option | Verdict |
|---|---|
| Tout en cloud américain | ❌ Rejetée : expose les données de santé au Cloud Act et à un éventuel nouvel arrêt « Schrems III » |
| Tout en cloud souverain | ⚠️ Écartée : trop limitant pour les filiales aux États-Unis et à Singapour, et pour les outils d'IA avancés |
| **Hybride** | ✅ **Recommandée** |

### Principe : classer les données selon leur sensibilité

| Catégorie de données | Hébergement recommandé |
|---|---|
| **Données de santé** (application patients) et données d'entraînement de l'IA | **Cloud souverain européen, certifié HDS**, idéalement qualifié SecNumCloud |
| Données personnelles clients (CRM) | CRM hébergé en UE, ou CRM américain **sans aucune donnée de santé**, avec données pseudonymisées et transferts encadrés (DPF + clauses contractuelles types) |
| Données opérationnelles non sensibles (stocks, flotte, logistique) | Cloud américain possible, pour bénéficier de la puissance et de la couverture mondiale |
| Activités locales aux États-Unis et à Singapour | Cloud local de chaque région, en respectant le droit local (HIPAA aux États-Unis, PDPA à Singapour) |

### Mesures d'accompagnement

1. **Chiffrement avec clés détenues par NovaCare en Europe** (approche « Hold Your Own Key ») : même si un fournisseur reçoit une demande, les données restent illisibles.
2. **Support de Singapour** : accès à distance journalisés, moindre privilège, données pseudonymisées par défaut, clauses contractuelles types.
3. **Plan de réversibilité** : privilégier des standards ouverts (conteneurs, Kubernetes, formats de données ouverts) pour pouvoir changer de fournisseur.
4. **Veille réglementaire continue** (outil RegRadar de la mission 3) : arrêt de la Cour de justice sur le DPF, loi française de transposition de NIS2, guides de la Commission sur l'AI Act.

### Feuille de route

| Phase | Échéance | Actions |
|---|---|---|
| 1. Urgence | 0 à 3 mois | AIPD, cartographie des flux, contrats art. 28 et clauses contractuelles types, chiffrement |
| 2. Migration | 3 à 9 mois | Migration des données de santé et de l'IA vers un cloud souverain HDS ; nettoyage du CRM |
| 3. Pilotage | 9 à 18 mois | Mise en conformité NIS2, classification et documentation AI Act, revue annuelle de la stratégie |

### Conclusion

La stratégie hybride protège ce qui compte le plus, les **données de santé des patients**, contre les risques juridiques extraterritoriaux, tout en conservant la puissance du cloud américain pour les activités non sensibles et internationales. Elle réduit l'exposition au Cloud Act, prépare NovaCare à NIS2 et à l'AI Act, et renforce la confiance de ses clients hospitaliers.

---

## Sources

- Règlement (UE) 2016/679 (RGPD), art. 44 à 49 et art. 48 : [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Directive (UE) 2022/2555 (NIS2) : [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- Règlement (UE) 2024/1689 (AI Act) : [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Digital Omnibus IA, calendrier : [Process Excellence Network](https://www.processexcellencenetwork.com/ai/articles/eu-ai-act-2026-what-actually-changed-and-what-deployers-still-must-do), [Digital Policy Alert](https://digitalpolicyalert.org/event/42539-council-of-the-european-union-adopted-digital-omnibus-on-ai-regulation-20250359-including-local-operations-requirement)
- Appel Latombe contre le Data Privacy Framework (C-703/25 P) : [Digital Policy Alert](https://digitalpolicyalert.org/event/35459-latombe-filed-appeal-against-general-court-dismissal-of-challenge-to-european-unionunited-states-data-protection-framework-adequacy-decision-in-latombe-v-commission)
- Transposition de NIS2 en France : [Next](https://next.ink/brief-article/alleluia-la-transposition-de-nis2-est-enfin-a-lordre-du-jour-de-lassemblee-nationale/), [OpenKRITIS](https://www.openkritis.de/eu/eu-nis-2-france.html)
