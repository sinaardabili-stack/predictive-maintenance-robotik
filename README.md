# 🔧 Predictive Maintenance Dashboard – Industrial Robotics

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Decision%20Tree-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **An interactive machine failure prediction dashboard built with Python, Streamlit and scikit-learn – based on real industrial sensor data from the AI4I 2020 Predictive Maintenance Dataset.**

---

## 🎯 Project Overview

This project predicts whether an industrial machine (e.g. a robot or CNC system) is likely to **fail in the near future**, based on real-time sensor readings.

The model was trained on the **AI4I 2020 Predictive Maintenance Dataset** – a widely used benchmark dataset in industrial machine learning research – and achieves **84% Recall**, meaning it correctly identifies 84% of actual machine failures before they occur.

This is directly relevant to modern manufacturing environments where unplanned downtime is costly and predictive maintenance systems are replacing reactive repair cycles.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🤖 **Failure Prediction** | Real-time prediction of machine failure (Yes / No) |
| 📊 **Feature Importance** | Visualizes which sensor values drive the prediction |
| 🎛️ **Interactive Input** | Adjust sensor values via sliders and see instant results |
| 📈 **Model Performance** | Recall: 84% – optimized for fault detection |
| 🖥️ **Streamlit Dashboard** | Clean, professional web interface |

---

## 🧠 Technical Approach

### Dataset
- **Source:** AI4I 2020 Predictive Maintenance Dataset (UCI Machine Learning Repository)
- **Samples:** 10,000 data points from simulated industrial machines
- **Features used:**
  - Air Temperature [K]
  - Process Temperature [K]
  - Rotational Speed [rpm]
  - Torque [Nm]
  - Tool Wear [min]

### Model
- **Algorithm:** Decision Tree Classifier (scikit-learn)
- **Target:** Binary classification – Machine Failure (1) / No Failure (0)
- **Key metric:** Recall = 84% (optimized to minimize missed failures)
- **Why Recall?** In predictive maintenance, a missed failure (false negative) is far more costly than a false alarm.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sinaardabili-stack/predictive-maintenance-robotik.git
cd predictive-maintenance-robotik

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the dashboard
streamlit run app.py
```

The dashboard will open automatically at `http://localhost:8501`

---

## 📁 Project Structure

```
predictive-maintenance-robotik/
│
├── app.py                  # Streamlit dashboard & prediction logic
├── ai4i2020.csv            # AI4I 2020 Predictive Maintenance Dataset
├── requirements.txt        # Python dependencies
├── logo.png                # Dashboard logo
└── README.md               # This file
```

---

## 🔍 How It Works

1. **Data Loading** – The AI4I 2020 dataset is loaded and preprocessed
2. **Model Training** – A Decision Tree is trained on historical sensor data
3. **User Input** – The user adjusts sensor values via interactive sliders
4. **Prediction** – The model outputs a failure probability in real time
5. **Explanation** – Feature importance chart shows which sensors matter most

---

## 💡 Real-World Relevance

This project was built to demonstrate practical application of machine learning in an industrial engineering context:

- **Quality Engineering:** Early detection of anomalies before failures occur
- **Robotics Operations:** Applied during hands-on work with industrial robots at Agile Robots SE
- **Automotive Testing:** Sensor-based monitoring is directly analogous to ECU validation and HiL test environments
- **Predictive vs. Reactive:** Shifting from reactive repair to data-driven prevention – a key challenge in modern manufacturing

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9+ | Core language |
| Streamlit | Interactive web dashboard |
| scikit-learn | Decision Tree model |
| pandas | Data loading & preprocessing |
| matplotlib / seaborn | Visualization |

---

## 📊 Model Results

| Metric | Value |
|--------|-------|
| Recall (Failure class) | **84%** |
| Target | Minimize missed failures |
| Dataset | AI4I 2020 – 10,000 samples |

---

## 👤 Author

**Sina Shahsavand Ardabili**
Mechatronics Engineer (B.Sc.) | Test Engineer | ISTQB® Certified

- 🔗 [LinkedIn](https://www.linkedin.com/in/sina-shahsavand-ardabili-77693511a/)
- 💻 [GitHub](https://github.com/sinaardabili-stack)
- ✉️ sina.s.ardabil@gmail.com

---

## 📄 License

This project is licensed under the MIT License.

---

*Built as a practical demonstration of applied machine learning in industrial maintenance contexts.*
# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Dashboard starten
streamlit run app.py
