export DEFAULT_RENDERER=arnold
export KTOA_ROOT=/opt/Autodesk/ktoa/ktoa-$RENVER-kat${KATANA_VERSION:0:3}-linux
export solidangle_LICENSE=
export ADSKFLEX_LICENSE_FILE=
export ARNOLD_PLUGIN_PATH=$KTOA_ROOT/Plugins
export KATANA_RESOURCES=$KATANA_RESOURCES:$KTOA_ROOT
export PATH=$PATH:$KTOA_ROOT/bin

# export MAYA_PATH=/usr/autodesk/maya2020
# export MTOA_PATH=/usr/autodesk/arnold/maya2020
# export XGEN_LOCATION=/usr/autodesk/maya2020/plug-ins/xgen
# export PATH=$ARNOLD_PLUGIN_PATH:/path/to/Yeti/bin:${PATH}
# export ARNOLD_PLUGIN_PATH=/path/to/Yeti/bin:$ARNOLD_PLUGIN_PATH
# export KTOA_LOAD_VERBOSITY=debug

# export MAYA_PATH=/usr/autodesk/maya2019
# export MTOA_PATH=/usr/autodesk/arnold/maya2019
# export XGEN_LOCATION=/usr/autodesk/maya2019/plug-ins/xgen
# export PATH=$ARNOLD_PLUGIN_PATH:/path/to/Yeti/bin:${PATH}
# export ARNOLD_PLUGIN_PATH=/path/to/Yeti/bin:$ARNOLD_PLUGIN_PATH
# export KTOA_LOAD_VERBOSITY=debug

# # https://github.com/Autodesk/arnold-usd#building-and-installation
# export ARNOLD_PLUGIN_PATH=$ARNOLD_PLUGIN_PATH:
# export PYTHONPATH=$PYTHONPATH:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/USD/KatanaUsdPlugins/lib/python
# export PXR_PLUGINPATH_NAME=$PXR_PLUGINPATH_NAME:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/USD/KatanaUsdPlugins/plugin
# export PXR_PLUGINPATH_NAME=$PXR_PLUGINPATH_NAME:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/RenderPlugins/usd
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/USD/KatanaUsdPlugins/lib

# export KATANA_RESOURCES=$KATANA_RESOURCES:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/USD/KatanaUsdPlugins/plugin
# export KATANA_RESOURCES=$KATANA_RESOURCES:/opt/Autodesk/ktoa/ktoa-3.2.2.2-kat4.0-linux/USD/KatanaUsdArnold

# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/Autodesk/ktoa/ktoa-3.2.2.1-kat4.0-linux/USD/KatanaUsdPlugins/lib
# export KATANA_RESOURCES=$KATANA_RESOURCES:/opt/Autodesk/ktoa/ktoa-3.2.2.1-kat4.0-linux/USD/KatanaUsdPlugins/plugin
# export PYTHONPATH=$PYTHONPATH:/opt/Autodesk/ktoa/ktoa-3.2.2.1-kat4.0-linux/USD/KatanaUsdPlugins/lib/python

# USD
# export KATANA_RESOURCES=$KATANA_RESOURCES:/opt/Autodesk/ktoa/ktoa-4.1.2.2-kat4.0-linux/USD/KatanaUsdPlugins/plugin
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/Autodesk/ktoa/ktoa-4.1.2.2-kat4.0-linux/USD/KatanaUsdPlugins/lib
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/Autodesk/ktoa/ktoa-4.1.2.2-kat4.0-linux/USD/KatanaUsdPlugins/plugin/Libs

# NdrParserPlugin and NdrDiscoveryPlugin
# export ARNOLD_FNUSDPLUGIN_DIR=/opt/Autodesk/ktoa/ktoa-4.1.2.2-kat4.5-linux/USD/Viewport
# export FNPXR_PLUGINPATH=$FNPXR_PLUGINPATH:$ARNOLD_FNUSDPLUGIN_DIR
