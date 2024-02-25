import os
from datetime import datetime

def create_weekly_folders():
    current_week = datetime.now().isocalendar()[1]

    for week_number in range(1, current_week + 1):
        week_folder = f"Week_{week_number}"
        if not os.path.exists(week_folder):
            os.makedirs(week_folder)
            print(f"Folder '{week_folder}' created successfully.")
        else:
            print(f"Folder '{week_folder}' already exists.")

        challenges_folder = os.path.join(week_folder, "Challenges")
        solutions_folder = os.path.join(week_folder, "Solutions")

        if not os.path.exists(challenges_folder):
            os.makedirs(challenges_folder)
            print(f"Challenges folder created inside '{week_folder}'.")
        else:
            print(f"Challenges folder inside '{week_folder}' already exists.")

        if not os.path.exists(solutions_folder):
            os.makedirs(solutions_folder)
            print(f"Solutions folder created inside '{week_folder}'.")
        else:
            print(f"Solutions folder inside '{week_folder}' already exists.")

if __name__ == "__main__":
    create_weekly_folders()
