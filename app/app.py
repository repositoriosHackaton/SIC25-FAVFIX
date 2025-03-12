import reflex as rx
from .pages import admin_page, users_page, messages_page, settings_page

# Configuración de la aplicación
app = rx.App()

# Agregar páginas
app.add_page(admin_page, route="/admin")
app.add_page(users_page, route="/admin/users")
app.add_page(messages_page, route="/admin/messages")
app.add_page(settings_page, route="/admin/settings")

