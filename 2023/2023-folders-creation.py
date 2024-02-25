import os
import datetime

# Function to create folders for each week
def create_week_folders(year, directory):
    # Get the first day of the year
    start_date = datetime.date(year, 1, 1)
    week_number = 1
    
    # Loop through each week of the year
    while start_date.year == year:
        # Get the start and end of the week
        week_start = start_date - datetime.timedelta(days=start_date.weekday())
        week_end = week_start + datetime.timedelta(days=6)
        
        # Format the week range
        week_range = f"{week_number}"
        
        # Create the week folder if it doesn't exist
        week_folder = os.path.join(directory, f"Week_{week_range}")
        if not os.path.exists(week_folder):
            os.makedirs(week_folder)
            # Create subfolders for challenges and solutions within the new week folder
            os.makedirs(os.path.join(week_folder, 'challenges'))
            os.makedirs(os.path.join(week_folder, 'solutions'))
        
        # Move to the next week
        start_date = week_end + datetime.timedelta(days=1)
        week_number += 1

# Function to create subfolders for challenges and solutions within existing week folders
def create_subfolders_for_existing_weeks(year, directory):
    # Loop through weeks 1 to 3
    for week_number in range(1, 4):
        # Format the week range
        week_range = f"{week_number}"
        
        # Path to the existing week folder
        week_folder = os.path.join(directory, f"Week_{week_range}")

        # Create subfolders for challenges and solutions if the week folder exists
        if os.path.exists(week_folder):
            os.makedirs(os.path.join(week_folder, 'challenges'), exist_ok=True)
            os.makedirs(os.path.join(week_folder, 'solutions'), exist_ok=True)
        else:
            print(f"Warning: Week {week_number} folder does not exist.")

# Specify the directory where you want to execute the code
directory = "C:/Users/lucky/Downloads/Data Science/TABLEAU/Tableau Prep Challenges/2023"

# Create folders for each week of 2023 in the specified directory
create_week_folders(2023, directory)

# Create subfolders for challenges and solutions within existing week folders
create_subfolders_for_existing_weeks(2023, directory)

print("Folders and subfloders successfully created")
