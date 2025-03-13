import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

# Define the spreadsheet path
SPREADSHEET_PATH = "RTW_commanders_database.xlsx"

def update_spreadsheet():
    try:
        # Load the spreadsheet
        wb = load_workbook(SPREADSHEET_PATH)
        sheet = wb.active  # Get active sheet

        # Example: Update the "Last Updated" column (assuming column Z has this info)
        last_updated_col = "Z"
        last_row = sheet.max_row  # Find last row

        # Insert timestamp in the last column
        sheet[f"{last_updated_col}{last_row}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save the spreadsheet
        wb.save(SPREADSHEET_PATH)
        print("Spreadsheet updated successfully.")

    except Exception as e:
        print(f"Error updating spreadsheet: {e}")

if __name__ == "__main__":
    update_spreadsheet()
