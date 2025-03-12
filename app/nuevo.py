import os
import pickle
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Imprimir el directorio de trabajo actual
print("Current working directory:", os.getcwd())

# Cargar los modelos entrenados y los vectorizadores
with open('app/modelo_sentimientos_regresin_logstica.pkl', 'rb') as f:
    sentiment_model_log_reg = pickle.load(f)