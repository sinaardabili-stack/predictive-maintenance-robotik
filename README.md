# 🔧 Predictive Maintenance Dashboard

**Sina Ardabilie**  
*Testingenieur | Predictive Maintenance & Robotik*

---

## Projektbeschreibung

Dieses Dashboard sagt voraus, ob eine Maschine (z. B. ein Industrieroboter) in naher Zukunft einen Ausfall haben wird.  
Es basiert auf realen Sensordaten (Temperatur, Drehzahl, Drehmoment und Werkzeugverschleiß) und wurde mit einem **Decision Tree** trainiert.

Das Projekt dient als Bewerbungsbeispiel für Positionen im Bereich **Predictive Maintenance, KI und Robotik** (z. B. bei Siemens in München).

---

## Features

- Vorhersage von Maschinen-Ausfällen mit **84% Recall**
- Interaktive Vorhersage mit realen Sensordaten
- Wichtige Einflussfaktoren (Feature Importance)
- Professionelles Dashboard mit Streamlit

---

## Technologien

- Python
- Streamlit
- scikit-learn (Decision Tree)
- pandas, matplotlib, seaborn

---

## So startest du das Projekt lokal

```bash
# 1. Repository klonen
git clone https://github.com/sinaardabili-stack/predictive-maintenance-robotik.git
cd predictive-maintenance-robotik

# 2. Virtuelle Umgebung erstellen (empfohlen)
python -m venv venv
source venv/bin/activate          # macOS / Linux

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Dashboard starten
streamlit run app.py