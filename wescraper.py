from bs4 import BeautifulSoup
import requests, smtplib, shutil, os, glob
import wget
from py3wetransfer import Py3WeTransfer

# WeTransfer API
x = Py3WeTransfer("you-api-key-here")

# Sets webpage to be scraped
r  = requests.get("https://unsplash.com/wallpaper/1065412/iphone-wallpapers")

data = r.text

soup = BeautifulSoup(data)

# creates empty list to be filled with scraped urls
list_of_urls = []

# sets the output directory for downloaded images
output_directory = "C:/Users/Callum/Documents/project_folder"

# sets outgoing email server
conn = smtplib.SMTP('smtp.gmail.com', 587)

# email template with sending and receiving addresses
message = """From: Test Email Address <example@gmail.com>
To: Callum <example@live.co.uk>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP e-mail test

<h2 style="color: #431060">This is a test e-mail message</h2>

"""
# deletes existing files in out directory
def clear_directory():
    filelistjpg=glob.glob("C:/Users/Callum/Documents/project_folder/*.jpg")
    filelistzip=glob.glob("C:/Users/Callum/Documents/project_folder/*.zip")
    for file in filelistjpg:
        os.remove(file)
    for file in filelistzip:
        os.remove(file)

# starts connect without outgoing email server
def email_connection():
    conn.ehlo()
    conn.starttls()
    conn.login('example@gmail.com', 'password')

# finds top download links from webpage and
# puts them in a list
def scrape():
    for link in soup.find_all('a', attrs={'title': 'Download photo'}):
        list_of_urls.append(link.get('href'))
        print(list_of_urls)

# downloads images from urls in list_of_urls then
# clears list contents
def download():
    print("Download started")
    for x in list_of_urls:
        wget.download(x, out=output_directory)
    print("Download complete")
    list_of_urls.clear

# creates .zip file containing downloaded images
def compress_downloads():
    print("Compressing downloads")
    shutil.make_archive("C:/Users/Callum/Desktop/test/downloads", 'zip', root_dir=None, base_dir=None)
    print("Compression complete")

# uploads file to wetransfer then send email
# from template containing wetransfer link
def upload_wetran():
    print("WeTransfer upload started")
    upload_link = x.upload_file("C:/Users/Callum/Documents/project_folder/downloads.zip", "test")
    print("WeTransfer complete")
    conn.sendmail('example@gmail.com', 'example@live.co.uk', message + str(upload_link))
    print(upload_link)
    conn.quit()

clear_directory()
email_connection()
scrape()
download()
compress_downloads()
upload_wetran()
print("Wallpapers downloaded and transferred succesfully")