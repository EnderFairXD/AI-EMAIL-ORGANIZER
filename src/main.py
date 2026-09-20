import streamlit as st
from dotenv import load_dotenv
from utils.mail_fetcher import get_recent_emails
from services.ai_agent import process_email

load_dotenv()

st.set_page_config(page_title="Inbox AI", page_icon="📨", layout="wide")

st.title("📨 Organizador de Correo con IA")
st.markdown("Clasifica, resume y redacta respuestas usando **Llama 3.1** desde tu servidor local.")

# Controles en la barra lateral
st.sidebar.header("⚙️ Configuración")
num_emails = st.sidebar.slider("Correos a procesar", 1, 10, 3)

if st.sidebar.button("📥 Descargar y Analizar Bandeja"):
    
    with st.spinner(f"Conectando al servidor IMAP y descargando {num_emails} correos..."):
        emails = get_recent_emails(limit=num_emails)
        
    if isinstance(emails, str): # Si devolvió un error de conexión
        st.error(emails)
    else:
        st.success(f"¡Se descargaron {len(emails)} correos con éxito!")
        
        # Procesar cada correo con la IA
        for i, email in enumerate(emails):
            with st.expander(f"✉️ {email['remitente']} - {email['asunto']}", expanded=(i==0)):
                
                col1, col2 = st.columns([1, 1])
                
                # Columna Izquierda: Correo Original
                with col1:
                    st.markdown("### 📄 Correo Original")
                    st.caption(f"**Fecha:** {email['fecha']}")
                    st.text_area("Cuerpo del mensaje", email['cuerpo'], height=200, disabled=True, key=f"cuerpo_{i}")
                
                # Columna Derecha: Análisis de la IA
                with col2:
                    st.markdown("### 🤖 Análisis IA")
                    with st.spinner("Analizando con Ollama en CasaOS..."):
                        try:
                            analisis = process_email(email)
                            st.markdown(analisis)
                        except Exception as e:
                            st.error(f"Error de conexión con Ollama: {str(e)}")