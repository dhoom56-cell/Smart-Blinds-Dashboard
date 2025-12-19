# ☀️ Smart Blinds IoT Monitoring System

This project is an interactive Streamlit dashboard designed to monitor IoT sensor
data related to light intensity and temperature. The system helps in controlling
smart blinds automatically to improve comfort and energy efficiency.

---

## 📌 Project Objectives
- Monitor environmental conditions using IoT sensors
- Analyze the relationship between light intensity and temperature
- Display the current status of smart blinds (Open / Closed)
- Provide interactive visualizations for better decision making

---

## 🛠️ Technologies Used
- **Python**
- **Streamlit** – for building the dashboard
- **Pandas** – for data processing
- **Plotly** – for interactive charts
- **OpenPyXL** – for reading Excel files

---

## 📂 Project Structure
smart-blinds-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
└── data/
└── iot final.xlsx


---

## ▶️ How to Run the Project Locally

1. Install the required libraries:
```bash
pip install -r requirements.txt


Run the Streamlit app:
streamlit run app.py

Open the browser and go to:
(http://16.170.225.196:8501)


📊 Dataset Description

The dataset contains IoT sensor readings with the following attributes:

Timestamp – date and time of measurement

Temperature (°C) – ambient temperature

Light Intensity (Lux) – measured light level

Blind Status – current state of the blinds (Open / Closed)


## ✅ Results
The dashboard provides:
- Real-time KPI indicators
- Interactive time-series plots
- Data filtering by date
- Clear visualization of blind status



