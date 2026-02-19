# Download the helper library from https://www.twilio.com/docs/python/install
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://shaniqua-zodiacal-shannon.ngrok-free.dev/voice/answer",
    to="+18054398008",
    from_="+18444827560",
    method="POST",
    record=True,
    recording_channels="dual",
    recording_status_callback="https://shaniqua-zodiacal-shannon.ngrok-free.dev/voice/recording-status",
    recording_status_callback_method="POST"
)



print(call.sid)