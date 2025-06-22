import streamlit as st
import pandas as pd
import joblib
import gdown

# import desde google drive
#url = "https://drive.google.com/uc?id=TU_ID_DE_DRIVE"  # Reemplazá con tu ID
#output = "modelo_entregas_kankay_comprimido.pkl"
#gdown.download(url, output, quiet=False)

# modelo = joblib.load(output)

modelo = joblib.load("modelo_entregas_kankay_comprimido.pkl")

# Input
st.title("🚚 Predicción de Entregas Tardías – Kankay")

st.write("Completá los datos de la entrega para predecir si será tardía o no.")

# Variables requeridas 

formas_entrega = ['Mercado Envíos Flex', 'Mercado Envíos Full', 'Correo y puntos de despacho']

ciudades = ['Córdoba', 'Rosario', 'Palermo', 'Mar del Plata', 'Belgrano', 'La Plata', 'Recoleta', 'Caballito', 'La Matanza', 'Grand Bourg', 'Villa Urquiza', 'Colegiales', 'Pilar', 'Núñez', 'San Isidro', 'Bahía Blanca', 'Neuquén', 'San Miguel de Tucumán', 'Villa Crespo', 'Balvanera' ]

forma_entrega = st.selectbox("Forma de entrega", formas_entrega)
ciudad = st.selectbox("Ciudad", ciudades)
dia_semana = st.selectbox("Día de la semana", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
mes = st.selectbox("Mes", ['January', 'February', 'March', 'April', 'May', 'June'])
hora = st.slider("Hora de entrega (0-23)", 0, 23, 12)

st.write("📋 Datos de entrada procesados:")
st.dataframe(input_df)

# --- Preparamos los datos de entrada ---
if st.button("📊 Predecir"):
    input_dict = {
        'Forma de entrega': [forma_entrega],
        'Ciudad': [ciudad],
        'dia_semana': [dia_semana],
        'mes': [mes],
        'hora': [hora]
    }
    input_df = pd.DataFrame(input_dict)

    # One-hot encoding (igual que el training)
    input_encoded = pd.get_dummies(input_df)
    
    # Alineamos con las columnas del modelo
    for col in modelo.feature_names_in_:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[modelo.feature_names_in_]

    # Predicción
    pred = modelo.predict(input_encoded)[0]
    proba = modelo.predict_proba(input_encoded)[0][1]

    if pred == 1:
        st.error(f"⚠️ ¡Atención! Alta probabilidad de entrega tardía. ({proba:.1%})")
    else:
        st.success(f"✅ Entrega a tiempo estimada. (Probabilidad de demora: {proba:.1%})")

