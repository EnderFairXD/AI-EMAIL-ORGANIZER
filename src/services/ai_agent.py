import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from services.seguridad import (
    construir_mensajes,
    nuevo_delimitador,
    senales_de_inyeccion,
    validar_analisis,
)

load_dotenv()


def process_email(email_data: dict) -> dict:
    """Analiza un correo con Ollama tratándolo como contenido no confiable.

    Devuelve el análisis del modelo, las señales de prompt injection encontradas en
    el correo y los problemas de formato de la respuesta, para avisar al usuario.
    """
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    llm = ChatOllama(
        base_url=base_url,
        model="llama3.1",
        temperature=0.1,  # Temperatura baja para que sea conciso y no invente
        num_ctx=4096,
    )

    sistema, usuario = construir_mensajes(email_data, nuevo_delimitador())
    respuesta = llm.invoke([SystemMessage(content=sistema), HumanMessage(content=usuario)])
    analisis = respuesta.content

    return {
        "analisis": analisis,
        "senales": senales_de_inyeccion(email_data),
        "problemas": validar_analisis(analisis),
    }
