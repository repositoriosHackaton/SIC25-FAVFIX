# Emotion Analyzer

Emotion Analyzer es una herramienta innovadora diseñada para analizar emociones en textos y detectar comportamientos basados en las emociones identificadas. Actualmente, estamos enfocados en la detección de depresión y su relación con la tasa de empleo y desempleo pre y post pandemia de COVID-19, con el objetivo de identificar patrones y coincidencias entre la salud mental y el mercado laboral. 

## Tabla de contenidos

1.  [Nombre](#nombre)
2.  [Descripción](#descripción)
3.  [Arquitectura](#arquitectura)
4.  [Proceso](#proceso)
5.  [Funcionalidades](#funcionalidades)
6.  [Estado del proyecto](#estado-del-proyecto)
7.  [Agradecimientos](#agradecimientos)

## Nombre

Emotion Analyzer

## Descripción

Emotion Analyzer es una aplicación que utiliza técnicas avanzadas de procesamiento de lenguaje natural (NLP) para analizar publicaciones, comentarios y otros textos. La idea es proporcionar una herramienta que pueda ser utilizada en foros, redes sociales y otras plataformas para identificar emociones subyacentes, especialmente la depresión, y su relación con la tasa de empleo y desempleo pre y post pandemia de COVID-19.

### ¿Por qué es importante?

En el mundo digital de hoy, las personas comparten sus pensamientos y sentimientos en línea más que nunca. Emotion Analyzer tiene el potencial de ser una herramienta valiosa para investigadores, políticos y cualquier persona interesada en comprender mejor la relación entre la salud mental y el mercado laboral. Al identificar patrones entre la depresión y la falta de empleo, podemos ofrecer insights valiosos para la creación de políticas públicas y programas de apoyo. ❤️

[![Imagen del Proyecto]()]()

## Arquitectura

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