

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as dt
from datetime import timedelta
import time
from time import sleep
from datetime import date
from extract import extract 

sendingdate=0
dict_date={}
result1=extract()

for key,value in result1.items():
        mail_content = "This is a reminder mail for your class on "+ value +"at" + key +" Please join the class on time."
        date1=dt.strptime(key.rstrip(), '%Y %d %b %I:%M %p')
        dayname=date1.strftime('%A')
        
        if dayname=="Monday":
            sendingdate=date1 - timedelta(days=3)
        else:
            sendingdate=date1 - timedelta(days=1)
        sendingdate1=sendingdate.date()
    
        dict_date[sendingdate1]=mail_content
        #print(dict_date)
for key1,value in dict_date.items():
        current_date=date.today()
        
        if current_date==key1:
            sender_address='your email'
            sender_pass='App Password'
            #sender_pass =sys.argv[2]
            receiver_addresses = ['yogithamudoor@gmail.com','rehan@onelearn.io']
            mailidslen=len(receiver_addresses)
            for i in range(mailidslen):
               x=receiver_addresses[i]
               receiver_address=x
            #Setup the MIME
               message = MIMEMultipart() 
               message['From'] = sender_address
               message['To'] = receiver_address
               message['Subject'] = 'OneLearn course series reminder.'   #The subject line
               #The body and the attachments for the mail
               message.attach(MIMEText(value, 'plain'))
               #Create SMTP session for sending the mail
               session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
               session.starttls() #enable security
               session.login(sender_address, sender_pass) #login with mail_id and password
               text=message.as_string()
               session.sendmail(sender_address, receiver_address, text)
               print('Mail Sent From TaskBar')
               session.quit()    
        else:
            pass
            
       
        