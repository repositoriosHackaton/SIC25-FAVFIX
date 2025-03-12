import reflex as rx
from typing import Union, List

# Estilos personalizados
styles = {
    "dark": {
        "background": "bg-gray-900",
        "text": "text-white",
        "sidebar": "bg-gray-800",
        "header": "bg-gray-700",
        "card": "bg-gray-700",
        "button": "bg-blue-500 hover:bg-blue-600 text-white",
    },
}

class SidebarState(rx.State):
    # Estado inicial
    control: str = "admin"

    def set_section(self, value: Union[str, List[str]]):
        """Actualizar la sección seleccionada."""
        # Si value es una lista, tomamos el primer elemento
        self.control = value[0] if isinstance(value, list) else value
        return rx.redirect(f"/{self.control}")

# Componente del Sidebar
def sidebar():
    return rx.box(
        rx.hstack(
            rx.heading("FavFix", size="5"),
            rx.divider(),
            # Navegación principal con Segmented Control
            rx.segmented_control.root(
                rx.segmented_control.item(
                    rx.hstack(
                        rx.icon("archive-restore", color="rgb(156 163 175)", size=15),
                        rx.text("messages"),
                        spacing="2",
                    ),
                    value="messages"
                ),
                rx.segmented_control.item(
                    rx.hstack(
                        rx.icon("contact", color="rgb(156 163 175)", size=15),
                        rx.text("users"),
                        spacing="2",
                    ),
                    value="users"
                ),
                rx.segmented_control.item(
                    rx.hstack(
                        rx.icon("hammer", color="rgb(156 163 175)", size=15),
                        rx.text("Settings"),
                        spacing="2",
                    ),
                    value="settings"
                ),
                on_change=SidebarState.set_section,
                value=SidebarState.control,
                width="100%",
            ),
            align_items="start",
            padding="4",
            spacing="4",
            width="100%",
        ),
        width="250px",
        height="100vh",
        background=styles["dark"]["sidebar"],
        color=styles["dark"]["text"],
    )

# Componente del Header
def header(title="Admin Dashboard", button_text="Logout"):
    return rx.box(
        rx.hstack(
            rx.heading(title, size="5"),
            rx.spacer(),
            rx.button(button_text, background=styles["dark"]["button"], padding="2"),
            padding="4",
            width="100%",
        ),
        background=styles["dark"]["header"],
        color=styles["dark"]["text"],
    )

# Tarjetas de Estadísticas
def stats_card(title="Title", value="Value", icon="icon"):
    return rx.box(
        rx.vstack(
            rx.heading(value, size="6"),
            rx.text(title),
            rx.icon(icon, size=24),
            align_items="center",
            spacing="2",
        ),
        padding="4",
        border_radius="5",
        background=styles["dark"]["card"],
        color=styles["dark"]["text"],
        width="100%",
    )