
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
 
# create message object instance
msg = MIMEMultipart()



destiny = input("Enter the destination email: "+"\n")
subject = input("Enter the subject: "+"\n")
message_text = input("Enter the message: "+"\n")


# setup the parameters of the message
message = message_text
password = "xxx"
msg['From'] = "xxx@xxx"
msg['To'] = destiny
msg['Subject'] = subject
 

try:
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))

	#create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
	 
	#identify as an encrypted connection
	server.ehlo()

	#Adding tls encryptation
	server.starttls()

	#re-identify as an encrypted connection
	server.ehlo()
	 
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
 
	try:
		# send the message via the server.
		server.sendmail(msg['From'], msg['To'], msg.as_string())	
		print ("successfully sent email to %s:" % (msg['To']))	 
	finally:	       
		server.quit()
except:
	sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
