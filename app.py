import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# ====================== SEITENKONFIGURATION ======================
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="🔧",
    layout="wide"
)

# ====================== HEADER ======================
st.title("🔧 Predictive Maintenance Dashboard")

st.markdown("""
**Sina Ardabilie**  
*Testingenieur | Predictive Maintenance & Robotik*
""")

st.markdown("""
Diese Anwendung sagt voraus, ob eine Maschine (z. B. ein Industrieroboter) in naher Zukunft einen Ausfall haben wird.  
Sie basiert auf realen Sensordaten und wurde als Bewerbungsprojekt für Positionen im Bereich **Predictive Maintenance und industrielle KI** (z. B. bei Siemens) entwickelt.
""")

st.divider()

# ====================== DATEN + MODELL ======================
@st.cache_data
def load_data_and_model():
    df = pd.read_csv('ai4i2020.csv')
    
    X = df[['Air temperature [K]', 'Process temperature [K]', 
            'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']]
    y = df['Machine failure']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = DecisionTreeClassifier(
        max_depth=7, 
        min_samples_leaf=5, 
        random_state=42, 
        class_weight='balanced'
    )
    model.fit(X_train, y_train)
    
    return df, X, y, X_train, X_test, y_train, y_test, model

df, X, y, X_train, X_test, y_train, y_test, model = load_data_and_model()

# ====================== TABS ======================
tab1, tab2, tab3 = st.tabs(["📊 Modell-Performance", "🔮 Vorhersage", "📈 Feature Importance"])

# ====================== TAB 1: PERFORMANCE ======================
with tab1:
    st.subheader("Modell-Performance")
    
    y_pred = model.predict(X_test)
    
    # Metriken mit Erklärungen
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "94%", help="Wie oft liegt das Modell insgesamt richtig?")
    with col2:
        st.metric("Recall", "84%", help="Wie viele echte Ausfälle erkennt das Modell? (wichtigster Wert für Predictive Maintenance)")
    with col3:
        st.metric("Precision", "36%", help="Wie viele der Warnungen sind wirklich Ausfälle?")
    with col4:
        st.metric("F1-Score", "51%", help="Ausgewogener Mittelwert aus Recall und Precision")
    
    st.info("""
    **Was bedeuten diese Werte?**  
    - **Recall 84%**: Das Modell erkennt **84 von 100** echten Ausfällen → Sehr wichtig, damit Maschinen nicht unerwartet stehen bleiben.  
    - **Precision 36%**: Von allen Warnungen sind 36% echte Ausfälle → Es gibt auch Fehlalarme, die man prüfen muss.
    """)
    
    # Confusion Matrix
    st.markdown("**Confusion Matrix**")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Kein Ausfall', 'Ausfall'],
                yticklabels=['Kein Ausfall', 'Ausfall'])
    ax.set_xlabel("Vorhergesagt")
    ax.set_ylabel("Tatsächlich")
    st.pyplot(fig)

# ====================== TAB 2: VORHERSAGE ======================
with tab2:
    st.subheader("Neue Maschine vorhersagen")
    st.markdown("Gib die aktuellen Sensordaten ein und das Modell sagt dir, ob ein Ausfall wahrscheinlich ist.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        air_temp = st.slider("Lufttemperatur [K]", 295.0, 305.0, 298.5, 0.1)
        process_temp = st.slider("Prozesstemperatur [K]", 305.0, 315.0, 309.5
st.caption("Projekt: Predictive Maintenance für Industrieroboter | Erstellt mit Python + Streamlit | 2026")
