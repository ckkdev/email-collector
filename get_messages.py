# importing os & os path & pathLib module
import os
import os.path
from pathlib import Path

#importing base64
import base64

#simpleGmail
from simplegmail import Gmail
from simplegmail.query import construct_query
gmail = Gmail()

#importing time
import time

#importing beautiful soup
from bs4 import BeautifulSoup

# importing email module
import email
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Parent Directory path
parent_dir = str(Path(os.getcwd())) + '\EMAILS'

def main():

    gmail = Gmail()

    labels = gmail.list_labels()

    if not labels:
        print('No labels found.')
        return

    for label in labels:

        directory = label.name
        path = os.path.join(parent_dir, directory)

        try: 
            os.makedirs(path) 
            print("Directory '% s' created" % path)
        except OSError as error: 
            print(error)

        query_params = {
            "labels":[[directory]]
        }

        messages = gmail.get_messages(query=construct_query(query_params))

        for message in messages:

            msg = MIMEMultipart('alternative')
            msg.set_charset("utf-8")
            index = 1
            headers = message.headers
            for header in headers:
                msg[header] = headers[header]
                index += 1

            if message.html is not None:
                body_content = MIMEText(message.html, 'html')

            elif message.plain is not None:
                body_content = MIMEText(message.plain, 'plain')

            else:
                continue
        
            msg.attach(body_content)
            outfile_name = os.path.join(parent_dir, directory, message.id+".eml")
            print("Duplicated email " + message.id + " into folder " + label.name)
            with open(outfile_name, 'w') as outfile:
                gen = generator.Generator(outfile)
                gen.flatten(msg)

if __name__ == '__main__':
    main()