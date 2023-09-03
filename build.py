import os
import json
from df import c_version, check_folder,version_search,file_search, install, versionFilePath
from scrapper import yt_download, yt_version, download
import sys



def initialize():
    if check_folder(False,True) == False:
        print("Some of the components are missing\nPlease run '--download-install' install command")
        sys.exit(0)
    if os.path.isfile(versionFilePath) == False:
        print("Couldn't find the file version.js")
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
    if os.path.isfile(versionFilePath) == False:
        return False
    else:
        with open(versionFilePath, 'r') as f:
            c_version = json.load(f)
    if os.path.isdir('revanced') == False:
        return False
    elif yt_version() != c_version['youtube'] or version_search(file_search('yt'),yt_version()) == None:
        return False
    elif download('cli', cv=True) != c_version['cli'] or version_search(file_search('cli'),yt_version()) == None:
        return False
    elif download('integrations', cv=True) != c_version['integrations'] or version_search(file_search('integrations'),yt_version()) == None:
        return False
    elif download('patches', cv=True) != c_version['patches'] or version_search(file_search('patches'),yt_version()) == None:
        return False
    else:
        return True



def build():
    if os.path.isfile(versionFilePath) == False:
        with open(versionFilePath, 'w') as f:
            temp_version = {
                'youtube': yt_version(),
                'cli': download('cli',cv=True),
                'patches': download('patches',cv=True),
                'integrations': download('integrations',cv=True)
            }
            f.write(json.dumps(temp_version))
        with open(versionFilePath, 'r') as f:
            with open(versionFilePath, 'r') as f:
                c_version = json.load(f)    
    else:
        with open(versionFilePath, 'r') as f:
            c_version = json.load(f)
    yt_download(yt_version())  # type: ignore
    repo = ['cli', 'patches','integrations']
    for x in repo:
        if download(x,c_version[x]) == None:
            pass
        else:
            c_version[x] = download(x,c_version[x])
    c_version['youtube'] = yt_version()
    with open(versionFilePath, 'w') as f:
        f.write(json.dumps(c_version))
    initialize()