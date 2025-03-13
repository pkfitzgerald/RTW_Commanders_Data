import gspread
import pandas as pd
import datetime
import os
from google.oauth2.service_account import Credentials
import subprocess

# --- Configuration ---
GITHUB_REPO = "https://github.com/pkfitzgerald/RTW_Commanders_Data.git"
GITHUB_BRANCH = "main"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Uses the GitHub secret
GITHUB_USER = "github-actions[bot]"

# --- Google Sheets Configuration ---
SHEET_ID = "YOUR_GOOGLE_SHEET_ID"
SHEET_NAME = "Sheet1"  # Update if different
SERVICE_ACCOUNT_FILE = "google-credentials.json"

# --- Authenticate Google Sheets ---
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# --- Fetch Data ---
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
data = sheet.get_all_records()
df = pd.DataFrame(data)

# --- Generate Timestamped Filename ---
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"RTW_commanders_database_{timestamp}.csv"
df.to_csv(filename, index=False)

print(f"✅ Google Sheets synced successfully! Saved as {filename}")

# --- GitHub Push ---
subprocess.run(["git", "config", "--global", "user.name", GITHUB_USER])
subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])
subprocess.run(["git", "add", filename])
subprocess.run(["git", "commit", "-m", f"Auto-sync Google Sheets: {timestamp}"])
subprocess.run(["git", "push", GITHUB_REPO, GITHUB_BRANCH])
