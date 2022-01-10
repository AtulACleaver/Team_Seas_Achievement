import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Team Seas just crossed 30 mil 🤯',
                              from_=os.getenv('FROMNUMBER'),
                              to=os.getenv('TONUMBER')
                          )
