from bs4 import BeautifulSoup
import requests
import wget
import smtplib
import os
import time
from py3wetransfer import Py3WeTransfer

# deletes any existing files in output directory
path = "c:/Users/Callum/Documents/project_folder"
for filename in os.listdir(path):
    if filename.endswith(''):
        # os.unlink(filename)
        print(filename)

# connect to sending email server
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('example@gmail.com', 'password')

# WeTransfer API
x = Py3WeTransfer("api-key")

# Sets webpage to be scraped
r  = requests.get("https://unsplash.com/wallpaper/1065412/iphone-wallpapers")

data = r.text

soup = BeautifulSoup(data)

# creates empty list to be filled with scraped urls
list_of_urls = []

file1 = []

output_directory = "C:/Users/Callum/Documents/project_folder"

for link in soup.find_all('a', attrs={'title': 'Download photo'}):
    list_of_urls.append(link.get('href'))

print(list_of_urls)

for x in list_of_urls:
        wget.download(x, out=output_directory)

# clears list contents
list_of_urls.clear

# sets output directory for google drive
drive_link = "googledrive.com"

# defines function to send delayed email with link to output directory on google drive.
# function has delay in order to allow suffcient time for file upload
def email_wait():
        print("waiting")
        time.sleep(15)
        conn.sendmail('example@gmail.com', 'example@live.co.uk', 'Subject: New Unplash iPhone wallpapers ' + str(drive_link))
        print("email sent")


# email template with sending and receiving addresses
message = """From: Test Email Address <tempdata590@gmail.com>
To: Callum <example@live.co.uk>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP e-mail test

<b>This is a test e-mail message<b>.
"""

# defines function to upload file to wetransfer then send email
# from template containing wetransfer link
def upload_wetran():
        print("wetransfer function called")
        # upload_link = x.upload_file(file1, "test")
        upload_link = x.upload_file("C:/Users/Callum/Desktop/test/andrew-pons-57133-unsplash.jpg", "test")
        print("wetransfer complete")
        time.sleep(5)
        conn.sendmail('example@gmail.com', 'example@live.co.uk', message + ("\n") + str(upload_link))
        print(upload_link)

# calls functions in order
upload_wetran()
# email_wait()
conn.quit()
file1.clear