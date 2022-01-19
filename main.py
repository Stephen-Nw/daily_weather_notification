import os
from twilio.rest import Client
from check_weather import daily_temperature

sender = os.environ['SENDER']
recipient = os.environ['RECIPIENT']

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

dt = daily_temperature()
print(dt)
print(dt[0])

# return current_temperature, feels_like, max_temperature, min_temperature

message = client.messages \
                .create(
                     body=f"Good morning, Beautiful. Here is your daily weather forecast:"
                          f"\nCurrent temp: {dt[0]}℉"
                          f"\nFeels like: {dt[1]}℉"
                          f"\nMax temp: {dt[2]}℉"
                          f"\nMin temp: {dt[3]}℉",
                     from_=sender,
                     to=recipient
                 )

