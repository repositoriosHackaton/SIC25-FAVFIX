from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sqlite3
import httpx

# Inicializar FastAPI
app = FastAPI()

# Cargar los modelos entrenados y los vectorizadores
with open('modelos/modelo_sentimientos_regresin_logstica.pkl', 'rb') as f:
    sentiment_model_log_reg = pickle.load(f)

with open('modelos/modelo_sentimientos_naive_bayes.pkl', 'rb') as f:
    sentiment_model_nb = pickle.load(f)

with open('modelos/modelo_sentimientos_random_forest_random_forest.pkl', 'rb') as f:
    sentiment_model_rf = pickle.load(f)

with open('modelos/modelo_sentimientos_xgboost_xgboost.pkl', 'rb') as f:
    sentiment_model_xgb = pickle.load(f)

with open('modelos/modelo_depresion_regresin_logstica.pkl', 'rb') as f:
    suicide_model_log_reg = pickle.load(f)

with open('modelos/modelo_depresion_naive_bayes.pkl', 'rb') as f:
    suicide_model_nb = pickle.load(f)

with open('modelos/modelo_depresion_random_forest_random_forest.pkl', 'rb') as f:
    suicide_model_rf = pickle.load(f)

with open('modelos/modelo_depresion_xgboost_xgboost.pkl', 'rb') as f:
    suicide_model_xgb = pickle.load(f)

with open('modelos/tfidf_vectorizador_sentimientos.pkl', 'rb') as f:
    tfidf_vectorizer_sentiment = pickle.load(f)

with open('modelos/tfidf_vectorizador_depresion.pkl', 'rb') as f:
    tfidf_vectorizer_suicide = pickle.load(f)

stop_words_english = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla de usuarios si no existe
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            sector TEXT,
            text TEXT,
            result TEXT,
            emotion TEXT,
            suicide_probability REAL
        )
    ''')
    conn.commit()
    conn.close()

# Preprocesar el texto
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words_english]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Modelo de entrada
class TextoEntrada(BaseModel):
    name: str
    age: int
    gender: str
    sector: str
    text: str

# Endpoint para predecir y guardar en la base de datos
@app.post("/predecir")
def predecir_tendencia_y_emocion(texto_entrada: TextoEntrada):
    try:
        # Preprocesar el texto de entrada
        texto_procesado = preprocess_text(texto_entrada.text)
        
        # Vectorizar el texto
        texto_vectorizado_sentiment = tfidf_vectorizer_sentiment.transform([texto_procesado])
        texto_vectorizado_suicide = tfidf_vectorizer_suicide.transform([texto_procesado])
        
        # Realizar las predicciones con todos los modelos de suicidio excepto SVM
        probabilidades_suicidio = []
        for modelo in [suicide_model_log_reg, suicide_model_nb, suicide_model_rf, suicide_model_xgb]:
            probabilidad = modelo.predict_proba(texto_vectorizado_suicide)
            probabilidades_suicidio.append(probabilidad[0])
        
        probabilidad_promedio_suicidio = np.mean(probabilidades_suicidio, axis=0)
        
        umbral = 0.5
        prediccion_suicidio = "suicidio" if probabilidad_promedio_suicidio[1] >= umbral else "no suicidio"
        
        # Realizar las predicciones con todos los modelos de emociones excepto SVM
        emociones_predichas = []
        for modelo in [sentiment_model_log_reg, sentiment_model_nb, sentiment_model_rf, sentiment_model_xgb]:
            emocion_predicha = modelo.predict(texto_vectorizado_sentiment)[0]
            emociones_predichas.append(emocion_predicha)
        
        emocion_final = max(set(emociones_predichas), key=emociones_predichas.count)
        emociones = ["Tristeza", "Alegría", "Amor", "Enojo", "Miedo", "Sorpresa"]
        emocion_texto = emociones[emocion_final]
        
        # Guardar en la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age, gender, sector, text, result, emotion, suicide_probability)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            texto_entrada.name,
            texto_entrada.age,
            texto_entrada.gender,
            texto_entrada.sector,
            texto_entrada.text,
            prediccion_suicidio,
            emocion_texto,
            float(probabilidad_promedio_suicidio[1])
        ))
        conn.commit()
        conn.close()
        
        return {
            "prediccion_suicidio": prediccion_suicidio,
            "probabilidad_suicidio": probabilidad_promedio_suicidio[1],
            "emocion": emocion_texto
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para obtener todos los usuarios
@app.get("/users")
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para realizar una solicitud asíncrona
@app.get("/fetch_users")
async def fetch_users():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("http://localhost:8000/users")
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Error fetching users")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear la tabla al iniciar la API
create_table()