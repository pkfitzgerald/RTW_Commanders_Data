import pandas as pd
import os

CSV_PATH = "latest_RTW_commanders_database.csv"

def test_editability():
    """Check if the file is writable."""
    try:
        if not os.access(CSV_PATH, os.W_OK):
            print("❌ ERROR: GitHub Actions does NOT have write access to the CSV file!")
            return False
        else:
            print("✅ SUCCESS: GitHub Actions CAN write to the CSV file.")
            return True
    except Exception as e:
        print(f"❌ ERROR checking file permissions: {e}")
        return False

def update_csv():
    """Test update: Log and modify CSV."""
    if not test_editability():
        return  # Stop if file is not editable

    try:
        # **Load the CSV**
        df = pd.read_csv(CSV_PATH)

        # **Log a sample of existing data**
        print("🔍 Existing Data Sample:")
        print(df.head())

        # **Test: Add a dummy column (or update a value)**
        df["Last_Updated_By"] = "GitHub_Actions_Bot"

        # **Save the updated CSV**
        df.to_csv(CSV_PATH, index=False)
        print("✅ CSV successfully updated.")

    except Exception as e:
        print(f"❌ ERROR updating CSV: {e}")

if __name__ == "__main__":
    update_csv()
