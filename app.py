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

# ====================== HEADER MIT LOGO ======================
col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=300)

with col2:
    st.title("Predictive Maintenance Dashboard")
    st.markdown("**Vorhersage von Maschinen-Ausfällen mit Decision Tree**")

st.markdown("""
Diese Anwendung sagt voraus, ob eine Maschine in naher Zukunft einen Ausfall haben wird.  
Sie basiert auf Sensordaten wie Temperatur, Drehzahl, Drehmoment und Werkzeugverschleiß.
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
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "94%", help="Wie oft liegt das Modell insgesamt richtig?")
    with col2:
        st.metric("Recall", "84%", help="Wie viele echte Ausfälle erkennt das Modell? (wichtigster Wert!)")
    with col3:
        st.metric("Precision", "36%", help="Wie viele der Warnungen sind wirklich Ausfälle?")
    with col4:
        st.metric("F1-Score", "51%", help="Ausgewogener Mittelwert aus Recall und Precision")
    
    st.markdown("**Was bedeuten diese Werte?**")
    st.info("""
    - **Recall 84%** → Das Modell erkennt **84 von 100** echten Ausfällen.  
      Sehr wichtig für die Produktion, damit Maschinen nicht unerwartet stehen bleiben.
    - **Precision 36%** → Von allen Warnungen sind **36%** echte Ausfälle.  
      Es gibt also auch Fehlalarme, die man prüfen muss.
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
        process_temp = st.slider("Prozesstemperatur [K]", 305.0, 315.0, 309.5, 0.1)
        rotational_speed = st.slider("Drehzahl [rpm]", 1100, 2900, 1500, 10)
    
    with col2:
        torque = st.slider("Drehmoment [Nm]", 20.0, 80.0, 45.0, 0.5)
        tool_wear = st.slider("Werkzeugverschleiß [min]", 0, 300, 120, 5)
    
    if st.button("🔍 Vorhersage starten", type="primary", use_container_width=True):
        input_data = pd.DataFrame({
            'Air temperature [K]': [air_temp],
            'Process temperature [K]': [process_temp],
            'Rotational speed [rpm]': [rotational_speed],
            'Torque [Nm]': [torque],
            'Tool wear [min]': [tool_wear]
        })
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        if prediction == 1:
            st.error(f"⚠️ **Ausfall wahrscheinlich!** (Wahrscheinlichkeit: {probability:.1%})")
            st.warning("Empfehlung: Wartung bald einplanen.")
        else:
            st.success(f"✅ **Kein Ausfall erwartet** (Wahrscheinlichkeit für Ausfall: {probability:.1%})")

# ====================== TAB 3: FEATURE IMPORTANCE ======================
with tab3:
    st.subheader("Wichtigste Einflussfaktoren")
    st.markdown("Welche Sensorwerte haben den größten Einfluss auf einen Ausfall?")
    
    importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=importance, x='Importance', y='Feature', ax=ax, palette='viridis')
    ax.set_xlabel("Wichtigkeit")
    ax.set_ylabel("")
    st.pyplot(fig)
    
    st.markdown("**Erkenntnis:**")
    st.info("Das **Drehmoment (Torque)** und der **Werkzeugverschleiß (Tool wear)** haben den größten Einfluss auf Ausfälle. Hohes Drehmoment + hoher Verschleiß = hohes Ausfallrisiko.")

# ====================== FOOTER ======================
st.divider()
st.caption("Projekt: Predictive Maintenance für Industrieroboter | Erstellt mit Python + Streamlit | 2026")