import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Define Google Sheets & GitHub Sync
SPREADSHEET_NAME = "RTW_commanders_database"
WORKSHEET_NAME = "Sheet1"

# Load credentials
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "rtw-commanders-data-key.json"  # Replace with your actual JSON key filename

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Open Google Sheet
spreadsheet = client.open(SPREADSHEET_NAME)
worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

# Read the data into Pandas DataFrame
data = worksheet.get_all_values()
df = pd.DataFrame(data)

# Save to GitHub
df.to_csv("RTW_commanders_database.csv", index=False)
print("Google Sheets synced successfully!")
