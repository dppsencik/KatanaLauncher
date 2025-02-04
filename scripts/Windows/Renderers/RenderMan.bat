set "DEFAULT_RENDERER=prman"

set "PIXAR_LICENSE_FILE=C:\Program Files\Pixar\pixar.license"

rem -- Location of the RenderMan Pro Server installation --
set "RMANTREE=C:\Program Files\Pixar\RenderManProServer-%RENVER%"

rem -- Location of the PRman plugin for KATANA --
set "RFKTREE=C:\Program Files\Pixar\RenderManForKatana-%RENVER%\plugins\katana%KATANA_LINE%"

rem -- This is what is required to load the RfK plugin --
set "KATANA_RESOURCES=%KATANA_RESOURCES%;%RFKTREE%"

set "RMAN_SHADERPATH=%RMANTREE%\lib\shad"
set "RMAN_RIXPLUGINPATH=%RMAN_RIXPLUGINPATH%;%RMANTREE%\lib\plugins"

set "PATH=%PATH%;%KATANA_ROOT%\bin"
