# pip install pyshorteners
# pip install pyperclip

import pyshorteners

link = input('Please enter the url here: ')


def shortenurl(link):
    p = pyshorteners.Shortener()
    print(p.tinyurl.short(link))

shortenurl(link)