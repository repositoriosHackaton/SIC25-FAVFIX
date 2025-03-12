import os
import pickle
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Imprimir el directorio de trabajo actual
print("Current working directory:", os.getcwd())

# Cargar los modelos entrenados y los vectorizadores
with open('modelo_sentimientos_regresin_logstica.pkl', 'rb') as f:
    sentiment_model_log_reg = pickle.load(f)

with open('modelo_sentimientos_naive_bayes.pkl', 'rb') as f:
    sentiment_model_nb = pickle.load(f)

with open('modelo_sentimientos_random_forest_random_forest.pkl', 'rb') as f:
    sentiment_model_rf = pickle.load(f)

with open('modelo_sentimientos_xgboost_xgboost.pkl', 'rb') as f:
    sentiment_model_xgb = pickle.load(f)

with open('modelo_depresion_regresin_logstica.pkl', 'rb') as f:
    suicide_model_log_reg = pickle.load(f)

with open('modelo_depresion_naive_bayes.pkl', 'rb') as f:
    suicide_model_nb = pickle.load(f)

with open('modelo_depresion_random_forest_random_forest.pkl', 'rb') as f:
    suicide_model_rf = pickle.load(f)

with open('modelo_depresion_xgboost_xgboost.pkl', 'rb') as f:
    suicide_model_xgb = pickle.load(f)

with open('tfidf_vectorizador_sentimientos.pkl', 'rb') as f:
    tfidf_vectorizer_sentiment = pickle.load(f)

with open('tfidf_vectorizador_depresion.pkl', 'rb') as f:
    tfidf_vectorizer_suicide = pickle.load(f)

stop_words_english = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words_english]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def probar_prediccion(texto_entrada):
    # Preprocesar el texto de entrada
    texto_procesado = preprocess_text(texto_entrada)
    
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
    
    return {
        "prediccion_suicidio": prediccion_suicidio,
        "probabilidad_suicidio": probabilidad_promedio_suicidio[1],
        "emocion": emocion_texto
    }

# Prueba con un texto de ejemplo en inglés
if __name__ == "__main__":
    resultado = probar_prediccion("I feel very sad and hopeless.")
    print(resultado)