import pandas as pd
from openpyxl import load_workbook

# Path to your spreadsheet
SPREADSHEET_PATH = "RTW_commanders_database.xlsx"

def update_spreadsheet():
    try:
        # Load the existing spreadsheet
        wb = load_workbook(SPREADSHEET_PATH)
        sheet = wb.active  # Use the active sheet

        # Example: Update a specific cell (modify as needed)
        sheet["A1"] = "Updated by GitHub Actions"

        # Save the updated spreadsheet
        wb.save(SPREADSHEET_PATH)
        print("Spreadsheet updated successfully.")

    except Exception as e:
        print(f"Error updating spreadsheet: {e}")

if __name__ == "__main__":
    update_spreadsheet()
