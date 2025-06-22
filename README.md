# 🚚 Predicción de Entregas Tardías – Kankay

Este proyecto utiliza un modelo de Machine Learning (Random Forest) para predecir si una entrega será tardía o no, en base a variables como la ciudad de destino, el tipo de envío, el día y hora, entre otros. Esta es una herramienta pensada para ayudar a Kankay a optimizar su logística!

## 🚀 Estructura del proyecto
📂 kankay-modelo/
├── app.py # App de Streamlit
├── modelo_entregas_kankay_comprimido.pkl # Modelo entrenado (comprimido con joblib)
├── kankay_datos_limpios.csv # Dataset limpio original
└── README.md # Este archivo

## 🧪 ¿Qué incluye?

- Limpieza y preprocesamiento de datos de entregas.
- Análisis de las variables más importantes.
- Entrenamiento de un modelo de clasificación (Random Forest).
- Métricas de validación (accuracy, precision, recall, F1-score).
- Aplicación interactiva con **Streamlit** para predecir futuras entregas.
- Carga del modelo desde `.pkl` y transformación dinámica del input del usuario.

## 🧑‍💻 Ejecución

**👉 Ver la app en [Streamlit ](https://kankaylogistica.streamlit.app/) 👈**
