import reflex as rx
import httpx
from typing import List, Dict, Any
from datetime import datetime

# Define un modelo de datos para la información de las emociones
class EmotionData(rx.Base):
    emotion: str
    count: int
    time: datetime

class SectorSentiment(rx.Base):
    sector: str
    average_suicide_probability: float
    time: datetime

class UsersState(rx.State):
    """Define el estado reactivo para la página de Usuarios."""

    emotion_data: List[EmotionData] = []
    sector_sentiment_data: List[SectorSentiment] = []
    time_interval: int = 60  # Intervalo de tiempo predeterminado en minutos
    is_loading: bool = False

    async def fetch_emotion_data(self):
        """Obtiene los datos de las emociones desde el backend."""
        self.is_loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"http://localhost:8000/emotions_over_time?time_interval={self.time_interval}"
                )
                if response.status_code == 200:
                    # Analiza la respuesta JSON y crea objetos EmotionData
                    data = response.json()
                    self.emotion_data = [EmotionData(**item) for item in data]
                else:
                    print(f"Error al obtener los datos: {response.status_code}")
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
        finally:
            self.is_loading = False

    async def fetch_sector_sentiment_data(self):
        """Obtiene el sentimiento promedio por sector desde el backend."""
        self.is_loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"http://localhost:8000/sentiment_by_sector?time_interval={self.time_interval}"
                )
                if response.status_code == 200:
                    # Analiza la respuesta JSON y crea objetos SectorSentiment
                    data = response.json()
                    self.sector_sentiment_data = [SectorSentiment(**item) for item in data]
                else:
                    print(f"Error al obtener los datos: {response.status_code}")
        except Exception as e:
            print(f"Error al obtener los datos: {e}")
        finally:
            self.is_loading = False

    def set_time_interval(self, interval: int):
        """Establece el intervalo de tiempo y actualiza los datos."""
        self.time_interval = interval
        # rx.console.log(f"Intervalo de tiempo establecido en: {self.time_interval}") #debugging
        return [self.fetch_emotion_data, self.fetch_sector_sentiment_data]  # Devuelve ambos manejadores de eventos

def emotion_chart():
    """Crea el componente del gráfico de emociones."""
    return rx.cond(
        UsersState.is_loading,
        rx.spinner(),
        rx.recharts.bar_chart(  # Usa un gráfico de barras para intervalos de tiempo discretos
            rx.recharts.bar(
                data_key="count",
                stroke=rx.color("blue", 5),
                fill=rx.color("blue", 4),
            ),
            rx.recharts.x_axis(
                data_key="time",
                tick_formatter=lambda x: datetime.fromisoformat(x).strftime("%H:%M"),  # Formatea la hora
                angle=-45,
                text_anchor="end",
                height=80,  # Ajusta la altura para las etiquetas rotadas
            ),
            rx.recharts.y_axis(
                type="number",
                domain=[0, 'dataMax + 1']  # Dominio dinámico del eje Y
            ),
            rx.recharts.tooltip(),
            rx.recharts.cartesian_grid(horizontal=False, vertical=True),
            data=UsersState.emotion_data,
        ),
    )

def sector_sentiment_chart():
    """Crea el componente del gráfico de sentimiento por sector."""
    return rx.cond(
        UsersState.is_loading,
        rx.spinner(),
        rx.recharts.line_chart(  # Usa un gráfico de líneas para mostrar tendencias
            rx.recharts.line(
                data_key="average_suicide_probability",
                stroke=rx.color("green", 5),
            ),
            rx.recharts.x_axis(
                data_key="time",
                tick_formatter=lambda x: datetime.fromisoformat(x).strftime("%H:%M"),  # Formatea la hora
                angle=-45,
                text_anchor="end",
                height=80,  # Ajusta la altura para las etiquetas rotadas
            ),
            rx.recharts.y_axis(
                type="number",
                domain=[0, 1]  # El dominio de la probabilidad de suicidio es entre 0 y 1
            ),
            rx.recharts.tooltip(),
            rx.recharts.cartesian_grid(horizontal=False, vertical=True),
            data=UsersState.sector_sentiment_data,
        ),
    )

def users_page():
    """La página de configuración."""
    return rx.vstack(
        rx.heading("Análisis de Usuarios", font_size="2em"),
        rx.hstack(
            rx.text("Intervalo de Tiempo (minutos):"),
            rx.number_input(
                value=UsersState.time_interval,
                on_change=UsersState.set_time_interval,
                min=1,
                max=1440,  # Hasta 24 horas
            ),
        ),
        emotion_chart(),
        sector_sentiment_chart(),  # Agrega el nuevo gráfico
        rx.button("Actualizar Datos", on_click=UsersState.fetch_emotion_data),  # Agrega un botón de actualización
        on_mount=[UsersState.fetch_emotion_data, UsersState.fetch_sector_sentiment_data],  # Carga los datos al cargar la página
        align_items="start",
        spacing="4",
        padding="4",
    )