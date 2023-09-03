import re
import os
import json

home = os.environ['HOME']
downloadPath = f'{home}/Downloads'
revancedPath = f'{downloadPath}/revanced'
versionPath = f'{home}/.config/autoRevanced'
versionFilePath = f'{versionPath}/version.json'
if os.path.isfile(versionFilePath) == True:
    with open(versionFilePath, 'r') as f:
        c_version = json.loads(f.read())
else:
    c_version = {
        'youtube': '',
        'cli': '',
        'integrations': '',
        'patches': ''
    }

def check_folder(create=False,chdir=False):
    if os.path.isdir(versionPath) == False and create == True:
        os.mkdir(versionPath)
    if os.path.isdir(revancedPath) == False:
        if create == True:
            os.mkdir(revancedPath)
        if chdir==True:
            os.chdir(revancedPath)
        return False
    else:
        if chdir == True:
            os.chdir(revancedPath)
        return True


def file_search(lwd):
    os.chdir(revancedPath)
    # lwd = cli, integrations, patches, yt
    cli_list = []
    int_list = []
    patch_list = []
    patch_list = []
    yt_list = []
    cli_pattern = re.compile(r'.*cli.*\.jar')
    int_pattern = re.compile(r'.*integrations.*\.apk')
    patch_pattern = re.compile(r'.*patches.*\.jar')
    yt_pattern = re.compile(r'.*(com.google.android.youtube|yt|youtube).*\.apk')
    if lwd == 'cli':
        for x in os.listdir():
            match_cli = cli_pattern.match(x)
            if match_cli:
                cli_list.append(x)
            else:
                pass
        return cli_list
    elif lwd == 'integrations':
        for x in os.listdir():
            match_int = int_pattern.match(x)
            if match_int:
                int_list.append(x)
            else:
                pass
        return int_list
    elif lwd == 'patches':
        for x in os.listdir():
            match_patch = patch_pattern.match(x)
            if match_patch:
                patch_list.append(x)
            else:
                pass
        return patch_list
    elif lwd == 'yt':
        for x in os.listdir():
            match_yt = yt_pattern.match(x)
            if match_yt:
                yt_list.append(x)
            else:
                pass
        return yt_list
    

def version_search(file, version):
    ver1, ver2, ver3 = version.split('.')
    exact_version = re.compile(fr'.*\v?{ver1}.?{ver2}.?{ver3}.*\.(jar|apk)')
    for x in file:
        match = exact_version.match(x)
        if match:
            return match.group()



def install(cli='cli*',patches='patches*',integrations='integrations*',yt='yt*',ver=''):
    command = f"""java -jar {cli} patch \
-b {patches} \
-m {integrations} \
-o revanced-{ver}.apk {yt} -p --options=options.json \
--exclusive \
-i alternative-thumbnails \
-i always-autorepeat \
-i client-spoof \
-i comments \
-i copy-video-url \
-i custom-branding \
-i custom-player-overlay-opacity \
-i disable-shorts-on-startup \
-i disable-auto-captions \
-i disable-player-popup-panels \
-i disable-zoom-haptics \
-i enable-debugging \
-i enable-tablet-layout \
-i external-downloads \
-i hdr-auto-brightness \
-i hide-shorts-components \
-i hide-ads \
-i hide-album-cards \
-i hide-autoplay-button \
-i hide-breaking-news-shelf \
-i hide-captions-button \
-i hide-cast-button \
-i hide-crowdfunding-box \
-i hide-email-address \
-i hide-endscreen-cards \
-i hide-filter-bar \
-i hide-floating-microphone-button \
-i hide-info-cards \
-i hide-layout-components \
-i hide-load-more-button \
-i hide-player-buttons \
-i hide-seekbar \
-i hide-timestamp \
-i hide-video-action-buttons \
-i hide-watermark \
-i minimized-playback \
-i navigation-buttons \
-i old-video-quality-menu \
-i open-links-externally \
-i playback-speed \
-i player-flyout-menu \
-i premium-heading \
-i remember-video-quality \
-i remove-player-controls-background \
-i return-youtube-dislike \
-i seekbar-tapping \
-i sponsorblock \
-i spoof-app-version \
-i swipe-controls \
-i theme \
-i tablet-mini-player \
-i vanced-microg-support \
-i video-ads \
-i wide-searchbar"""
    os.system(command)
    os.system(f'rm revanced-{ver}.keystore')