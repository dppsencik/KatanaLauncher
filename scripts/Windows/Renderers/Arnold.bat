set "DEFAULT_RENDERER=arnold"
rem -- Where you have installed the KtoA plug-in --
set "KTOA_HOME=C:\Program Files\Arnold\ktoa\ktoa-%RENVER%-kat%KATANA_LINE%-windows"

rem -- The KtoA bin folder is needed in PATH --
set "PATH=%PATH%;%KTOA_HOME%\bin"

rem set "solidangle_LICENSE="
rem set "ADSKFLEX_LICENSE_FILE="

rem -- This is how to load the KtoA plug-in --
set "KATANA_RESOURCES=%KATANA_RESOURCES%;%KTOA_HOME%"

rem -- USD plugins --
set "path=%KTOA_HOME%\\USD\\KatanaUsdPlugins\\lib;%KTOA_HOME%\\USD\\KatanaUsdPlugins\\plugin\\Libs;%path%"
set "KATANA_RESOURCES=%KTOA_HOME%\\USD\\KatanaUsdPlugins\\plugin;%KTOA_HOME%\\USD\\KatanaUsdArnold;%KATANA_RESOURCES%"
set "PYTHONPATH=%KTOA_HOME%\\USD\\KatanaUsdPlugins\\lib\\python;%PTHONPATH%" 

set "ARNOLD_FNUSDPLUGIN_DIR=%KTOA_HOME%\USD\Viewport"
set "FNPXR_PLUGINPATH=%FNPXR_PLUGINPATH%;%ARNOLD_FNUSDPLUGIN_DIR%"


