import smtplib
import getpass # takes password input in an invisible and safer way

smtp_object = smtplib.SMTP('smtp.gmail.com',587) 
smtp_object.ehlo() 
# this ehlo function greets the server; we used 587 , it means we used tls encryption 
# so we have to initialize the server with starttls function. İf we were to used 465
# that would means that the mail is not encrypted and we dont need to use starttls function

smtp_object.starttls()

# with getpass library we take the informations in an invisible way
sender_mail = getpass.getpass("please enter your email: ")
receiver_mail = getpass.getpass("please enter receiver's mail")
password = getpass.getpass("please enter your password ") 
# we cannot use our gmail password here, we have take a password called app password
# this password will be able to used for a few hours

smtp_object.login(sender_mail, password) # with .login function we use the informations we took above and we are logining up to our mail account

subject = input("enter subject line")
message = input("enter message line")
msg = "Subject: "+subject+'\n+message'

smtp_object.sendmail(sender_mail , receiver_mail, msg)
