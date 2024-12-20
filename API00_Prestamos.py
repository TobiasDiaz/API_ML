#Integrantes de la tarea 3 del modulo 3:
#Nombre                                      Correos:
#Tobias Alexander Santamria Diaz             tobias.santamaria@baccredomatic.sv
#Carlos Isaac Flores Aparicio                carlos.flores@baccredomatic.sv
#Willian Alexander Saravia Cuellar           willian.saravia@baccredomatic.sv
#Carlos Eduardo Fuentes Romero               carlos_romero@baccredomatic.sv
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests

# Título de la aplicación
st.title("Predicción de Préstamos Bancarios 💳")

# Descripción breve
st.write("""
Esta aplicación predice si un préstamo será aprobado o no.
Ingresa tus datos financieros y obtén la predicción en tiempo real.
""")

# URL de la API Flask (ajústala si la API está en otro servidor o puerto)
API_URL = "http://127.0.0.1:8000/predict"  # Asegúrate de que esta URL sea la correcta

# Formulario para ingresar los datos
with st.form("prediction_form"):
    st.subheader("Ingresa tus datos para el préstamo:")
    
    # Campos de entrada
    age = st.number_input("Edad:", min_value=18, step=1)
    income = st.number_input("Ingreso mensual ($):", min_value=0.0, step=100.0)
    credit_score = st.number_input("Puntaje crediticio:", min_value=300, max_value=850, step=1)
    loan_amount = st.number_input("Monto del préstamo solicitado ($):", min_value=0.0, step=100.0)
    loan_term = st.number_input("Plazo del préstamo (en años):", min_value=1, step=1)

    # Botón de predicción
    submitted = st.form_submit_button("Predecir Aprobación del Préstamo")

if submitted:
    # Crear el payload para la API
    payload = {
        "age": age,
        "income": income,
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "loan_term": loan_term
    }
    
    try:
        # Enviar la solicitud POST a la API Flask
        response = requests.post(API_URL, json=payload)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            result = response.json()
            # Mostrar el resultado en la interfaz de usuario
            if result['approval'] == "approved":
                st.success("¡Tu préstamo ha sido **APROBADO**! 💰")
            else:
                st.error("Lo siento, tu préstamo **NO HA SIDO APROBADO**. ❌")
        else:
            st.error(f"Error en la predicción: {response.json().get('error')}")
    except Exception as e:
        st.error(f"No se pudo conectar a la API: {e}")


# In[ ]:




