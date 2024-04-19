from PyQt5.uic import loadUi
import os
from PyQt5 import QtWidgets, QtGui
import configparser

BASEDIR = os.path.dirname(__file__)
CONFIG = configparser.ConfigParser()


class KatanaLauncherSettings(QtWidgets.QDialog):
    """class representing the settings dialog box for setting user paths"""
    def __init__(self):
        super(KatanaLauncherSettings, self).__init__()
        loadUi(os.path.join(BASEDIR, "assets\\KatanaLauncherSettings.ui"), self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(BASEDIR, "assets\\Katana.ico")))
        CONFIG.read(os.path.join(BASEDIR, "config.ini"))

        self.LE_Katana_Root.setText(CONFIG.get("Katana", "Path"))
        self.LE_RenderMan.setText(CONFIG.get("RenderMan", "Path"))
        self.LE_Arnold.setText(CONFIG.get("Arnold", "Path"))
        self.PB_Cancel.pressed.connect(self.close)
        self.PB_Save.pressed.connect(self.save)

        self.PB_Katana_Root.pressed.connect(self.selectKatanaPath)
        self.PB_RenderMan.pressed.connect(self.selectRendermanPath)
        self.PB_Arnold.pressed.connect(self.selectArnoldPath)

    def selectKatanaPath(self):
        """Creates a file browser to define the directory for Katana"""
        fname = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Katana Install location", 'C:\Program Files', QtWidgets.QFileDialog.ShowDirsOnly)
        self.LE_Katana_Root.setText(fname)

    def selectRendermanPath(self):
        """Creates a file browser to define the directory for RenderMan"""

        fname = QtWidgets.QFileDialog.getExistingDirectory(
            self, "RenderMan Install location", 'C:\Program Files', QtWidgets.QFileDialog.ShowDirsOnly)
        self.LE_RenderMan.setText(fname)

    def selectArnoldPath(self):
        """Creates a file browser to define the directory for Arnold"""
        fname = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Katana Install location", 'C:\Program Files', QtWidgets.QFileDialog.ShowDirsOnly)
        self.LE_Arnold.setText(fname)

    def save(self):
        """Saves the user input into the config file"""
        CONFIG['Katana']['Path'] = self.LE_Katana_Root.text()
        CONFIG['RenderMan']['Path'] = self.LE_RenderMan.text()
        CONFIG['Arnold']['Path'] = self.LE_Arnold.text()
        with open(os.path.join(BASEDIR, "config.ini"),'w', encoding="utf-8") as configFile:
            CONFIG.write(configFile)
        self.close()
