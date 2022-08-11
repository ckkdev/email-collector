#Email-collector
Locally backing up Gmail labels + messages in each

#Setup
Python39
Env Variable set in Path
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
Get .json credentials (name crednetials.json)

#Run
python getMessages.py

#Idea
# loop through accounts here and wrap with iteration below line 64.
# creating new folders per each account
# creating folders for each label
# listing & getting each email by label
# generating .eml file per each email grabbed
