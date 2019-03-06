# A work in progress python web scraper.

## This web scraper goes to a specified page on Unsplash and find the download links for individual photos. It then stores the links in a list, iterates over them and downloads the image file at end of each url.

## It then uploads the files to WeTransfer via their API and inserts the WeTransfer download link into a preset email template.

## The script then sends this email with the download link to a predetermined recipient.

### Planned updates, alterations and improvements:

-Further styling the email template

-Adding environmental variables to allow for a more typical looking python script
as commonly appears on github

-Having the output directory for the scraped files auto-clearing once the script is succesfully run
in order to prevent duplication of files and to stop accumulation of previously downloaded files

-General refactoring and restructuring of the code to more resemble a typical python file

-Scheduling the script to run at a set interval (i.e. once per week)

-Adding a requirements.txt file for easier install of required libraries

-Flask integration, making the script callable from a webpage

-As part this script's functionality within this webpage, using a dropdown list
of options to select which category of Unsplash wallpapers to download