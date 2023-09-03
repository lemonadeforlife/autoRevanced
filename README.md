# autoRevanced🔽
Download and install latest revanced patches for **YouTube**.
<br>
<br>
## Requiremenets:
- Java SDK 11+ ( [Azul zulu JDK](https://docs.azul.com/core/zulu-openjdk/install/debian#) or OpenJDK )
- [Python 3.10+](https://python.org)
- Install requirements.txt for script dependency
<br>
<br>
## Usage
```terminal
usage: AutoRevanced [-h] [-dt [DARK_THEME]] [-lt [LIGHT_THEME]] [-cy] [-cc]
                    [-ci] [-cp] [-cl] [-di] [-i]

A simple automation tool for downloading and installing latest revanced
patches for youtube

options:
  -h, --help            show this help message and exit
  -dt [DARK_THEME], --dark-theme [DARK_THEME]
                        set custom dark theme for youtube app
  -lt [LIGHT_THEME], --light-theme [LIGHT_THEME]
                        set custom light theme for youtube app
  -cy, --check-youtube  checks the latest revanced supported youtube version
  -cc, --check-cli      checks the latest revanced cli version
  -ci, --check-integrations
                        checks the latest revanced integrations version
  -cp, --check-patches  checks the latest revanced patches version
  -cl, --check-all      list all the components latest version
  -di, --download-install
                        Download & Install Latest YouTube Revanced
  -i, --install         Install YouTube Revanced Only

```

This script download all the necessary components in your `HOME/Downloads/revanced` as well revanced-version.apk and saves the version number in `HOME/.config/autoRevanced/version.json`.  
But it does not completely rely on `version.json` file to checking latest version. It uses regex for detecting file so it is recommend to not renaming the file core name and version.

### Download & Install Revanced Patches:
Use `-di` or `--download-install`  

It checks for the all latest file in `HOME/Downloads/revanced` and downloads only missing one only. So if you manually download the file and put it on the revanced folder. It will skip those files and download the missing one.  
It will download latest supported version of youtube.apk, cli, patches, integrations and then it installs it to patch YouTube.

### Install Revanced Patches
Use `-i` or `--install`

It only install the patch on YouTube if you already downloaded all the necessary files in revanced folder. If you have any missing compononents then it will not run.


### Custom Dark Theme and Light Theme
Use:  
`-dt` or `--dark-theme` for custom Dark theme  
`-lt` or `--light-theme` for custom light theme

example: `-dt #000000` or `-lt #00FFFF` or `-dt #FF00FF -lt #EA1E5A`

Use it only when using `--install` or `--download-install` command only.
