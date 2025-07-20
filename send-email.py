import smtplib
from email.message import EmailMessage

sender_email = "sudhakarojha19@gmail.com"
receiver_email = "nectarsharma108@gmail.com"
app_password = "-------------"	#passward 16-digit

subject = "Test Email from Python"
body = "Hi there,\nThis is a test email sent from Python! "

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        print(" Email sent successfully!")
except Exception as e:
    print(" Failed to send email:", e)
