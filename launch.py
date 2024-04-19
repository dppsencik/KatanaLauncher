import sys
import os
import configparser
import subprocess
from pathlib import Path
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi
from settings import KatanaLauncherSettings
from editscripts import KatanaLauncherEditor

BASEDIR = os.path.dirname(__file__)
CONFIG = configparser.ConfigParser()

try:
    from ctypes import windll  # Only exists on Windows.

    APP_ID = "Foundry.Katana.Launcher.1"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
except ImportError:
    pass


class KatanaLauncher(QtWidgets.QMainWindow):
    """class representing the main launcher UI"""

    def __init__(self):
        super(KatanaLauncher, self).__init__()
        loadUi(os.path.join(BASEDIR, "assets\\KatanaLauncher.ui"), self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(BASEDIR, "assets\\Katana.ico")))
        CONFIG.read(os.path.join(BASEDIR, "config.ini"))
        self.settings = KatanaLauncherSettings()
        self.editor = KatanaLauncherEditor()
        self.populate()
        self.refresh_BTN.clicked.connect(self.populate)
        self.renderer_CB.currentTextChanged.connect(self.renderer_changed)
        self.katana_version_CB.currentTextChanged.connect(self.renderer_changed)
        self.editScripts_BTN.pressed.connect(self.edit_script)
        self.settings_BTN.pressed.connect(self.settings.show)
        self.run_BTN.pressed.connect(self.launch)

    def center_on_screen(self):
        """Centers the window to the users screen."""
        qt_rectangle = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def renderer_changed(self, index):
        """After the combobox changes, find and populate the versions for chosen renderer"""
        index = self.renderer_CB.currentText()
        katana_line = self.katana_version_CB.currentText()[0:3]
        self.renderer_version_CB.clear()
        self.renderer_version_CB.setEnabled(False)
        if index == "3Delight":
            self.renderer_version_CB.addItem("Katana Version")
            self.renderer_version_CB.setCurrentIndex(0)
        elif index == "RenderMan":
            renderman_path = CONFIG.get("RenderMan", "path")
            renderman_versions = [
                file.split("-")[1]
                for file in os.listdir(renderman_path)
                if "RenderManForKatana" in file
                and os.path.isdir(renderman_path + "\\" + file)
            ]
            renderman_versions.reverse()
            if not renderman_versions:
                self.renderer_version_CB.addItem('None')
                self.renderer_version_CB.setEnabled(False)
            else:
                self.renderer_version_CB.addItems(renderman_versions)
                self.renderer_version_CB.setEnabled(True)
        elif index == "Arnold":
            arnold_path = CONFIG.get("Arnold", "path")
            arnold_versions = [
                file.split("-")[1]
                for file in os.listdir(arnold_path)
                if "kat" + katana_line in file
                and "ktoa" in file
                and os.path.isdir(arnold_path + "\\" + file)
            ]
            arnold_versions.reverse()
            if not arnold_versions:
                self.renderer_version_CB.addItem('None')
                self.renderer_version_CB.setEnabled(False)
            else:
                self.renderer_version_CB.addItems(arnold_versions)
                self.renderer_version_CB.setEnabled(True)
        else:
            self.renderer_version_CB.setEnabled(False)

    def populate(self):
        """populates the UI with versions found"""
        # clear scripts
        while self.scripts_layout.count():
            child = self.scripts_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # clear versions
        self.katana_version_CB.clear()
        self.renderer_CB.clear()

        CONFIG.read(os.path.join(BASEDIR, "config.ini"))
        if self.validate_paths():
            # get versions
            katana_path = CONFIG.get("Katana", "path")
            katana_versions = [
                file[6:]
                for file in os.listdir(katana_path)
                if os.path.isfile(katana_path + "\\" + file + "\\bin\\katanaBin.exe")
            ]
            renderers = [
                file[0:-4]
                for file in os.listdir((os.path.join(BASEDIR, "scripts\\Renderers")))
                if file.endswith(".bat")
            ]
            scripts = [
                file[0:-4]
                for file in os.listdir((os.path.join(BASEDIR, "scripts")))
                if file.endswith(".bat")
            ]
            # get scripts
            for script in scripts:
                check_box = QtWidgets.QCheckBox(script)
                self.scripts_layout.addWidget(check_box)
            self.scripts_layout.addStretch()

            # add to UI
            katana_versions.reverse()
            self.katana_version_CB.addItems(katana_versions)
            self.renderer_CB.addItems(renderers)

    def edit_script(self):
        optional_scripts = []
        for i in range(self.scripts_layout.count() - 1):
            if self.scripts_layout.itemAt(i).widget().isChecked():
                optional_scripts.append(self.scripts_layout.itemAt(i).widget().text())
        if optional_scripts:
            self.editor.load_data(optional_scripts[0])
            self.editor.show()

    def launch(self):
        """Gather all environment variables, combine, and run a single .bat, launching Katana"""
        # Gather user input
        katana_version = self.katana_version_CB.currentText()
        os.environ["KATANA_VERSION"] = katana_version
        os.environ["KATANA_LINE"] = katana_version[:3]
        os.environ["KATANA_ROOT"] = (
            CONFIG.get("Katana", "path") + "\\Katana" + katana_version
        )
        os.environ["RENVER"] = self.renderer_version_CB.currentText()
        renderer = self.renderer_CB.currentText()


        if katana_version == "" or renderer == "":
            QtWidgets.QMessageBox.critical(
                None,
                "Error",
                "No Katana version or renderer selected.",
                QtWidgets.QMessageBox.Ok,
            )
            return
        # Create and launch script
        optional_scripts = (
            self.scripts_layout.itemAt(i).widget()
            for i in range(self.scripts_layout.count() - 1)
            if self.scripts_layout.itemAt(i).widget().isChecked()
        )
        cmd = "@echo off \n"
        for script in optional_scripts:
            cmd += Path(
                os.path.join(BASEDIR, "scripts\\" + script.text() + ".bat")
            ).read_text(encoding="utf-8")
        cmd += Path(
            os.path.join(BASEDIR, "scripts\\Renderers\\" + renderer + ".bat")
        ).read_text(encoding="utf-8")
        cmd += '\n"%KATANA_ROOT%\\bin\\katanaBin.exe"'
        # Temp bat file deletes itself when Katana closes
        cmd += '\ngoto 2>nul & del "%~f0"'
        # Create temporary file with all commands
        with open(os.path.join(BASEDIR, "temp.bat"), "w", encoding="utf-8") as f:
            f.write(cmd)

        os.system("start cmd /c temp.bat")

    def validate_paths(self):
        """Ensure all paths in config file exist"""
        for section in CONFIG.sections():
            path = CONFIG.get(section, "path")
            if not os.path.exists(path):
                QtWidgets.QMessageBox.critical(
                    None,
                    "Error",
                    "One or more of your paths are not valid, please modify your config.ini file.",
                    QtWidgets.QMessageBox.Ok,
                )
                return False
        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = KatanaLauncher()
    ui.center_on_screen()
    ui.show()
    app.exec_()
