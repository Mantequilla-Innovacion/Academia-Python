# Chatbot con FastAPI y Firebase Auth

Este es un mini proyecto de un chatbot desarrollado con **FastAPI** que incluye un sistema de autenticación utilizando **Firebase**.

## Características

- API desarrollada con FastAPI
- Autenticación de usuarios mediante Firebase Authentication
- Chatbot con respuestas automáticas
- Estructura modular y fácil de escalar

## Requisitos

- Python (3.13.1 recomendado)
- Cuenta en Firebase con un proyecto habilitado
- Entorno virtual (recomendado)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Mantequilla-Innovacion/Academia-Python.git
cd Academia-Python
```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Añade credenciales para inicializacion de firestore `friebaseconsole->settings->serviceaccounts->adminsdk`.

5. Configura tus variables de entorno en un archivo `.env`:

## Uso

1. Ejecuta el servidor:

```bash
uvicorn main:app --reload
```

2. Accede a la documentación interactiva de la API en:

```
http://127.0.0.1:8000/docs
