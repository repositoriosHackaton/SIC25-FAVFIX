import reflex as rx
from .components import sidebar, header
import httpx
from typing import Any
from .prueba import probar_prediccion  # Importar la función desde prueba.py

class UserInputState(rx.State):
    # Estado inicial del formulario
    form_data: dict = {}
    result: dict = {}

    def send_data_to_backend(self, data: dict[str, Any]) -> dict:
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

    @rx.event
    def handle_submit(self, form_data: dict):
        """Manejar el envío del formulario."""
        self.form_data = form_data
        
        # Calcular los resultados usando la función de prueba.py
        resultado = probar_prediccion(form_data["text"])
        
        # Actualizar el resultado
        self.result = {
            **form_data,
            "result": resultado["prediccion_suicidio"],
            "emotion": resultado["emocion"],
            "suicide_probability": resultado["probabilidad_suicidio"]
        }
        
        # Enviar los datos al backend
        self.send_data_to_backend(self.result)

# Página de entrada de datos del usuario
def user_input_page():
    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(title="Análisis de Texto"),
                rx.card(
                    rx.vstack(
                        rx.heading("Formulario de Entrada", size="5", color="rgb(107 114 128)"),
                        rx.form(
                            rx.vstack(
                                rx.hstack(
                                    rx.input(
                                        name="name",
                                        placeholder="Nombre",
                                        required=True,
                                        width="100%",
                                    ),
                                    rx.input(
                                        name="age",
                                        placeholder="Edad",
                                        type="number",
                                        required=True,
                                        width="100%",
                                    ),
                                    spacing="4",
                                    width="100%",
                                ),
                                rx.hstack(
                                    rx.input(
                                        name="gender",
                                        placeholder="Género",
                                        required=True,
                                        width="100%",
                                    ),
                                    rx.input(
                                        name="sector",
                                        placeholder="Sector",
                                        required=True,
                                        width="100%",
                                    ),
                                    spacing="4",
                                    width="100%",
                                ),
                                rx.text_area(
                                    name="text",
                                    placeholder="Ingrese el texto aquí...",
                                    required=True,
                                    height="150px",
                                    width="100%",
                                ),
                                rx.button(
                                    "Enviar",
                                    type="submit",
                                    width="100%",
                                    bg="blue.500",
                                    color="white",
                                    _hover={"bg": "blue.600"},
                                ),
                                width="100%",
                                spacing="4",
                            ),
                            on_submit=UserInputState.handle_submit,
                            reset_on_submit=True,
                            width="100%",
                        ),
                        rx.cond(
                            UserInputState.result,
                            rx.vstack(
                                rx.divider(padding_y="4"),
                                rx.heading("Resultados del Análisis", size="3", color="rgb(107 114 128)"),
                                rx.hstack(
                                    rx.vstack(
                                        rx.text("Predicción:", font_weight="bold"),
                                        rx.badge(
                                            UserInputState.result["result"],
                                            color_scheme="blue",
                                        ),
                                        align_items="start",
                                    ),
                                    rx.vstack(
                                        rx.text("Emoción:", font_weight="bold"),
                                        rx.badge(
                                            UserInputState.result["emotion"],
                                            color_scheme="green",
                                        ),
                                        align_items="start",
                                    ),
                                    rx.vstack(
                                        rx.text("Probabilidad:", font_weight="bold"),
                                        rx.badge(
                                            UserInputState.result["suicide_probability"],
                                            color_scheme="purple",
                                        ),
                                        align_items="start",
                                    ),
                                    justify="between",
                                    width="100%",
                                    padding_y="4",
                                ),
                            ),
                        ),
                        align_items="start",
                        width="100%",
                        spacing="4",
                    ),
                    width="100%",
                    max_width="800px",
                ),
                align_items="center",
                width="100%",
                padding="4",
            ),
            justify="center",
            width="100%",
        ),
        background="bg-gray-900",
        min_height="100vh",
    )