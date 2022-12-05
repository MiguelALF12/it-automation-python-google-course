from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

# ---- Defining an email-like message
message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = "Hey dude whats up!"
message.set_content(body)

# ---- Attaching a File
attachment_path = "car_sales.json"
attachment_filename = os.path.basename(attachment_path)

# we guess here the MIME type of the file
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
with open(attachment_path, 'rb') as ap:  # Important to always use rb
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

port = 2500
mail_server = smtplib.SMTP('localhost', port)
# mail_server.login(sender, 'password')
mail_server.send_message(message)
mail_server.quit()
