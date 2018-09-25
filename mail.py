__author__ = 'DELL'
import smtplib
s= smtplib.SMTP('smtp.gmail.com',587)
sender= 'gargi.vyas@gmail.com'
s.starttls()
s.login('senderemailid','password')
receiver="<receiver addr>"
message = "Type your msg here"
s.sendmail(sender,receiver,message)
s.quit()
