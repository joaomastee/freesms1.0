# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC1d39a1e3d92c6e5b6abc82dad3096cd1"
auth_token = "40f341e7dd033575135ca94d69ee6e26"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hey, I can send Free SMS using Python. Eu estou indo. ASS: João Ivo Lopes",
  from_="+13133514189",
  to="+5579981359918",
)

print(message.sid)