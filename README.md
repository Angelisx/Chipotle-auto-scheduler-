# Project README

## Introduction

This project utilizes the `simplegmail` library and the Google Calendar API to process email messages and add events to a Google Calendar based on the contents of the emails.

## Code Overview

The script performs the following tasks:

1. **Authentication**: It authenticates the user with the Google Calendar API using OAuth 2.0.
2. **Calendar Retrieval**: It retrieves a list of calendars associated with the user's Google account.
3. **User Interface**: It presents a user interface to select a calendar from the retrieved list.
4. **Email Processing**: It processes email messages fetched from Gmail using the `simplegmail` library.
5. **Schedule Data Extraction**: It extracts schedule data from the email body using regular expressions.
6. **Event Creation**: It creates events in the selected Google Calendar based on the extracted schedule data.
7. **Error Handling**: It handles errors such as expired credentials or HTTP errors gracefully.

The code is organized into functions and follows a modular approach for better readability and maintainability. Comments are provided throughout the code to explain key functionalities and logic. The script utilizes exception handling to deal with potential errors during the authentication process and API calls.

The script can be extended or modified to suit specific use cases by customizing the email processing logic, adding additional error handling, or integrating with other Google APIs for enhanced functionality.

## Prerequisites

Before running the code, ensure you have the following prerequisites installed:

- Python 3.x
- Pip (Python package manager)

## Installation

###1. Clone the repository to your local machine:

###2.Navigate to the project directory:
      cd <project_directory>
###3.Install the required Python packages using pip and the provided requirements.txt file:

pip install -r requirements.txt
