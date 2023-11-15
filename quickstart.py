from simplegmail import Gmail
from simplegmail.query import construct_query
from datetime import datetime
import os.path
import re
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

gmail = Gmail()
processed_dates = set()
# calendarId='1d3014ce0c421b0ba9eb3ae682e681daaf522a492bc89ce09c7b54c8a583880d@group.calendar.google.com'

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_CHIP_messages():
    # For even more control, use queries:
    query_params = {
        "labels": [["CHIP"]]
    }

    messages = gmail.get_messages(query=construct_query(query_params))

    for message in messages:
        process_email(message)
        # print(message.plahin)

def process_email(email):
    body = email.html  


    # Extract schedule data using regular expressions
    pattern =re.compile(r'\s*(\d{1,2}/\d{1,2}/\d{4}) Shift: (\d{1,2}:\d{2} [APMapm]{2}) - (\d{1,2}:\d{2} [APMapm]{2})')
   

    schedule_data = pattern.findall(body)
    for date, start_time, end_time in schedule_data:
        # print(f'Date: {date}, Start Time: {start_time}, End Time: {end_time}')
        if date not in processed_dates:
            processed_dates.add(date)
            # print(f'Date: {date}, Start Time: {start_time}, End Time: {end_time}')

            
            d = datetime.strptime(date, "%m/%d/%Y")
            formatted_date = d.strftime("%Y-%m-%d")

            nt = datetime.strptime(start_time, "%I:%M %p")
            formatted_start_time = nt.strftime("%H:%M")

            et = datetime.strptime(end_time, "%I:%M %p")
            formatted_end_time = et.strftime("%H:%M")
            
            
            add_event_to_calendar(formatted_date,formatted_start_time, formatted_end_time)


        

def add_event_to_calendar(formatted_date,formatted_start_time,formatted_end_time):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        summary = 'Chipotle Schedule'
        location = '6135 Junction Blvd., Queens, NY 11374'

        # Format date, start_time, and end_time into a valid format for Google Calendar
        start_datetime = f'{formatted_date}T{formatted_start_time}:00-05:00'
        end_datetime = f'{formatted_date}T{formatted_end_time}:00-05:00'


        # Check if the event already exists in the calendar
        events_result = service.events().list(
            calendarId='f6ab48a7569f8fd42cc20a93dee4b689fd2182c091c7f1476e0ad2c8f00684a9@group.calendar.google.com',
            timeMin=start_datetime,
            timeMax=end_datetime,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

        if not events:
            # Event does not exist, so add it to the calendar
            event = {
                'summary': summary,
                'location': location,
                'description': 'Chipotle Schedule',
                'start': {
                    'dateTime': start_datetime,
                    'timeZone': 'America/New_York',
                },
                'end': {
                    'dateTime': end_datetime,
                    'timeZone': 'America/New_York',
                },
            }

            event = service.events().insert(calendarId='f6ab48a7569f8fd42cc20a93dee4b689fd2182c091c7f1476e0ad2c8f00684a9@group.calendar.google.com', body=event).execute()
            
            print(f"DATE:{formatted_date}  START TIME:{start_datetime} END TIME:{end_datetime} ")

            print('Event added successfully')
        else:
            print('Event already exists')

    except HttpError as error:
        print(f"An error occurred: {error}")

# Call the function to process CHIP messages
get_CHIP_messages()

