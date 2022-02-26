# coding=utf-8
"""
__author__ = "CEPBEP_RU56"
__copyright__ = "Copyright © 2022 CEPBEP_RU56."
__version__ = '(WoT v.1.15.0.3 #1168)'
__email__ = "CEPBEP_RU56@protonmail.com"

"""
import Keys
import BigWorld
from debug_utils import *
from Avatar import PlayerAvatar
from AvatarInputHandler import AvatarInputHandler

def initTrees():
    BigWorld.wg_enableTreeHiding(False)
    
def new_startGUI(self):
    old_startGUI(self)
    BigWorld.callback(0.2, initTrees)

old_startGUI = PlayerAvatar._PlayerAvatar__startGUI
PlayerAvatar._PlayerAvatar__startGUI = new_startGUI

def new_destroyGUI(self):
    BigWorld.wg_enableTreeHiding(False)
    old_destroyGUI(self)

old_destroyGUI = PlayerAvatar._PlayerAvatar__destroyGUI
PlayerAvatar._PlayerAvatar__destroyGUI = new_destroyGUI

def new_onControlModeChanged(current, eMode, **args):
    old_onControlModeChanged(current, eMode, **args)
    if eMode == 'sniper':
        BigWorld.wg_setTreeHidingRadius(720, 0)
    else:
        BigWorld.wg_setTreeHidingRadius(15.0, 10.0)
        
old_onControlModeChanged = AvatarInputHandler.onControlModeChanged
AvatarInputHandler.onControlModeChanged = new_onControlModeChanged

def new_PlayerHandleKey(current, isDown, key, mods):
    if hasattr(BigWorld.player(), 'arena'):
        if key == Keys.KEY_LALT:
            player = BigWorld.player()
            if player.inputHandler.ctrl == player.inputHandler.ctrls['sniper']:
                if isDown:
                    BigWorld.wg_setTreeHidingRadius(15.0, 10.0)
                else:
                    BigWorld.wg_setTreeHidingRadius(720, 0)
            else:
                if isDown:
                    BigWorld.wg_enableTreeHiding(True)
                    BigWorld.wg_setTreeHidingRadius(720, 0)
                else:
                    BigWorld.wg_enableTreeHiding(False)
    return old_PlayerHandleKey(current, isDown, key, mods)

old_PlayerHandleKey = PlayerAvatar.handleKey
PlayerAvatar.handleKey = new_PlayerHandleKey

print '[Mod]:SetTreeHidingRadius'
print '[Description]:Adapted to the patch v.1.15.0.3 #1168 Allows you to make the foliage of trees and bushes translucent in sniper mode.'

