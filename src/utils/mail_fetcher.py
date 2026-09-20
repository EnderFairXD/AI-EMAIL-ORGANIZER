from imap_tools import MailBox, A
import os

def get_recent_emails(limit=5):
    """Se conecta al servidor IMAP y extrae los últimos correos."""
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    imap_server = os.getenv("IMAP_SERVER", "imap.gmail.com")

    emails = []
    try:
        with MailBox(imap_server).login(email_user, email_pass, 'INBOX') as mailbox:
            # Hacemos fetch de los últimos correos, ordenados por fecha (reverse)
            for msg in mailbox.fetch(limit=limit, reverse=True):
                # Limpiamos un poco el texto para no enviar HTML basura a la IA
                body = msg.text if msg.text else "El correo solo contiene HTML o está vacío."
                
                emails.append({
                    "asunto": msg.subject,
                    "remitente": msg.from_,
                    "fecha": msg.date_str,
                    "cuerpo": body[:1500] # Limitamos a 1500 caracteres por correo
                })
    except Exception as e:
        return f"Error de conexión: {str(e)}"
    
    return emails