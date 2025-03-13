import pandas as pd
from openpyxl import load_workbook
import subprocess
import time
import os

# File paths
SPREADSHEET_PATH = "RTW_commanders_database.xlsx"
CSV_PATH = "latest_RTW_commanders_database.csv"

def update_spreadsheet():
    try:
        # Load existing spreadsheet
        wb = load_workbook(SPREADSHEET_PATH)
        sheet = wb.active  # Work on the main sheet

        # Load CSV data
        df = pd.read_csv(CSV_PATH)

        # Clear sheet (except headers)
        for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
            for cell in row:
                cell.value = None

        # Write new data from CSV
        for r_idx, row in enumerate(df.itertuples(index=False), start=2):  # Start from row 2
            for c_idx, value in enumerate(row, start=1):
                sheet.cell(row=r_idx, column=c_idx, value=value)

        # **Force an update** by modifying a cell that changes every run
        sheet["Z1"] = f"Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}"

        # Save changes
        wb.save(SPREADSHEET_PATH)

        print("Spreadsheet successfully updated.")

    except Exception as e:
        print(f"Error updating spreadsheet: {e}")

def pull_latest():
    """Pull the latest changes to prevent conflicts."""
    subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])
    subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions Bot"])
    subprocess.run(["git", "pull", "--rebase", "origin", "main"])  # Ensure repo is up-to-date

def push_changes():
    """Push the updated spreadsheet back to GitHub."""
    subprocess.run(["git", "add", SPREADSHEET_PATH, CSV_PATH])

    # **Check if there are changes**
    status_output = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status_output.stdout.strip():
        print("No changes detected. Skipping push.")
        return  # **Exit if no changes**

    # Commit and push changes
    subprocess.run(["git", "commit", "-m", "Auto-updated commander database and CSV"])
    subprocess.run(["git", "push", "origin", "main"])  # Push changes

if __name__ == "__main__":
    pull_latest()
    update_spreadsheet()
    push_changes()

