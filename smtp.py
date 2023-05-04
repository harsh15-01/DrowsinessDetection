import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


def mailing(recipient_email):
    


# Define email sender and recipient
    sender_email = 'arnavsha94.jpr@gmail.com'
    sender_name = 'Arnav'
    

# Create message object
    msg = MIMEMultipart()
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = recipient_email
    msg['Subject'] = 'Unknown Person Boarding'

# Add message body
    message = ''' Dear Sir,
    
    Some Unknown Person Boarded your car, please check the attachment to see his face!!

Thanking You
Yours faithfully
Team Suvery Corps'''
    msg.attach(MIMEText(message, 'plain'))

# Add attachment
    # attachment_file_path = 'C://Users//gupta//OneDrive//Desktop//Email Script//out//'+roll+'.png'
    attachment_file_path = 'screenshot.jpeg'
    attachment_file_name = os.path.basename(attachment_file_path)
    with open(attachment_file_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('content-disposition', 'attachment', filename=attachment_file_name)
        msg.attach(attachment)

# Set up SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = '2105701@kiit.ac.in'
    smtp_password = 'zcdrstbclvyclufc'

# Create SMTP connection and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)

    print('Email sent successfully with attachment.')

# mailing('itsthechamp0074@gmail.com')