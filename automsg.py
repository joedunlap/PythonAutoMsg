from email.mime.image import MIMEImage
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

import schedule

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = os.getenv('EMAIL_ADDRESS')
email_password = 'awoi vkkp dyhm zjwv'

print(f"EMAIL_ADDRESS: {email_address}")
print(f"EMAIL_PASSWORD: {email_password}")

# List of recipient email addresses
recipient_emails = ['joedunlap26@gmail.com', 'jamie.valenza@gmail.com']

def send_email():
    print("Preparing to send email...")
    subject = 'Daily Reminder'
    body = 'Me love you:)'

    # Create the email headers and message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = ", ".join(recipient_emails)
    msg['Subject'] = subject

      # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Path to the image file
    image_path = './img/koalas.png'

    # Read and attach the image
    try:
        with open(image_path, 'rb') as img:
            img_data = img.read()
            image = MIMEImage(img_data, name=os.path.basename(image_path))
            msg.attach(image)
    except Exception as e:
        print(f"Failed to attach image: {e}")


    # Connect to the server and send the email
    try:
        print(f"Connecting to SMTP server: {smtp_server}:{smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("Logging into email server...")
        server.login(email_address, email_password)
        text = msg.as_string()
        print(f"Sending email to: {', '.join(recipient_emails)}")
        server.sendmail(email_address, recipient_emails, text)
        server.quit()
        print(f"Email sent to {', '.join(recipient_emails)}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent every day at 8:00 AM
schedule.every().day.at("08:05").do(send_email)

print("Scheduler started...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)