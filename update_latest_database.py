import pandas as pd
import subprocess
import os
import time

# File paths
CSV_PATH = "latest_RTW_commanders_database.csv"

def update_csv():
    try:
        # Load the existing CSV
        df = pd.read_csv(CSV_PATH)

        # Extract commander data (this is where image processing would go)
        new_data = {
            "Commander Name": "Galadriel",
            "Tier": "Mythic",
            "Race/Faction": "Elf",
            "Damage Min": 22,
            "Damage Max": 23,
            "Health": 4668,
            "Command": 94,
            "Attack": 21,
            "Defense": 29,
            "Focus": 83,
            "Initiative": 19,
            "Unique Item": "Nenya Ring Of Water",
            "Stat 1": "[Commander] HP +145",
            "Stat 2": "[Commander] Focus +6",
            "Stat 3": "[Commander] Defense +6",
            "Stat 4": "[Unit] Defense +6",
            "Skill 1 Name": "Mistress Of Magic",
            "Skill 1 Type": "Cooldown",
            "Skill 1 Effect Lv1": "Deals 14.0% → 140.0% Focus Damage once to 3 formation(s).",
            "Skill 1 Effect Lv5": "Normal attacks now deal Focus Damage.",
            "Skill 1 Effect Lv10": "In addition, Focus Damage dealt +10.0%. Can stack.",
            "Skill 2 Name": "Lady Of Lorien",
            "Skill 2 Type": "Cooldown",
            "Skill 2 Effect Lv1": "Deals 32.0% → 320.0% Focus Damage once to 2 formation(s), and has a 30.0% chance to inflict Madness on the target for 1 round(s).",
            "Skill 2 Effect Lv5": "Chance for Madness increases to 40.0%.",
            "Skill 2 Effect Lv10": "Chance for Madness increases to 50.0%.",
            "Skill 3 Name": "Scholar Of The Occult",
            "Skill 3 Type": "Passive",
            "Skill 3 Effect Lv1": "Restores 15.0% → 150.0% HP to the Commander's formation unit once each round (effect modified by Focus stat).",
            "Skill 3 Effect Lv5": "Defense of the Commander's formation unit +15.0 for 1 round(s).",
            "Skill 3 Effect Lv10": "Defense of 1 allied formation unit +15.0 for 1 round(s).",
            "Skill 4 Name": "Nenyas Guardian",
            "Skill 4 Type": "Cooldown",
            "Skill 4 Effect Lv1": "Restore 20.0% → 200.0% HP once to 2 allied formation unit(s) (effect modified by Focus stat).",
            "Skill 4 Effect Lv5": "50.0% chance to also remove 1 debuff.",
            "Skill 4 Effect Lv10": "The chance for removing debuffs is increased to 100.0%."
        }

        # Convert new data to DataFrame and append to CSV
        new_row = pd.DataFrame([new_data])
        df = pd.concat([df, new_row], ignore_index=True)

        # Save updated CSV
        df.to_csv(CSV_PATH, index=False)
        print(f"✅ Galadriel successfully added!")

    except Exception as e:
        print(f"❌ ERROR updating CSV: {e}")

def git_push():
    """Commits and pushes updates to GitHub."""
    try:
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])
        subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions Bot"])
        subprocess.run(["git", "add", CSV_PATH])
        subprocess.run(["git", "commit", "-m", "Auto-update: Added Galadriel"])
        subprocess.run(["git", "push", "origin", "main"])
    except Exception as e:
        print(f"❌ ERROR pushing to GitHub: {e}")

if __name__ == "__main__":
    update_csv()
    git_push()

