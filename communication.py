import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import yagmail
from twilio.rest import Client


load_dotenv()

sender_mail = os.getenv('SENDER_MAIL')
sender_password = os.getenv('MAIL_PASS')
receiver_mail = os.getenv('RECEIVER_MAIL')
twilio_sid = os.getenv('TWILIO_SID')
twilio_token = os.getenv('TWILIO_TOKEN')
sender_phone = os.getenv('TWILIO_PHONE')
receiver_phone = os.getenv('RECEIVER_PHONE')
smtp_domain = os.getenv('SMTP_DOMAIN')


def message_percentage(paper_name: str, target: float,
                       change: float, status='decrease or rise'):

    subject = f"Update! {paper_name} has shown {status} in it's value!"
    body = f"{paper_name} has shown {status} of {change}% in it's value. "\
        + f"Target change was: {target}%"

    return subject, body


def message_rate(paper_name: str, target: int,
                 change: int, status='below or above'):

    subject = f"Update! {paper_name} has shown change in it's rate value!"
    body = f"{paper_name}'s current rate is: {change}. "\
        + f"Target rate was {status} {target} points."

    return subject, body


def send_gmail(subject: str, body: str):
    with yagmail.SMTP(user=sender_mail, password=sender_password) as yag:
        try:
            yag.send(receiver_mail, subject, body)
        except:
            print("Couldn't send Mail using yagmail.")


def send_mail(subject: str, body: str):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_mail
    msg['To'] = receiver_mail

    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_domain, 465) as smtp:
        try:
            smtp.login(sender_mail, sender_password)
            smtp.send_message(msg)
        except:
            print("Couldn't send Mail using smtplib.")


def send_sms(message: str):
    client = Client(twilio_sid, twilio_token)
    try:
        client.messages.create(body=message,
                               from_=sender_phone,
                               to=receiver_phone)
    except:
        print("Couldn't send SMS using Twilio's API.")


def send_whatsapp(message: str):
    client = Client(twilio_sid, twilio_token)
    try:
        client.messages.create(body=message,
                               from_='whatsapp:' + sender_phone,
                               to='whatsapp:' + receiver_phone)
    except:
        print("Couldn't send WhatsApp using Twilio's API.")