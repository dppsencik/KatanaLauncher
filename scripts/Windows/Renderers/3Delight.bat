set "DEFAULT_RENDERER=dl"

rem -- Location of where the main 3Delight package is installed --
set "DELIGHT=C:\Program Files\3Delight_%KATANA_VERSION%"
set "DELIGHT=%Delight%;C:\Program Files\3Delight"

rem -- The 3Delight bin folder is needed in PATH  --
set "PATH=%PATH%;%DELIGHT%\bin"

rem -- Location of the 3Delight for KATANA plug-in --
set "KATANA_RESOURCES=%KATANA_RESOURCES%;%DELIGHT%\3DelightForKatana"