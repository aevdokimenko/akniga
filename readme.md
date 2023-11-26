# Akniga Audiobook Downloader

## Table of Contents
- [Introduction](#introduction)
- [Disclaimer](#disclaimer)
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction
Akniga.com offers a wide range of audiobooks, predominantly in Russian. This includes both freely downloadable books and fragments of larger works available for purchase. This script is designed to automate the downloading process for the **free audiobooks only**.


## Disclaimer
The script is provided as is. Feel free to modify as it suits your needs.

The script is tested on MacOS only, you may need to adjust it to run on other systems.

## Overview
The script uses *seleniumwire* version of *webdriver* to iterate through all the urls called by the user provided audiobook page. The url of the playlist containing all the fragments is selected, and then sent to the locally installed VLC player. The player streams the playlist to a local mp3 file.

## Requirements
1. Seleniumwire
2. VLC player

## Usage
The script can be used either interactively or with command line parameters.

The url of the audiobook is required, can be provided as the first parameter, if missing then the script will prompt for it. If the url is not matching the common pattern for the akniga urls, the script will exit.

Optionally a file name can be provided as a second parameter, if it's omitted then the last section of the audiobook url will be used as the name of the output audiobook mp3 file.

## Future dev
It would be nice to show progress of the conversion. The current solution is to bring up the VLC GUI, which expands it from the pure CLI. It's possible to hide the GUI by uncommenting "-I dummy" parameters of the VLC call, but then there's no progress updates and it may be confusing for a user. The downloads though are faster than the actual play time by factor ~20-40.