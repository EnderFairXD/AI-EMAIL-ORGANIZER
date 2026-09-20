import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

load_dotenv()

def process_email(email_data: dict) -> str:
    """Envía los datos del correo a Ollama para su clasificación y análisis."""
    
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # Usamos llama3.1, que ya tienes descargado en CasaOS
    llm = Ollama(
        base_url=base_url,
        model="llama3.1",
        temperature=0.1, # Temperatura baja para que sea conciso y no invente
        num_ctx=4096 
    )
    
    template = """
    Eres un asistente ejecutivo impecable. Analiza el siguiente correo electrónico y responde ESTRICTAMENTE usando este formato Markdown:

    **Clasificación:** [Elige UNA: 🔴 Urgente / 🟡 Trabajo / 🟢 Personal / ⚪ Spam/Boletín]
    **Prioridad:** [Alta / Media / Baja]
    **Resumen:** [Resumen muy breve de 1 o 2 líneas]
    **Respuesta Sugerida:** [Redacta un borrador de respuesta profesional en español listo para enviar, si el correo no requiere respuesta, indica "No requiere respuesta"]

    DATOS DEL CORREO:
    De: {remitente}
    Asunto: {asunto}
    Cuerpo: {cuerpo}
    """
    
    prompt = PromptTemplate(
        input_variables=["remitente", "asunto", "cuerpo"], 
        template=template
    )
    
    chain = prompt | llm
    
    return chain.invoke({
        "remitente": email_data["remitente"],
        "asunto": email_data["asunto"],
        "cuerpo": email_data["cuerpo"]
    })