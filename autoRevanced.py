#! /usr/bin/python3.10

import os
import sys
from scrapper import download, yt_version
import argparse
from build import build, initialize, update
from df import check_folder, c_version, options


parser = argparse.ArgumentParser(
     prog="AutoRevanced",
     description="A simple automation tool for downloading and installing latest revanced patches for youtube"
)
parser.add_argument('-dt', '--dark-theme',nargs='?', action='store',type=str, default='@android:color/black', help='set custom dark theme for youtube app')
parser.add_argument('-lt', '--light-theme',nargs='?', action='store',type=str, default='@android:color/white', help='set custom light theme for youtube app')
parser.add_argument('-cy', '--check-youtube',dest='cy', action='store_true', help='checks the latest revanced supported youtube version')
parser.add_argument('-cc', '--check-cli', action='store_true', help='checks the latest revanced cli version')
parser.add_argument('-ci', '--check-integrations', action='store_true', help='checks the latest revanced integrations version')
parser.add_argument('-cp', '--check-patches', action='store_true', help='checks the latest revanced patches version')
parser.add_argument('-cl', '--check-all', dest='cl', action='store_true', help='list all the components latest version')
parser.add_argument('-di', '--download-install', dest='di', action='store_true', help='Download & Install Latest YouTube Revanced')
parser.add_argument('-i', '--install', action='store_true', help='Install YouTube Revanced Only')
args = parser.parse_args()


def space(x):
    z = 11 - len(x)
    return ' '*z


s_yt = space(yt_version())
s_cli = space(download('cli', cv=True))
s_integrations = space(download('integrations', cv=True))
s_patch = space(download('patches', cv=True))
heading = f"[Name]  |  [Latest version]  |  [Current version]"
check_youtube = f"Revanced YouTube        --> {yt_version()}{s_yt}   -->   {c_version['youtube']}"
check_cli = f"Revanced CLI            --> {download('cli',cv=True)}{s_cli}   -->   {c_version['cli']}"
check_integrations = f"Revanced Integrations   --> {download('integrations',cv=True)}{s_integrations}   -->   {c_version['integrations']}"
check_patches = f"Revanced Patches        --> {download('patches',cv=True)}{s_patch}   -->   {c_version['patches']}"
try:
    if args.cy:
        print(f"{heading}\n\n{check_youtube}")
    elif args.check_cli:
        print(f"{heading}\n\n{check_cli}")
    elif args.check_integrations:
        print(f"{heading}\n\n{check_integrations}")
    elif args.check_patches:
        print(f"{heading}\n\n{check_patches}")
    elif args.cl:
        list_version = f"{heading}\n\n{check_youtube}\n{check_cli}\n{check_integrations}\n{check_patches}"
        print(list_version)
    elif args.di:
        check_folder(True,True)
        if update() == True:
            print('You have latest YouTube Revanced')
        else:
            print("Your have old version\nDo you want to download & install latest resources?[y/n]")
            decide = input('>>')
            if 'y' in decide.lower():
                options(args.dark_theme,args.light_theme)
                build()
            else:
                sys.exit(0)
    elif args.install:
        options(args.dark_theme,args.light_theme)
        initialize()

except KeyboardInterrupt:
    print("Operation Cancelled...")