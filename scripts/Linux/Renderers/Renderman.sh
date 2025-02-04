export DEFAULT_RENDERER=prman


export RFKTREE=/opt/pixar/RenderManForKatana-$RENVER/plugins/katana${KATANA_VERSION:0:3}
export RMANTREE=/opt/pixar/RenderManProServer-$RENVER
export KATANA_RESOURCES=$KATANA_RESOURCES:$RFKTREE
export PATH=$PATH:$RMANTREE/bin



# USD
export FNPXR_PLUGINPATH=$RFKTREE/usd
export RMAN_SHADERPATH=$RMAN_SHADERPATH:$RFKTREE/usd/resources/shaders
export RMAN_RIXPLUGINPATH=$RMAN_RIXPLUGINPATH:$RMANTREE/lib/plugins:$RFKTREE/usd
export PATH=$PATH:$RFKTREE/usd

export PATH=$PATH:$RMANTREE/lib