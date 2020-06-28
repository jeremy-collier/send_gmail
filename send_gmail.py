import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email = input("Email: ")
password = getpass.getpass('Password: ')
smtp_object.login(email, password)

from_address = email
to_address = input("Send Email To: ")
subject = input("Enter subject: ")
message = input('Enter Your Message: ')
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()
