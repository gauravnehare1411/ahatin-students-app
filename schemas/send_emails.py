import smtplib
from email.mime.text import MIMEText
from config.getenv_var import email_address, email_password

RESET_TOKEN_EXPIRE_MINUTES = 60

async def send_verification_email(to_email: str, code: str):
    subject = "Verify your email"
    body = f"Your verification code is: {code}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = to_email

    smtp_server = "smtp.hostinger.com"
    smtp_port = 465

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email_address, email_password)
            server.send_message(msg)
            print('sent')
    except Exception as e:
        print(f"Email send failed: {e}")