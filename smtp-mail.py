#Autor: Federico Joaquín Coronati
#Matricula: 40502859

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# Correo del destinatario 
mail_receptor = "feedehc@gmail.com" #"dbritos@gmail.com"

# Credenciales para conexión SMTP:

""" Para google """
# smtp_server = 'smtp.gmail.com'    
# port = 465
# sender = ''   # Direccion y contraseña del correo Gmail del remitente
# password = ''

""" Para outlook """
smtp_server = 'smtp.office365.com'  
port = 587
sender = '' # Direccion y contraseña del correo Hotmail/Outlook del remitente
password = ''

# Se construye el mensaje en formato HTML y texto, por si falla el formateo a HTML se envie el de texto
message = MIMEMultipart("alternative")
message["Subject"] = "SMTP Coronati Federico"
message["From"] = formataddr(('Nadie', sender))
message["To"] = mail_receptor

# Creo el mensaje, lo que va despues de la barra invertida es el asunto
text = """
"""

""" Para google. GOOGLE NO OCULTA EL CORREO DEL REMITENTE (FROM:) """
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(host=smtp_server, port=port, context=context) as server:
#     print(server.login(sender, password))
#     print(server.helo())
#     # Enviamos el correo:
#     server.sendmail(from_addr=sender, to_addrs=mail_receptor, msg=text)
#     print(server.quit())

""" Para outlok """ 
with smtplib.SMTP(host=smtp_server, port=port) as server: 
    print(server.ehlo())
    print(server.starttls())
    print(server.login(sender, password))
    # Enviamos el correo:
    server.sendmail(from_addr=sender, to_addrs=mail_receptor, msg=message.as_string())
    print(server.quit())
