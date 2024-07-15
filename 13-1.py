from datetime import datetime

# Get the current date as a string
current_date = datetime.now().strftime("%Y-%m-%d")

# Write the current date to the text file today.txt
with open("today.txt", "w") as file:
    file.write(current_date)
    