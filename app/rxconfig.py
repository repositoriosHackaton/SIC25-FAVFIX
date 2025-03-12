import reflex as rx

config = rx.Config(
    app_name="app",
    api_url="http://localhost:8000",  # URL del backend
    env=rx.Env.DEV,
) 