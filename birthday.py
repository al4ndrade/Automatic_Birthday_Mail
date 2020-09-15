import sqlite3
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_birthdaymail(name, lastName, to_addr):
	msg = MIMEMultipart()
	from_addr = 'alfakemail@fakemail.com'
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = 'Feliz Cumple ' + name + ' ' + lastName

	html_body = f'''
	<html>
		<head></head>
		<body>
		<h1>¡Feliz Cumple {name}!</h1>
		<p>Solo unas pocas palabras para desearte un feliz cumpleaños.</p>
		<img src=https://media.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif>
		<p>
		Disfruta tu día.
		</p>
		</body>
	</html>
	'''

	msg.attach(MIMEText(html_body, 'html'))

	smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.login(from_addr, 'flatkvelpeajsmskw')

	text = msg.as_string()
	smtp_server.sendmail(from_addr, to_addr, text)
	smtp_server.quit()
	print(f'Felicidades {name}, mail enviado')


conn = sqlite3.connect('birthdays.db')
cur = conn.cursor()
cur.execute("SELECT * FROM clientes")
rows = cur.fetchall()

hoy = date.today()
hoy_md = (hoy.month, hoy.day)

for row in rows:
	birthday = row[3]
	birthdate = date.fromisoformat(birthday)
	birth_month_and_day = (birthdate.month, birthdate.day)
	if birth_month_and_day == hoy_md:
		name, lastName, email = row[0], row[1], row[2]
		send_birthdaymail(name, lastName, email)
















