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

## Overview
The script uses *seleniumwire* version of *webdriver* to iterate through all the urls called by the user provided audiobook page. The url of the playlist containing all the fragments is selected, and then sent to the locally installed VLC player. The player streams the playlist to a local mp3 file.

## Requirements
1. Seleniumwire installed;
2. VLC installed locally.

## Usage
The script can be used either interactively or with command line parameters.

The url of the audiobook is a required parameter. Optionally a file name can be provided as a second parameter, it it's omitted then the last section of the audiobook url will be used as the name of the audiobook mp3.
