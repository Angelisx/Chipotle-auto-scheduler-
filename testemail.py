import re

# Updated regular expression
pattern = re.compile(r'\s*(\d{1,2}/\d{1,2}/\d{4}) Shift: (\d{1,2}:\d{2} [APMapm]{2}) - (\d{1,2}:\d{2} [APMapm]{2})')

# Example email
email_content = """
Your schedule for 9/18/2023 - 9/24/2023 is now available. The details of your schedule are the following: Added:
9/18/2023 Shift: 12:00 PM - 4:30 PM
9/20/2023 Shift: 3:45 PM - 11:15 PM
9/21/2023 Shift: 3:30 PM - 11:15 PM
9/23/2023 Shift: 3:00 PM - 7:00 PM
9/24/2023 Shift: 7:00 AM - 11:00 AM
"""

# Find all occurrences using the updated pattern
schedule_data = pattern.findall(email_content)

# Print the results
for date, start_time, end_time in schedule_data:
    print(f'Date: {date}, Start Time: {start_time}, End Time: {end_time}')
