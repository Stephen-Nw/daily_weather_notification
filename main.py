import os
from twilio.rest import Client
from check_weather import daily_temperature

sender = os.environ['SENDER']
recipient = os.environ['RECIPIENT']

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

dt = daily_temperature()

message = client.messages \
                .create(
                     body=f"Good morning, Beautiful."
                          f"\n\n Here is your daily Bartlesville weather forecast:"
                          f"\nCurrent temp: {dt[0]}℉"
                          f"\nFeels like: {dt[1]}℉"
                          f"\nHigh temp: {dt[2]}℉"
                          f"\nLow temp: {dt[3]}℉",
                     from_=sender,
                     to=recipient
                 )

