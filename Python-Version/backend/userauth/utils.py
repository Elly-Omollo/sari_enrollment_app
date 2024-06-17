import requests
from KEMAPP import settings
import random
import string
from django.core.mail import send_mail
from twilio.rest import Client # this is for twilio

# generating random otp

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp





# EMAIL SENDING
def send_otp_mail(email, otp):
    subject = 'Youe OTP for Login'
    message = f'Your otp is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


# sebding via SMS
# choose an sms api/service provider like: (twilio, nexmo, plivo etc....)
# signup for account and obtain necessary credential like (api key, authentication token)

# ie using twilio
# pip install twilio




def send_otp_phone(phone_number, otp):
    accountSID = '' # enter the twilio sid
    auth_token = '' #twilio auth token
    twilio_phone_number = ''

    client = Client(accountSID, auth_token)
    message = client.messages.create(
        body = f'your OTP is {otp}',
        from_ = twilio_phone_number,
        to = phone_number
    )
