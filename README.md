{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # \uc0\u55357 \u56615  Predictive Maintenance Dashboard\
\
**Sina Ardabilie**  \
*Testingenieur | Predictive Maintenance & Robotik*\
\
---\
\
## Projektbeschreibung\
\
Dieses Dashboard sagt voraus, ob eine Maschine (z. B. ein Industrieroboter) in naher Zukunft einen Ausfall haben wird.  \
Es basiert auf realen Sensordaten (Temperatur, Drehzahl, Drehmoment und Werkzeugverschlei\'df) und wurde mit einem **Decision Tree** trainiert.\
\
Das Projekt dient als Bewerbungsbeispiel f\'fcr Positionen im Bereich **Predictive Maintenance, KI und Robotik** (z. B. bei Siemens in M\'fcnchen).\
\
---\
\
## Features\
\
- Vorhersage von Maschinen-Ausf\'e4llen mit **84% Recall**\
- Interaktive Vorhersage mit realen Sensordaten\
- Wichtige Einflussfaktoren (Feature Importance)\
- Professionelles Dashboard mit Streamlit\
\
---\
\
## Technologien\
\
- Python\
- Streamlit\
- scikit-learn (Decision Tree)\
- pandas, matplotlib, seaborn\
\
---\
\
## So startest du das Projekt lokal\
\
```bash\
# 1. Repository klonen\
git clone https://github.com/sinaardabili-stack/predictive-maintenance-robotik.git\
cd predictive-maintenance-robotik\
\
# 2. Virtuelle Umgebung erstellen (empfohlen)\
python -m venv venv\
source venv/bin/activate          # macOS / Linux\
\
# 3. Abh\'e4ngigkeiten installieren\
pip install -r requirements.txt\
\
# 4. Dashboard starten\
streamlit run app.py}