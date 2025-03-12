import reflex as rx

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

# Componente del Sidebar
def sidebar(links=None):
    if links is None:
        links = [
            {"text": "Dashboard", "href": "/admin"},
            {"text": "Users", "href": "/admin/users"},
            {"text": "Messages", "href": "/admin/messages"},
            {"text": "Settings", "href": "/admin/settings"},
        ]
    return rx.box(
        rx.vstack(
            rx.heading("Admin Panel", size="5"),  # Tamaño ajustado a valor numérico
            rx.divider(),
            rx.vstack(
                *[rx.link(link["text"], href=link["href"], padding="2", _hover={"background": "gray-700"}) for link in links],
                spacing="2",
                width="100%",
            ),
            align_items="start",
            padding="4",
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
            rx.heading(title, size="5"),  # Tamaño ajustado a valor numérico
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
            rx.heading(value, size="6"),  # Tamaño ajustado a valor numérico
            rx.text(title),
            rx.icon(icon, size=24),  # Tamaño ajustado a valor numérico entero
            align_items="center",
            spacing="2",
        ),
        padding="4",
        border_radius="5",
        background=styles["dark"]["card"],
        color=styles["dark"]["text"],
        width="100%",
    )