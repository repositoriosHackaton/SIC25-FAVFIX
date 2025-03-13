# Analista de emociones en entornos laborales

es una herramienta innovadora diseñada para analizar emociones en textos y detectar comportamientos basados en las emociones identificadas. Actualmente, estamos enfocados en la detección de depresión y su relación con la tasa de empleo y desempleo pre y post pandemia de COVID-19, con el objetivo de identificar patrones y coincidencias entre la salud mental y el mercado laboral. 

## Tabla de contenidos

1.  [Nombre](#nombre)
2.  [Descripción](#descripción)
3.  [Arquitectura](#arquitectura)
4.  [Proceso](#proceso)
5.  [Funcionalidades](#funcionalidades)
6.  [Estado del proyecto](#estado-del-proyecto)
7.  [Agradecimientos](#agradecimientos)

## Nombre

Analista de emociones en entornos laborales

## Descripción

El Analista de emociones  es una aplicación que utiliza técnicas avanzadas de procesamiento de lenguaje natural (NLP) para analizar publicaciones, comentarios y otros textos. La idea es proporcionar una herramienta que pueda ser utilizada en foros, redes sociales y otras plataformas para identificar emociones subyacentes, especialmente la depresión, y su relación con la tasa de empleo y desempleo pre y post pandemia de COVID-19.

### ¿Por qué es importante?

En el mundo digital de hoy, las personas comparten sus pensamientos y sentimientos en línea más que nunca. Emotion Analyzer tiene el potencial de ser una herramienta valiosa para investigadores, políticos y cualquier persona interesada en comprender mejor la relación entre la salud mental y el mercado laboral. Al identificar patrones entre la depresión y la falta de empleo, podemos ofrecer insights valiosos para la creación de políticas públicas y programas de apoyo. ❤️

[![Imagen del Proyecto]()]()

## Arquitectura

El proyecto se basa en una arquitectura modular que permite la integración de diferentes componentes y tecnologías. A continuación, se describe la arquitectura general del proyecto:

1.  **Recopilación de datos:** Se obtienen datos de diversas fuentes, como Kaggle, Twitter y fuentes gubernamentales.
2.  **Preprocesamiento de datos:** Se realiza una limpieza y transformación de los datos para prepararlos para el entrenamiento de los modelos.
3.  **Entrenamiento de modelos:** Se utilizan algoritmos de aprendizaje automático, como Regresión Lineal, Naive Bayes y SVM, para entrenar modelos de detección de emociones y depresión.
4.  **Desarrollo de la API:** Se crea una API utilizando FastAPI para exponer los modelos entrenados y permitir su integración con otras aplicaciones.
5.  **Desarrollo de la interfaz web:** Se desarrolla una interfaz web interactiva utilizando Reflex para permitir a los usuarios ingresar texto y obtener una predicción en tiempo real.

[![Arquitectura del Proyecto]()]()

## Proceso

### Fuente del Dataset

Para entrenar nuestros modelos, utilizamos un conjunto de datos de textos etiquetados que contienen indicios de depresión y datos sobre la tasa de empleo y desempleo pre y post pandemia de COVID-19. Las fuentes del dataset incluyen:

* Kaggle: Suicide and Depression Detection
* Datos extraídos de Twitter, que fueron clasificados manualmente.
* Datos de empleo y desempleo de fuentes gubernamentales y organizaciones internacionales.

### Limpieza de Datos

No se utilizó una limpieza de datos exhaustiva ya que las fuentes fueron bastante certeras y minimalistas. A continuación, mostramos el flujo de datos de cada dataset.

[![Limpieza de Datos]()]()

### Manejo de Excepciones/Control de Errores

Implementamos diversas técnicas para manejar excepciones y controlar errores durante el preprocesamiento y análisis de los datos.

### Estadísticos

Incluimos análisis estadísticos y gráficos para entender mejor la distribución de los datos y el rendimiento de los modelos.

[![Estadísticos]()]()

[![Estadísticos]()]()

[![Estadísticos]()]()

[![Estadísticos]()]()

## Funcionalidades

El proyecto Emotion Analyzer ofrece las siguientes funcionalidades:

*   **Análisis de emociones en textos:** Permite identificar y clasificar las emociones presentes en un texto dado.
*   **Detección de depresión:** Permite detectar la presencia de depresión en un texto dado.
*   **Relación entre depresión y empleo:** Permite analizar la relación entre la depresión y la tasa de empleo y desempleo pre y post pandemia de COVID-19.
*   **Predicción en tiempo real:** Permite a los usuarios ingresar texto y obtener una predicción en tiempo real a través de la interfaz web.
*   **API para integración:** Proporciona una API para integrar los modelos entrenados con otras aplicaciones.

### Entrenamiento de los modelos

* Modelos: Regresión Lineal, Naive Bayes, SVM.
* Arquitectura:
    * Modelo de sentimientos:
        * [![Arquitectura del modelo]()]())
        * [![Arquitectura del modelo]()]()
        * [![Arquitectura del modelo]()]()
    * Modelo de depresión:
        * [![Arquitectura del modelo]()]()
        * [![Arquitectura del modelo]()]()
        * [![Arquitectura del modelo]()]()

### Integración del Proyecto en una Página Web

Utilizamos Reflex para desarrollar una interfaz interactiva que permite a los usuarios ingresar texto y obtener una predicción en tiempo real a traves de fasAPI.

* Tecnología/Herramientas usadas: Reflex, Python, Scikit-learn
* Arquitectura:
    * [![Arquitectura de la API]()]()

### Desarrollo de la API

Desarrollamos una api para poder procesar el texto y hacer la prediccion con el modelo de forma mas eficaz

* Tecnología/Herramientas usadas: FastAPI
* Arquitectura:
    * [![Arquitectura de la Interfaz Gráfica]()]()
* Tecnología/Herramientas usadas: Reflex, HTML, CSS, JavaScript

## Estado del Proyecto

Emotion Analyzer está en continuo desarrollo. Actualmente, hemos implementado la detección de depresión y su relación con la tasa de empleo y desempleo pre y post pandemia de COVID-19. Estamos trabajando en mejorar la precisión y expandir las capacidades del modelo para incluir más variables socioeconómicas.

## Agradecimientos

Este proyecto ha sido desarrollado como parte del curso de Samsung Innovation Campus. Agradecemos a Samsung por la oportunidad y el apoyo brindado para llevar a cabo este proyecto.