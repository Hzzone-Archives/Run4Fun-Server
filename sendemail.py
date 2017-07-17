import smtplib
from email.mime.text import MIMEText

def sendEmail(email_title, email_text, target_address):
	_user = "1141408077@qq.com"
	_pwd  = "emxrefjwdjprigcg"
	_to   = target_address

	msg = MIMEText(email_text)
	msg["Subject"] = email_title
	msg["From"]    = _user
	msg["To"]      = _to

	try:
		s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		s.login(_user, _pwd)
		s.sendmail(_user, _to, msg.as_string())
		s.quit()
		print("Send email success!")
	except smtplib.SMTPException:
		print("Send email falied")

# if __name__ == "__main__":
# 	sendEmail("hahahah", '100')