#! /usr/bin/python3.10

import os
import sys
from scrapper import download, yt_version
import argparse
from build import build, initialize, update
from df import check_folder, c_version, options
import concurrent.futures

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
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)


def space(x):
    z = 11 - len(x)
    return ' '*z



def displayVersion(check:str='', individual:bool=True):
    heading = f"{' '*4}[Name]{' '*10}|  [Latest version]  |  [Current version]"
    if individual == False:
        with concurrent.futures.ThreadPoolExecutor() as run:
            youtubeVersion = run.submit(yt_version).result()
            cliVersion = run.submit(download,'cli', '',True).result()
            intgVersion = run.submit(download,'integrations', '',True).result()
            patchVersion = run.submit(download,'patches', '',True).result()
            s_yt = run.submit(space,youtubeVersion).result()
            s_cli = run.submit(space,cliVersion).result()
            s_int = run.submit(space,intgVersion).result()
            s_patch = run.submit(space,patchVersion).result()
        check_integrations = f"Revanced Integrations   --> {intgVersion}{s_int}   -->   {c_version['integrations']}"
        check_patches = f"Revanced Patches        --> {patchVersion}{s_patch}   -->   {c_version['patches']}"
        check_youtube = f"Revanced YouTube        --> {youtubeVersion}{s_yt}   -->   {c_version['youtube']}"
        check_cli = f"Revanced CLI            --> {cliVersion}{s_cli}   -->   {c_version['cli']}"
        print(f"{heading}\n\n{check_youtube}\n{check_cli}\n{check_integrations}\n{check_patches}")
    else:
        if check == 'youtube':
            s_yt = space(yt_version())
            check_youtube = f"Revanced YouTube        --> {yt_version()}{s_yt}   -->   {c_version['youtube']}"
            print(f"{heading}\n\n{check_youtube}")
        elif check == 'cli':
            s_cli = space(download('cli', cv=True))
            check_cli = f"Revanced CLI            --> {download('cli',cv=True)}{s_cli}   -->   {c_version['cli']}"
            print(f"{heading}\n\n{check_cli}")
        elif check == 'integrations':
            s_int = space(download('integrations', cv=True))
            check_integrations = f"Revanced Integrations   --> {download('integrations',cv=True)}{s_int}   -->   {c_version['integrations']}"
            print(f"{heading}\n\n{check_integrations}")
        elif check == 'patches':
            s_patch = space(download('patches', cv=True))
            check_patches = f"Revanced Patches        --> {download('patches',cv=True)}{s_patch}   -->   {c_version['patches']}"
            print(f"{heading}\n\n{check_patches}")
        else:
            print(None)



try:
    if args.cy:
        displayVersion('youtube')
    elif args.check_cli:
        displayVersion('cli')
    elif args.check_integrations:
        displayVersion('integrations')
    elif args.check_patches:
        displayVersion('patches')
    elif args.cl:
        displayVersion(individual=False)
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