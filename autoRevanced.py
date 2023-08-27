#! /usr/bin/python3.10

import os
import sys
from scrapper import download, yt_version
import argparse
import json
from build import build, initialize, update
from df import check_folder

home = os.environ['HOME']
os.chdir(f'{home}/Code/pthon/autoRevanced')
if os.path.isfile('version.js') == False:
    c_version = {
        'youtube': '',
        'cli': '',
        'integrations': '',
        'patches': ''
    }
else:
    with open('version.json', 'r') as f:
        c_version = json.load(f)
parser = argparse.ArgumentParser(
     prog="AutoRevanced",
     description="A simple automation tool for downloading and installing latest revanced patches for youtube"
)
parser.add_argument('-cy', '--check-youtube',dest='cy', action='store_true', help='checks the latest revanced supported youtube version')
parser.add_argument('-cl', '--check-all', dest='cl', action='store_true', help='list all the components latest version')
parser.add_argument('-di', '--download-install', dest='di', action='store_true', help='Download & Install Latest YouTube Revanced')
parser.add_argument('-i', '--install', action='store_true', help='Install YouTube Revanced Only')
args = parser.parse_args()

try:
    if args.cy:
        print(f"<*> Latest YouTube Revanced Version: {yt_version()}")
    elif args.cl:
        list_version = f"""
    <*> Latest: [Name] [latest version] | [current version]\n
            Revanced YouTube        --> {yt_version()}   |   {c_version['youtube']}
            Revanced CLI            --> {download('cli',cv=True)}    |   {c_version['cli']}
            Revanced Integrations   --> {download('integrations',cv=True)}   |   {c_version['integrations']}
            Revanced Patches        --> {download('patches',cv=True)}   |   {c_version['patches']}
    """
        print(list_version)
    elif args.di:
        check_folder(True,True)
        if update() == False:
            print('You have latest YouTube Revanced')
        else:
            print("Your have old version\nDo you want to download & install latest resources?[y/n]")
            decide = input('>>')
            if 'y' in decide.lower():
                build()
            else:
                sys.exit(0)
    elif args.install:
        initialize()

except KeyboardInterrupt:
    print("Operation Cancelled...")