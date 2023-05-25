from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'pwrobel2010@gmail.com'
email_password = 'mcjyyhixtlfnfljk'
email_reciver = 'gidola9771@cutefier.com'

subject = "Twój tyul"
body = "Witam jest to test"
em = EmailMessage()
em['from'] = email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)SS

context = ssl.create_default_context()
 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context ) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string() )
