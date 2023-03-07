import requests
import smtplib

# Global variables

GMAIL = 'smtp.gmail.com'
EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
recipient_email = 'RECIPIENT EMAIL'
TITLE = 'Your Weather Update!'
body = 'Today\'s weather description: '
umbrella_result = ''

endpoint = f'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'oklahoma city,ok,us',
    'appid': "APP ID"
}

# API call

data = requests.get(endpoint, params=params).json()['weather'][0]

# ID below 700 means snow or rain

if int(data['id']) < 700:
    umbrella_result = 'Bring an umbrella!'
else:
    umbrella_result = 'No need for an umbrella!'

# Add the final result to the message

body = body + f'{data["main"]}\n{umbrella_result}'

# Finalize the message

message = f'Subject: {TITLE}\n\n{body}'

# Send the message

with smtplib.SMTP(GMAIL) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=recipient_email,
                        msg=message)
