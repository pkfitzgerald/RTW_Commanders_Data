import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

# Paths to files
SPREADSHEET_PATH = "RTW_commanders_database.xlsx"
CSV_PATH = "latest_RTW_commanders_database.csv"

def update_spreadsheet():
    try:
        # Load the spreadsheet
        wb = load_workbook(SPREADSHEET_PATH)
        sheet = wb.active

        # Update "Last Updated" column (assuming column Z contains timestamps)
        last_updated_col = "Z"
        last_row = sheet.max_row
        sheet[f"{last_updated_col}{last_row}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save the spreadsheet
        wb.save(SPREADSHEET_PATH)
        print("Spreadsheet updated successfully.")

        # Convert spreadsheet to CSV
        df = pd.read_excel(SPREADSHEET_PATH, sheet_name=0)
        df.to_csv(CSV_PATH, index=False)
        print("CSV file generated successfully.")

    except Exception as e:
        print(f"Error updating spreadsheet: {e}")

if __name__ == "__main__":
    update_spreadsheet()
