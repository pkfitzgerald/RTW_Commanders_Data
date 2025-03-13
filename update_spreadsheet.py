import subprocess
import pandas as pd
from openpyxl import load_workbook
import time

# Path to your spreadsheet
SPREADSHEET_PATH = "RTW_commanders_database.xlsx"

def update_spreadsheet():
    try:
        # Load the existing spreadsheet
        wb = load_workbook(SPREADSHEET_PATH)
        sheet = wb.active  # Use the active sheet

        # Example: Update timestamp to force a change
        sheet["Z1"] = f"Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}"

        # Save the updated spreadsheet
        wb.save(SPREADSHEET_PATH)
        print("Spreadsheet updated successfully.")

    except Exception as e:
        print(f"Error updating spreadsheet: {e}")

def pull_latest():
    """Pull the latest changes before pushing."""
    subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])
    subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions Bot"])
    subprocess.run(["git", "pull", "--rebase", "origin", "main"])  # Ensure up-to-date repo

def push_changes():
    """Push the updated spreadsheet back to GitHub."""
    subprocess.run(["git", "add", "RTW_commanders_database.xlsx", "latest_RTW_commanders_database.csv"])
    subprocess.run(["git", "commit", "-m", "Auto-updated commander database and CSV"])
    subprocess.run(["git", "push", "origin", "main"])  # Push changes

if __name__ == "__main__":
    pull_latest()
    update_spreadsheet()
    push_changes()
