import pandas as pd
import subprocess

CSV_PATH = "latest_RTW_commanders_database.csv"

# King of the Dead's data
kotd_data = {
    "Commander Name": "King of the Dead",
    "Race/Faction": "Undead",
    "Tier": "Mythic",
    "Damage Min": 20,
    "Damage Max": 22,
    "Attack": 41,
    "Focus": 33,
    "Speed": 49,
    "Command": 166,
    "Defense": 44,
    "HP": 4756,
    "Unique Item": "Crown Of The Dead",
    "Unique Item Effect": "[Commander] Command +30, [Commander] Focus +5. On Round 1, deals 1200.0% Focus Damage once to 1 enemy formation(s), and inflicts Madness on the target for 1 round.",
    "Weapon": "None",
    "Chest Armor": "None",
    "Helmet": "None",
    "Accessory": "None",
    "Set Effect": "None",
    "Troop Bonus": "None",
    "Skill 1 Name": "Incorporeal",
    "Skill 1 Type": "Focus Damage",
    "Skill 1 Effect Lv1": "Deals 60.0% → 600.0% Focus Damage once to 1 enemy formation(s).",
    "Skill 1 Effect Lv5": "35.0% chance to inflict Stun on the target for 1 round(s).",
    "Skill 1 Effect Lv10": "Chance to Stun increases to 50.0%.",
    "Skill 1 Cooldown": "2 Rounds",
    "Skill 2 Name": "Betrayer",
    "Skill 2 Type": "Passive Buff",
    "Skill 2 Effect Lv1": "Damage dealt by 2 allied formation unit(s) +1.0% → 10.0% (effect modified by Command stat), but they succumb to heal block.",
    "Skill 2 Effect Lv5": "[Unit] Attack (Undead) +3.0.",
    "Skill 2 Effect Lv10": "[Unit] Defense +5.0.",
    "Skill 3 Name": "Men Of The Mountains",
    "Skill 3 Type": "Passive Buff",
    "Skill 3 Effect Lv1": "Each round, 2 formation(s) on both sides have 9.0% → 90.0% chance to deal minimum damage.",
    "Skill 3 Effect Lv5": "Affects 3 enemy and allied formations.",
    "Skill 3 Effect Lv10": "[Commander] Focus +5.0.",
    "Skill 4 Name": "Army Of The Dead",
    "Skill 4 Type": "Healing",
    "Skill 4 Effect Lv1": "Restores 31.0% → 310.0% HP to Small Units in the Commander’s formation (effect modified by Focus stat). Unaffected by heal block.",
    "Skill 4 Effect Lv5": "[Unit] HP +10.0%.",
    "Skill 4 Effect Lv10": "Grants 1 additional instance of healing to 1 Undead unit formation(s)."
}

def update_csv():
    """Check for King of the Dead and update the database."""
    try:
        # Load CSV and ensure correct column names
        df = pd.read_csv(CSV_PATH)

        # Ensure 'Commander Name' exists
        if "Commander Name" not in df.columns:
            print("❌ ERROR: 'Commander Name' column not found. Check the CSV format.")
            print("🔍 Current Columns:", df.columns.tolist())
            return  # Stop execution

        # Check if King of the Dead exists
        if "King of the Dead" in df["Commander Name"].values:
            print("✅ King of the Dead is already in the database.")
            return  # No update needed

        # Add new row
        df = df.append(kotd_data, ignore_index=True)

        # Save updated CSV
        df.to_csv(CSV_PATH, index=False)
        print("✅ King of the Dead successfully added!")

    except Exception as e:
        print(f"❌ ERROR updating CSV: {e}")

def git_push():
    """Stage, commit, and push changes to GitHub."""
    subprocess.run(["git", "add", CSV_PATH])

    # Check if there are actual changes
    status_output = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    
    if not status_output.stdout.strip():
        print("No new changes detected. Skipping push.")
        return  # Exit if no new data was added

    # Commit and push
    subprocess.run(["git", "commit", "-m", "Added King of the Dead to latest_RTW_commanders_database"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    update_csv()  # Add King of the Dead
    git_push()  # Push updates
