# Organizador de Correo IA

Una herramienta desarrollada con Streamlit y LangChain que se conecta a tu bandeja de correo (vía IMAP), descarga los últimos mensajes y utiliza IA local (Llama 3.1 vía Ollama) para clasificarlos, resumirlos y redactar respuestas, garantizando la privacidad de tus datos.

## Requisitos Previos
1. [Python 3.9+](https://www.python.org/)
2. [Ollama](https://ollama.com/) ejecutándose localmente con el modelo Llama 3.1 (`ollama run llama3.1`).
3. Una cuenta de correo con acceso IMAP habilitado (en Gmail, debes crear una "Contraseña de aplicación").

## Instalación
1. Clona el repositorio: `git clone https://github.com/EnderFairXD/AI-EMAIL-ORGANIZER.git`
2. Crea y activa un entorno virtual (`python -m venv .venv`).
3. Instala las dependencias: `pip install -r requirements.txt`
4. Copia `.env.example` a `.env` y rellena tus credenciales reales de correo.
5. Arranca la interfaz: `streamlit run src/main.py`

## Seguridad: prompt injection

Un correo lo escribe cualquiera, así que puede traer instrucciones escondidas para la IA
(*prompt injection indirecta*, OWASP LLM01). Las defensas salen de lo que medí en
[llm-agent-prompt-injection-lab](https://github.com/EnderFairXD/llm-agent-prompt-injection-lab):

- **Sin herramientas (mínimo privilegio)**: la IA solo lee y redacta. No puede enviar, borrar ni
  mover correos, y la respuesta sugerida es un borrador que revisa y manda el usuario. Es la
  defensa que de verdad aguanta.
- **El correo va como dato, aparte de las instrucciones**: las normas viajan en el mensaje de
  sistema y el correo en el de usuario, entre etiquetas con un nombre aleatorio en cada análisis.
  Si el correo intenta cerrar la etiqueta para colar texto fuera, se neutraliza.
- **Avisos al usuario**: la app marca los correos con frases típicas de inyección ("ignora las
  instrucciones", texto dirigido al asistente de IA…) y las respuestas del modelo que se salen
  del formato pedido.

Las dos últimas reducen el riesgo, pero se pueden esquivar: un correo malicioso todavía puede
falsear la clasificación o el resumen. Por eso el análisis es una ayuda, no una decisión.

## Tests

```bash
pip install pytest
pytest
```
