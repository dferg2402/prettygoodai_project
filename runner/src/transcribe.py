from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv(dotenv_path=".env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CALL_SID = "CAe3a9b91a5766f0b12214046c933dea61"
BASE_PATH = f"artifacts/calls/{CALL_SID}"
AUDIO_PATH = f"{BASE_PATH}/call.mp3"

TXT_PATH = f"{BASE_PATH}/transcript.txt"
JSON_PATH = f"{BASE_PATH}/transcript.json"
MD_PATH = f"{BASE_PATH}/transcript.md"

#Transcribe the audio file using the OpenAI API
with open(AUDIO_PATH, "rb") as f:
    transcript = client.audio.transcriptions.create( 
        model="gpt-4o-mini-transcribe", 
        file = f)
    
#Save to text file
text = transcript.text
with open(TXT_PATH, "w", encoding="utf-8") as out:
    out.write(text)
    
#Save to json file
json_data = {
    "call_sid": CALL_SID,
    "audio_file": AUDIO_PATH,
    "transcript": text
}
  
with open(JSON_PATH, "w", encoding="utf-8") as out:
    json.dump(json_data, out, indent=2) 
    
#Save to markdown file
with open(MD_PATH, "w", encoding="utf-8") as out:
    out.write(f'#Call Transcript - {CALL_SID}\n\n')
    out.write("## Raw Transcription\n\n")
    out.write(f"> {text}\n")

print("Saved transcript files:")
print("-", TXT_PATH)
print("-", JSON_PATH)
print("-", MD_PATH)
print("\nTranscript Preview:\n")
print(text)