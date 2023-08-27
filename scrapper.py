from urllib.request import urlopen, Request
import os
from bs4 import BeautifulSoup
import json
from df import version_search, file_search

def yt_download(ver:str):
    if version_search(file_search('yt'),ver) == True:
        return None
    mod_ver = ver.replace('.','-')
    link = f"https://www.apkmirror.com/apk/google-inc/youtube/youtube-{mod_ver}-release/youtube-{mod_ver}-3-android-apk-download/"
    headers = {'User-Agent':'Mozilla/4.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.114 Mobile Safari/537.36'}
    req = Request(url=link,data=None,headers=headers)
    print(f"{'#'*23}\n['YouTube APK {ver.replace('-','.')}]\n{'#'*24}")
    print("\n\nSending request apk client site...")
    f = urlopen(req)
    print('\nSuccess\n\nCollecting the Download Link')
    html_text = f.read()
    soup = BeautifulSoup(html_text, 'html.parser')
    be_soup = soup.find("a", class_=["accent_bg", "btn", "btn-flat", "downloadButton", "WZn"])
    get_download_page = f"https://www.apkmirror.com{be_soup['href']}"  # type: ignore
    req_main = Request(url=get_download_page,data=None,headers=headers)
    main_index = urlopen(req_main).read()
    final_soup = BeautifulSoup(main_index,'html.parser')
    get_download_link = final_soup.find("a",{'rel':'nofollow'})
    download_link = f"https://www.apkmirror.com{get_download_link['href']}" # type: ignore
    print('\nSucessfully Collected Download Link\n\nStarted Downloading...')
    os.system(f'wget --user-agent="Mozilla" -c -q --show-progress -O yt_{ver}.apk "{download_link}"')
    print('Successfully Download YouTube APK')

 
def download(repo:str, ver:str='',cv=False):
    if repo == 'integrations':
        ext = 'apk'
    else:
        ext = 'jar'
    if repo == 'cli':
        extra = '-all'
    else:
        extra = ''
    link = f"https://github.com/ReVanced/revanced-{repo}/releases/latest"
    redirect_link = urlopen(link).geturl()
    d_version = redirect_link.split('/')[-1]
    if cv == True:
        return d_version
    if d_version == ver and version_search(file_search(repo),ver) == True:
        return None
    else:
        print(f"{'#'*24}\n[Revanced {repo.capitalize()}'{ver}]\n{'#'*24}")
        download_link = f"{link.replace('latest','download/')}{d_version}/revanced-{repo}-{d_version.replace('v','')}{extra}.{ext}"
        print(download_link)
        print(f"\nStarted Downloading {repo}.{ext}")
        os.system(f'wget --user-agent="Mozilla" -c -q --show-progress -O "revanced-{repo}-{d_version}{extra}.{ext}" "{download_link}"')
        print(f'\n\nFinished Downloading file revanced-{repo}_{d_version}{extra}.{ext}')
        return d_version



def yt_version():
    package_ver = "https://raw.githubusercontent.com/ReVanced/revanced-patches/main/patches.json"
    parse_package_ver = urlopen(package_ver).read()
    convert_package_ver = json.loads(parse_package_ver)
    for x in convert_package_ver:
        if x['name'] == 'Video ads':
            data = x['compatiblePackages'][0]
            latest_verison = data['versions'][-1]
            return latest_verison

