import reflex as rx
from .components import sidebar, header, stats_card
import httpx

# Función para obtener datos del backend (con manejo de errores)
def fetch_data():
    try:
        with httpx.Client() as client:
            response = client.get("http://localhost:8000/users")
            if response.status_code == 200:
                return response.json()["users"]
            else:
                return []
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

# Página de Admin
def admin_page():
    # Datos predeterminados en caso de que el backend no responda
    default_stats = [
        {"title": "Visitors", "value": "0", "icon": "users"},
        {"title": "Messages", "value": "0", "icon": "message-circle"},
        {"title": "Users", "value": "0", "icon": "user"},
    ]

    # Obtener datos del backend (o usar datos predeterminados)
    users_data = fetch_data()

    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(),
                rx.hstack(
                    *[stats_card(stat["title"], stat["value"], stat["icon"]) for stat in default_stats],
                    spacing="4",
                    padding="4",
                ),
                rx.box(
                    rx.heading("User Analysis", size="5", padding="4"),  # Tamaño ajustado a valor numérico válido
                    rx.cond(
                        users_data,  # Si hay datos, mostrar la tabla
                        rx.box(
                            rx.box(
                                rx.text("ID", font_weight="bold"),
                                rx.text("Name", font_weight="bold"),
                                rx.text("Age", font_weight="bold"),
                                rx.text("Gender", font_weight="bold"),
                                rx.text("Sector", font_weight="bold"),
                                rx.text("Result", font_weight="bold"),
                                rx.text("Emotion", font_weight="bold"),
                                rx.text("Suicide Probability", font_weight="bold"),
                                display="flex",
                                justify_content="space-between",
                                padding="4",
                                background="bg-gray-800",
                            ),
                            *[
                                rx.box(
                                    rx.text(str(user["id"])),
                                    rx.text(user["name"]),
                                    rx.text(str(user["age"])),
                                    rx.text(user["gender"]),
                                    rx.text(user["sector"]),
                                    rx.text(user["result"]),
                                    rx.text(user["emotion"]),
                                    rx.text(f"{user['suicide_probability']:.2f}"),
                                    display="flex",
                                    justify_content="space-between",
                                    padding="4",
                                    border_bottom="1px solid gray",
                                )
                                for user in users_data
                            ],
                            width="100%",
                            background="bg-gray-700",
                            color="text-white",
                        ),
                        rx.text("No data available", padding="4"),  # Si no hay datos, mostrar un mensaje
                    ),
                    padding="4",
                ),
                width="100%",
            ),
            height="100vh",
        ),
        background="bg-gray-900",
        color="text-white",
    )

# Página de Usuarios
def users_page():
    # Datos predeterminados en caso de que el backend no responda
    default_stats = [
        {"title": "Total Users", "value": "0", "icon": "user"},
        {"title": "Active Users", "value": "0", "icon": "user-check"},
        {"title": "Inactive Users", "value": "0", "icon": "user-x"},
    ]

    # Obtener datos del backend (o usar datos predeterminados)
    users_data = fetch_data()

    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(title="Users"),
                rx.hstack(
                    *[stats_card(stat["title"], stat["value"], stat["icon"]) for stat in default_stats],
                    spacing="4",
                    padding="4",
                ),
                rx.box(
                    rx.heading("User Management", size="5", padding="4"),  # Tamaño ajustado a valor numérico válido
                    rx.cond(
                        users_data,  # Si hay datos, mostrar la tabla
                        rx.box(
                            rx.box(
                                rx.text("ID", font_weight="bold"),
                                rx.text("Name", font_weight="bold"),
                                rx.text("Age", font_weight="bold"),
                                rx.text("Gender", font_weight="bold"),
                                rx.text("Sector", font_weight="bold"),
                                rx.text("Result", font_weight="bold"),
                                rx.text("Emotion", font_weight="bold"),
                                rx.text("Suicide Probability", font_weight="bold"),
                                display="flex",
                                justify_content="space-between",
                                padding="4",
                                background="bg-gray-800",
                            ),
                            *[
                                rx.box(
                                    rx.text(str(user["id"])),
                                    rx.text(user["name"]),
                                    rx.text(str(user["age"])),
                                    rx.text(user["gender"]),
                                    rx.text(user["sector"]),
                                    rx.text(user["result"]),
                                    rx.text(user["emotion"]),
                                    rx.text(f"{user['suicide_probability']:.2f}"),
                                    display="flex",
                                    justify_content="space-between",
                                    padding="4",
                                    border_bottom="1px solid gray",
                                )
                                for user in users_data
                            ],
                            width="100%",
                            background="bg-gray-700",
                            color="text-white",
                        ),
                        rx.text("No data available", padding="4"),  # Si no hay datos, mostrar un mensaje
                    ),
                    padding="4",
                ),
                width="100%",
            ),
            height="100vh",
        ),
        background="bg-gray-900",
        color="text-white",
    )

# Página de Mensajes
def messages_page():
    # Datos predeterminados en caso de que el backend no responda
    default_stats = [
        {"title": "Total Messages", "value": "0", "icon": "message-circle"},
        {"title": "Unread Messages", "value": "0", "icon": "mail"},
        {"title": "Read Messages", "value": "0", "icon": "mail-open"},
    ]

    # Obtener datos del backend (o usar datos predeterminados)
    messages_data = fetch_data()

    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(title="Messages"),
                rx.hstack(
                    *[stats_card(stat["title"], stat["value"], stat["icon"]) for stat in default_stats],
                    spacing="4",
                    padding="4",
                ),
                rx.box(
                    rx.heading("Messages", size="5", padding="4"),  # Tamaño ajustado a valor numérico válido
                    rx.cond(
                        messages_data,  # Si hay datos, mostrar la tabla
                        rx.box(
                            rx.box(
                                rx.text("ID", font_weight="bold"),
                                rx.text("Sender", font_weight="bold"),
                                rx.text("Recipient", font_weight="bold"),
                                rx.text("Subject", font_weight="bold"),
                                rx.text("Message", font_weight="bold"),
                                rx.text("Status", font_weight="bold"),
                                display="flex",
                                justify_content="space-between",
                                padding="4",
                                background="bg-gray-800",
                            ),
                            *[
                                rx.box(
                                    rx.text(str(message["id"])),
                                    rx.text(message["sender"]),
                                    rx.text(message["recipient"]),
                                    rx.text(message["subject"]),
                                    rx.text(message["message"]),
                                    rx.text(message["status"]),
                                    display="flex",
                                    justify_content="space-between",
                                    padding="4",
                                    border_bottom="1px solid gray",
                                )
                                for message in messages_data
                            ],
                            width="100%",
                            background="bg-gray-700",
                            color="text-white",
                        ),
                        rx.text("No data available", padding="4"),  # Si no hay datos, mostrar un mensaje
                    ),
                    padding="4",
                ),
                width="100%",
            ),
            height="100vh",
        ),
        background="bg-gray-900",
        color="text-white",
    )

# Página de Configuración
def settings_page():
    # Datos predeterminados en caso de que el backend no responda
    default_stats = [
        {"title": "Settings Changed", "value": "0", "icon": "settings"},
        {"title": "Pending Changes", "value": "0", "icon": "clock"},
        {"title": "Completed Changes", "value": "0", "icon": "circle_check"},
    ]

    # Obtener datos del backend (o usar datos predeterminados)
    settings_data = fetch_data()

    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                header(title="Settings"),
                rx.hstack(
                    *[stats_card(stat["title"], stat["value"], stat["icon"]) for stat in default_stats],
                    spacing="4",
                    padding="4",
                ),
                rx.box(
                    rx.heading("Settings Management", size="5", padding="4"),  # Tamaño ajustado a valor numérico válido
                    rx.cond(
                        settings_data,  # Si hay datos, mostrar la tabla
                        rx.box(
                            rx.box(
                                rx.text("ID", font_weight="bold"),
                                rx.text("Setting", font_weight="bold"),
                                rx.text("Value", font_weight="bold"),
                                rx.text("Status", font_weight="bold"),
                                display="flex",
                                justify_content="space-between",
                                padding="4",
                                background="bg-gray-800",
                            ),
                            *[
                                rx.box(
                                    rx.text(str(setting["id"])),
                                    rx.text(setting["setting"]),
                                    rx.text(setting["value"]),
                                    rx.text(setting["status"]),
                                    display="flex",
                                    justify_content="space-between",
                                    padding="4",
                                    border_bottom="1px solid gray",
                                )
                                for setting in settings_data
                            ],
                            width="100%",
                            background="bg-gray-700",
                            color="text-white",
                        ),
                        rx.text("No data available", padding="4"),  # Si no hay datos, mostrar un mensaje
                    ),
                    padding="4",
                ),
                width="100%",
            ),
            height="100vh",
        ),
        background="bg-gray-900",
        color="text-white",
    )