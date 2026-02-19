# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://abcd.ngrok-free.app/voice/answer",
    to="+16156451400",
    from_="+18444827560"
    method="POST"
    recording=True
    recording_channels="dual",
    recording_status_callback="https://your-ngrok-url.ngrok-free.app/voice/recording-status",
    recording_status_callback_method="POST"
)



print(call.sid)