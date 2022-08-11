# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# loop through accounts here and wrap with iteration below line 64.
# creating new folders per each account
# creating folders for each label
# listing & getting each email by label
# generating .eml file per each email grabbed

# [START gmail_quickstart]
from __future__ import print_function

# importing os & os path module
import os
import os.path

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
parent_dir = "C:/Users/14694/Desktop/gm/"


def main():

    gmail = Gmail()

    labels = gmail.list_labels()

    if not labels:
        print('No labels found.')
        return
    print('Labels:')
    for label in labels:
        # Directory
        directory = label.name
        # Path
        path = os.path.join(parent_dir, directory)
        try: 
            os.makedirs(path) 
            print("Directory '% s' created" % path)
        except OSError as error: 
            print(error)

        # # For even more control use queries:
        # # Messages that are: newer than 2 days old, unread, labeled "Finance" or both "Homework" and "CS"
        query_params = {
            "labels":[[directory]]
        }

        messages = gmail.get_messages(query=construct_query(query_params))
        print(len(messages))


        # for message in messages:
            
        #     payload = nEmail['payload']
        #     headers = payload['headers']
                
        #     if not payload.get('parts'): continue
        #     parts = payload.get('parts')[1]['body'] if payload.get('parts')[1]['body'] else payload.get('parts')[0]['body']
        #     if 'data' in parts.keys():
        #         data = parts['data']
        #         data = data.replace("-","+").replace("_","/")
        #         decoded_data = base64.b64decode(data)
    
        #         soup = BeautifulSoup(decoded_data , "lxml")
        #         body = soup.body()
        #         msg = MIMEMultipart('alternative')
        #         msg.set_charset("utf-8")


        #         index = 0
        #         while index < len(headers):
        #             msg[headers[index]['name']] = headers[index]['value']
        #             index += 1
        #             body_content = '';
        #             for body_part in body:
        #                 body_content = body_content + str(body_part)

        #         body_content = MIMEText(body_content, 'html')
        #         msg.attach(body_content)
        #         outfile_name = os.path.join(parent_dir, directory, nEmail['id']+".eml")
        #         print("Email " + nEmail['id'] + " added into folder " + label['name'])
        #         with open(outfile_name, 'w') as outfile:
        #             gen = generator.Generator(outfile)
        #             gen.flatten(msg)

if __name__ == '__main__':
    main()
# [END gmail_quickstart]
