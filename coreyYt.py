import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")

print(f"API Key: {api_key}")


youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.channels().list(part="statistics", forUsername="jiejenn")
# request = youtube.channels().list(part="statistics", forUsername="schafer5")

response = request.execute()

print(response)
