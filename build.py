from genericpath import isfile
import os
import json
from df import check_folder, install, file_search, version_search
from scrapper import yt_download, yt_version, download
import sys



def initialize():
    home = os.environ['HOME']
    os.chdir(f'{home}/Code/pthon/autoRevanced')
    if os.path.isfile('version.js') == False:
        print("Couldn't find the file version.js")
        sys.exit(0)
    with open('version.json', 'r') as f:
        c_version = json.load(f)
    if check_folder(False,True) == False:
            print("Some of the components are missing\nPlease run '--download-install' install command")
            sys.exit(0)
    cli = version_search(file_search('cli'),c_version['cli'])
    patch = version_search(file_search('patches'),c_version['patches'])
    integration = version_search(file_search('integrations'),c_version['integrations'])
    yt = version_search(file_search('yt'),yt_version())
    if cli == None:
        print('cli missing')
    elif patch == None:
        print('patches missing')
    elif integration == None:
        print('integrations missing')
    elif yt == None:
        print('youtube missing')
    else:
        install(cli,patch,integration,yt,ver=c_version['youtube'])
    print('\n\nTask Complete!!!')
    sys.exit(0)


def update():
    with open('version.json', 'r') as f:
        c_version = json.load(f)
    if os.path.isfile('version.json') == False:
        return False
    elif yt_version() == c_version['youtube']:
        return False
    elif download('cli', cv=True) == c_version['cli']:
        return False
    elif download('integrations', cv=True) == c_version['integrations']:
        return False
    elif download('patches', cv=True) == c_version['patches']:
        return False
    else:
        return True



def build():
    if check_folder(False,True) == False:
        print("Some of the components are missing\nPlease run '--download-install' install command")
        sys.exit(0)
    if os.path.isfile('version.js') == False:
        print("Couldn't find the file version.js")
        sys.exit(0)
    with open('version.json', 'r') as f:
        c_version = json.load(f)
    check_folder(True,True)
    yt_download(yt_version())  # type: ignore
    repo = ['cli', 'patches','integrations']
    for x in repo:
        if download(x,c_version[x]) == None:
            pass
        else:
            c_version[x] = download(x,c_version[x])
    c_version['youtube'] = yt_version()
    with open('../version.json', 'w') as f:
        f.write(json.dumps(c_version))
    initialize()