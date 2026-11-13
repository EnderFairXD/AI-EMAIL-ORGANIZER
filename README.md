# Organizador de Correo IA

> **Este proyecto continúa en [suite-ia-local](https://github.com/EnderFairXD/suite-ia-local)**, que junta las cinco herramientas de IA local (contratos, documentación, correo, reuniones y estudio) con código común, tests y soporte para textos largos. Este repositorio queda archivado como referencia.

Una herramienta desarrollada con Streamlit y LangChain que se conecta a tu bandeja de correo (vía IMAP), descarga los últimos mensajes y utiliza IA local (Llama 3.1 vía Ollama) para clasificarlos, resumirlos y redactar respuestas, garantizando la privacidad de tus datos.

## Requisitos Previos
1. [Python 3.9+](https://www.python.org/)
2. [Ollama](https://ollama.com/) ejecutándose localmente con el modelo Llama 3.1 (`ollama run llama3.1`).
3. Una cuenta de correo con acceso IMAP habilitado (en Gmail, debes crear una "Contraseña de aplicación").

## Instalación
1. Clona el repositorio.
2. Crea y activa un entorno virtual (`python -m venv .venv`).
3. Instala las dependencias: `pip install -r requirements.txt`
4. Copia `.env.example` a `.env` y rellena tus credenciales reales de correo.
5. Arranca la interfaz: `streamlit run src/main.py`