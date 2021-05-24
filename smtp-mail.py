#Autor: Federico Joaquín Coronati
#Matricula: 40502859

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.text import MIMEText

#Dirección de email del destinatario 
receiver_email = "dbritos@gmail.com" #"feedehc@gmail.com"

#Se usa remitente de Hotmail porque con Google Drive no es posible ocultar el remitente, a menos que se desactiven las opciones de seguridad de la cuenta,
#Lo cual no es recomendable para la cuenta que usamos en el día a día

#Outlook
smtp_server = 'smtp.office365.com'  
port = 587
sender_email = 'federico.coronati@hotmail.com'
password = input(str("Ingrese su contraseña del correo remitente: ")) #Por seguridad la contraseña se solicita en todos los envios

#Google Gmail
#smtp_server = 'smtp.gmail.com'    
#port = 465

#El mensaje se escribe en formato HTML, con ayuda de la libreria email y mimemultipart
message = MIMEMultipart("mixed")
message["Subject"] = "SMTP Coronati"
message["From"] = formataddr(('Anonymous', sender_email))
message["To"] = receiver_email

text_msg = str("Este es un mensaje de prueba de protocolo SMTP con remitente desconocido")
plaintext_part = MIMEText(text_msg, 'plain')
message.attach(plaintext_part)

with smtplib.SMTP(host=smtp_server, port=port) as server: 
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    print("Login exitoso")    
    server.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message.as_string()) #Se envia el correo
    print("Mensaje enviado correctamente desde: " + sender_email + " hacia: " + receiver_email)
    server.quit()
