import re
import os


def check_folder(create=False,chdir=False):
    if os.path.basename(os.getcwd()) != 'revanced':
        if os.path.isdir('revanced') == False:
            if create != False:
                os.mkdir('revanced')
                os.chdir(f'{os.getcwd()}/revanced')
            return False
        else:
            if chdir != False:
                os.chdir(f'{os.getcwd()}/revanced')
            return True
    else:
        return True


def file_search(lwd):
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
    command = f"""java -jar {cli} \
-b {patches} \
-m {integrations} \
-a {yt} \
-c \
-o revanced-{ver}.apk \
--exclusive \
-i always-autorepeat \
-i client-spoof \
-i comments \
-i copy-video-url \
-i custom-branding \
-i disable-shorts-on-startup \
-i disable-auto-captions \
-i disable-fullscreen-panels \
-i disable-player-popup-panels \
-i disable-zoom-haptics \
-i enable-debugging \
-i external-downloads \
-i hdr-auto-brightness \
-i hide-shorts-components \
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
-i hide-player-overlay \
-i hide-seekbar \
-i hide-timestamp \
-i hide-video-action-buttons \
-i hide-watch-in-vr \
-i hide-watermark \
-i minimized-playback \
-i navigation-buttons \
-i old-video-quality-menu \
-i open-links-externally \
-i premium-heading \
-i remember-video-quality \
-i remove-player-controls-background \
-i return-youtube-dislike \
-i seekbar-tapping \
-i tap-to-seek \
-i swipe-controls \
-i theme \
-i video-ads \
-i vanced-microg-support \
-i sponsorblock"""
    os.system(command)




