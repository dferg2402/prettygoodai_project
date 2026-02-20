#download recording files and add extensions
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def download(recording_sid: str, output_path: str):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    
    if not account_sid or not auth_token:
        raise RuntimeError("Missing TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN. Check your .env.")
    
    if not account_sid.startswith("AC"):
        raise RuntimeError(f"TWILIO_ACCOUNT_SID looks wrong: {account_sid}")

    client = Client(account_sid, auth_token)
    
    recordings = client.recordings(recording_sid).fetch()
    
    base_url = "https://api.twilio.com" + recordings.uri.replace(".json", ".mp3")
    #fallback to wav if mp3 fails
    
    for ext in ["mp3", "wav"]:
        r = requests.get(base_url, auth=(account_sid, auth_token), timeout=60)
        if r.status_code == 200:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(r.content)
            print(f"Downloaded from: {base_url}")
            print(f"Saved to: {output_path}")
            return
        else:
            print("Tried", base_url, "but got status", r.status_code)
    
    r.raise_for_status()
    
        
if __name__ == "__main__":
    
    download("RE07c9a6108bbf7a4fdf8f2e6a3c42b86a",
        "artifacts/calls/CAe3a9b91a5766f0b12214046c933dea61/call.mp3")
     

