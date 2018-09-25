__author__ = 'DELL'
import smtplib
sender = "mandimus@gmail.com"
receiver =["mandimus@gmail.com"]
message =" From: From person <mandimus@gmail.com> " \
         "To: To person <mandimus@gmail.com>" \
         "Subject : SMTP email test" \
         "This is a test email message "
try:
    s= smtplib.SMTP('smtp.gmail.com',578)
    s.starttls()
    s.login(sender,'motu1234')
    s.sendmail(sender,receiver,message)
    print("Sent Email")
    s.quit()
except Exception as e:
    print("Error while sending", e)