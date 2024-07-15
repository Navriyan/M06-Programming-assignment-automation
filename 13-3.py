from datetime import datetime

# Assuming today_string contains the date string from the file
today_string = "2024-07-12"  # Example content

# Parse the date from today_string
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print(parsed_date)