# email-collector (Gmail)
Locally backing up Gmail labels + messages in each

# Setup
Python39<br />
Env Variable set in Path<br />
pip3 install simplegmail<br />
pip install beautifulsoup4<br />
Get .json credentials (name client_secret.json)

# Run
python getMessages.py

# Idea
loop through accounts here and wrap with iteration.<br />
creating new folders per each account<br />
creating folders for each label<br />
listing & getting each email by label<br />
generating .eml file per each email grabbed<br />
