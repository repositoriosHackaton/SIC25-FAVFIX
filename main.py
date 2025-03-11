from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import glob
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Inicializar FastAPI
app = FastAPI()

# Cargar todos los modelos de detección de tendencias suicidas
modelos_suicidio = {}
for modelo_path in glob.glob("suicidio_*.pkl"):
    nombre_modelo = modelo_path.split(".pkl")[0]
    with open(modelo_path, 'rb') as f:
        modelos_suicidio[nombre_modelo] = pickle.load(f)

# Cargar el modelo de detección de emociones
with open("modelo_emociones.pkl", 'rb') as f:
    modelo_emociones = pickle.load(f)

# Definir el esquema de entrada
class TextoEntrada(BaseModel):
    texto: str

# Endpoint para predecir tendencias suicidas y emociones
@app.post("/predecir")
def predecir_tendencia_y_emocion(texto_entrada: TextoEntrada):
    # Preprocesar el texto de entrada
    texto_procesado = preprocesar_texto(texto_entrada.texto)
    
    # Realizar las predicciones con todos los modelos de suicidio
    probabilidades_suicidio = []
    for nombre_modelo, modelo in modelos_suicidio.items():
        probabilidad = modelo.predict_proba([texto_procesado])
        probabilidades_suicidio.append(probabilidad[0])
    
    # Calcular el promedio de las probabilidades de suicidio
    probabilidad_promedio_suicidio = np.mean(probabilidades_suicidio, axis=0)
    
    # Determinar si es suicidio o no basado en un umbral (por ejemplo, 0.5)
    umbral = 0.5
    prediccion_suicidio = "suicidio" if probabilidad_promedio_suicidio[1] >= umbral else "no suicidio"
    
    # Realizar la predicción de emoción
    emocion_predicha = modelo_emociones.predict([texto_procesado])[0]
    emociones = ["Tristeza", "Alegría", "Amor", "Enojo", "Miedo", "Sorpresa"]
    emocion_texto = emociones[emocion_predicha]
    
    return {
        "prediccion_suicidio": prediccion_suicidio,
        "probabilidad_suicidio": probabilidad_promedio_suicidio[1],
        "emocion": emocion_texto
    }

def preprocesar_texto(texto):
    # Inicializar stopwords y lematizador
    stop_words_english = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    # 1. Minúsculas 📝
    text = texto.lower()
    # 2. Eliminar puntuación ✂️
    text = ''.join([char for char in text if char not in string.punctuation])
    # 3. Tokenización 🔍
    tokens = text.split()
    # 4. Eliminar Stop Words 🚫
    tokens = [word for word in tokens if word not in stop_words_english]
    # 5. Lematización 🔄
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)