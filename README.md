# email-collector (Gmail)
Locally backing up Gmail labels + messages in each

# Setup
Python39<br />
pip3 install simplegmail<br />
Download .json credentials from Google Console Credentials (rename to client_secret.json)

# Run
python getMessages.py

# Purpose
Create folders for each label in a Gmail account.<br />
Create .eml copies of each message in each newly created folder.

#ToDos
Find a better way to not cap out on quota limit.
