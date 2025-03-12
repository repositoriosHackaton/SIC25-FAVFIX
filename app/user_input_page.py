import reflex as rx
from .components import sidebar, header
import httpx
import sys
import os

from .prueba import probar_prediccion  # Importar la función desde prueba.py

# Función para enviar datos al backend
def send_data_to_backend(data):
    try:
        with httpx.Client() as client:
            response = client.post("http://localhost:8000/predecir", json=data)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Failed to send data"}
    except Exception as e:
        print(f"Error sending data: {e}")
        return {"error": str(e)}

# Función para manejar el envío del formulario
def handle_form_submit(form_data):
    # Calcular los resultados usando la función de prueba.py
    resultado = probar_prediccion(form_data["text"])
    
    # Agregar los resultados al formulario de datos
    form_data["result"] = resultado["prediccion_suicidio"]
    form_data["emotion"] = resultado["emocion"]
    form_data["suicide_probability"] = resultado["probabilidad_suicidio"]
    
    # Enviar los datos al backend
    return send_data_to_backend(form_data)

# Página de entrada de datos del usuario
def user_input_page():
    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(title="User Input"),
                rx.form(
                    rx.input(name="name", placeholder="Name", required=True),
                    rx.input(name="age", placeholder="Age", type="number", required=True),
                    rx.input(name="gender", placeholder="Gender", required=True),
                    rx.input(name="sector", placeholder="Sector", required=True),
                    rx.textarea(name="text", placeholder="Enter text here...", required=True),
                    rx.button("Submit", type="submit", background="bg-blue-500", color="text-white"),
                    on_submit=lambda form_data: handle_form_submit(form_data),
                    padding="4",
                ),
                width="100%",
                padding="4",
            ),
            height="100vh",
        ),
        background="bg-gray-900",
        color="text-white",
    )