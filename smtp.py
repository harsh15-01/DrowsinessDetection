import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
#from email.utils import COMMASPACE
from email import encoders

# Define email credentials and settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USERNAME = '2005084@kiit.ac.in'
SMTP_PASSWORD = 'kiit@1234'
EMAIL_FROM = '205084@kiit.ac.in'
EMAIL_TO = 'itsthechamp0074@gmail.com'
EMAIL_SUBJECT = 'Facial recognition screenshot'

# Load the screenshot image using OpenCV
screenshot_path = 'Screenshot.png'
img = cv2.imread(screenshot_path)

# Encode the image to bytes and create the email attachment
attachment = MIMEBase('application', "octet-stream")
attachment.set_payload(cv2.imencode('.png', img)[1].tostring())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment', filename='screenshot.png')

# Create the email message
msg = MIMEMultipart()
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO
msg['Subject'] = 'facial recognition screenshot for security issues'
msg.attach(MIMEText('Facial recognition screenshot is attached.'))
msg.attach(attachment)

# Connect to the SMTP server and send the email
smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp_server.starttls()
smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
smtp_server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
smtp_server.quit()