#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    # ---- Attaching a File
    if attachment_path != "":
        attachment_filename = os.path.basename(attachment_path)

        # we guess here the MIME type of the file
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:  # Important to always use rb
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=os.path.basename(attachment_path))
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
