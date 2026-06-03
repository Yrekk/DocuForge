# DocuForge

DocuForge est une application locale Python permettant de générer des documents à partir de templates dynamiques Jinja2 via une interface Streamlit.

Le projet vise à fournir une base simple, propre et extensible pour automatiser la génération de documents structurés : prompts, lettres de motivation, mails professionnels, cahiers des charges, user stories ou autres documents métier.

La V1 se concentre volontairement sur un moteur générique de génération documentaire, sans intégration IA immédiate. L'objectif est de construire une base saine avant d'ajouter des fonctionnalités plus avancées.

---

## Objectif du projet

DocuForge permet de :

- charger un template texte ou Markdown ;
- détecter automatiquement les variables Jinja2 présentes dans le template ;
- générer dynamiquement un formulaire à partir de ces variables ;
- remplir les champs nécessaires ;
- générer le document final ;
- copier le résultat dans le presse-papier ;
- télécharger le document généré ;
- valider les champs obligatoires avant génération.

---

## Exemple de template

```jinja2
Bonjour {{ nom }},

Je candidate au poste de {{ poste }} chez {{ entreprise }}.

{{ motivation }}

Cordialement,
{{ signature }}
```

DocuForge détecte automatiquement les variables suivantes :

```txt
nom
poste
entreprise
motivation
signature
```

Puis génère un formulaire permettant de renseigner ces valeurs.

Les variables Jinja2 doivent être écrites en snake_case :
- lettres minuscules
- chiffres autorisés sauf en premier caractère
- underscores pour séparer les mots
- pas d'espaces
- pas d'apostrophes
- pas de tirets

Exemples :
    Correct :
    {{ nom_entreprise }}
    {{ public_cible }}
    {{ objectif_redaction }}

    Incorrect :
    {{ nom entreprise }}
    {{ public-cible }}
    {{ l'objectif }}

---

## Fonctionnalités actuelles

- Interface locale avec Streamlit
- Upload de templates `.txt` et `.md`
- Lecture propre du fichier uploadé
- Extraction automatique des variables Jinja2
- Génération dynamique du formulaire
- Validation des champs vides
- Rendu final avec Jinja2
- Affichage du document généré
- Copie du résultat dans le presse-papier
- Téléchargement du document généré en `.txt`
- Tests unitaires avec pytest

---

## Stack technique

- Python
- Streamlit
- Jinja2
- Pytest

---

## Structure du projet

```txt
DocuForge/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── form_validator.py
│   │   ├── template_reader.py
│   │   ├── template_renderer.py
│   │   └── variable_extractor.py
│   │
│   └── ui/
│       ├── __init__.py
│       ├── clipboard_button.py
│       └── form_builder.py
│
├── generated/
├── templates_examples/
├── tests/
│   ├── __init__.py
│   ├── test_form_validator.py
│   ├── test_template_renderer.py
│   └── test_variable_extractor.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── run_app.bat
```

---

## Installation

Cloner le projet :

```bash
git clone https://github.com/Yrekk/DocuForge.git
cd DocuForge
```

Créer un environnement virtuel :

```bash
py -3.12 -m venv .venv
```

Activer l'environnement virtuel sous Windows :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Lancement de l'application

Avec Streamlit :

```bash
streamlit run app/main.py
```

Ou sous Windows, via le fichier fourni :

```bash
run_app.bat
```

Le script `run_app.bat` utilise directement le Python de l'environnement virtuel local.

---

## Lancer les tests

Depuis la racine du projet :

```bash
python -m pytest
```

Résultat attendu :

```txt
23 passed
```

---

## Pourquoi Jinja2 ?

DocuForge utilise Jinja2 plutôt qu'un simple remplacement de texte afin de préparer des templates plus riches.

Jinja2 permet notamment :

- les variables ;
- les conditions ;
- les boucles ;
- les blocs optionnels ;
- les templates métier plus complexes.

Exemple d'évolution possible :

```jinja2
{% if mention_rqth %}
Je bénéficie d'une RQTH et recherche un environnement de travail adapté à une performance durable.
{% endif %}
```

---

## Pourquoi Streamlit ?

Streamlit permet de construire rapidement une interface locale simple et efficace, sans développer un front-end complet.

C'est adapté pour une première version orientée :

- prototype propre ;
- outil local ;
- démonstration GitHub ;
- automatisation documentaire ;
- future extension IA.

---

## Roadmap

### V1

- [x] Upload de template
- [x] Lecture du contenu
- [x] Extraction des variables Jinja2
- [x] Génération dynamique du formulaire
- [x] Validation des champs obligatoires
- [x] Rendu du document final
- [x] Copie dans le presse-papier
- [x] Téléchargement du document généré
- [x] Tests unitaires

### V1

- [x] Refacto de la logique de main vers un controller dédié
- [x] Ajouts d'un fichier config.json pour indiquer le path de documents en local
- [x] Ajouts d'un controller pour générer des prompts uniquement depuis le fichier local

### V2 envisagée

La V2 pourra intégrer une couche IA pour assister la génération documentaire.

Exemple de flux envisagé :

```txt
CV + offre d'emploi + informations utilisateur
↓
Génération d'un prompt intermédiaire
↓
Validation ou correction par l'utilisateur
↓
Génération finale du document
```

La V2 pourra notamment servir à générer :

- lettres de motivation ;
- prompts structurés ;
- mails professionnels ;
- documents de candidature ;
- documents métier enrichis.

---

## Points de vigilance pour la future V2 IA

L'intégration IA devra prendre en compte :

- la protection des API keys ;
- la confidentialité des CV et documents uploadés ;
- le traitement des données personnelles ;
- les hallucinations possibles des modèles ;
- la validation humaine obligatoire ;
- la séparation claire entre suggestion automatique et décision utilisateur ;
- la prudence sur le parsing d'URL ou de documents externes.

---

## Limites actuelles

La V1 reste volontairement simple :

- les champs détectés sont considérés comme obligatoires ;
- les valeurs sont actuellement traitées comme du texte ;
- les exports sont limités au texte brut ;
- les templates complexes avec listes ou booléens nécessiteront une évolution de l'interface ;
- l'application est pensée pour un usage local.

---

## Statut

Projet en développement.

La V1 fonctionnelle est disponible et testée.
