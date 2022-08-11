# email-collector (Gmail)
Locally backing up Gmail labels + messages in each

# Setup
Python39<br />
Env Variable set in Path<br />
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib<br />
Get .json credentials (name crednetials.json)

# Run
python getMessages.py

# Idea
#loop through accounts here and wrap with iteration.<br />
#creating new folders per each account<br />
#creating folders for each label<br />
#listing & getting each email by label<br />
#generating .eml file per each email grabbed<br />
