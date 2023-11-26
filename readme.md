A script to download audiobooks from akniga.com and store as local mp3s.

# Disclaimer

The script provided as is. Feel free to modify as it suits your needs.

# Overview

Akniga.com site provides a variety of audiobooks, mostly in Russian. Some books are available for download for free, some a present only as fragments of the whole works, that you can purchase on the site. The scripts help to automate downloading of __only free audiobooks__.

The script uses *seleniumwire* version of *webdriver* to iterate through all the urls called by the page. The url of the playlist containing all the fragments is selected, and then sent to the local

# Requirements

1. Seleniumwire installsed
2. VLC installed locally