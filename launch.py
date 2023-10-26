import sys
import os
import configparser
import subprocess
from pathlib import Path
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

class KatanaLauncher(QtWidgets.QMainWindow):
    """class representing the main launcher UI"""
    def __init__(self):
        super(KatanaLauncher, self).__init__()
        loadUi('assets\\KatanaLauncher.ui', self)
        self.setWindowIcon(QtGui.QIcon('assets\\Katana.ico'))
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.populate()
        self.refresh_BTN.clicked.connect(self.populate)
        self.renderer_CB.currentTextChanged.connect(self.renderer_changed)
        self.katana_version_CB.currentTextChanged.connect(self.renderer_changed)
        self.editScripts_BTN.pressed.connect(self.edit_scripts)
        self.settings_BTN.pressed.connect(self.open_settings)
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
        if index == '3Delight':
            self.renderer_version_CB.addItem('Katana Version')
            self.renderer_version_CB.setCurrentIndex(0)
        elif index == 'RenderMan':
            renderman_path = self.config.get('RenderMan', 'Path')
            renderman_versions = [file.split('-')[1] for file in os.listdir(renderman_path)
                if 'RenderManForKatana' in file and os.path.isdir(renderman_path + '\\' + file)]
            renderman_versions.reverse()
            self.renderer_version_CB.addItems(renderman_versions)
            self.renderer_version_CB.setEnabled(True)
        elif index == 'Arnold':
            arnold_path = self.config.get('Arnold', "Path")
            arnold_versions = [file.split('-')[1] for file in os.listdir(arnold_path)
                if 'kat' + katana_line in file and 'ktoa' in file and
                os.path.isdir(arnold_path + '\\' + file)]
            arnold_versions.reverse()
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
        katana_path = self.config.get('Katana', "Path")
        katana_versions = [file[6:] for file in os.listdir(katana_path)
                           if os.path.isfile(katana_path + '\\'  + file + '\\bin\\katanaBin.exe')]
        renderers = [file[0:-4] for file in os.listdir('scripts\\Renderers')
                     if file.endswith('.bat')]
        scripts = [file[0:-4] for file in os.listdir('scripts')
                     if file.endswith('.bat')]
        #get scripts
        for script in scripts:
            check_box = QtWidgets.QCheckBox(script)
            self.scripts_layout.addWidget(check_box)
        self.scripts_layout.addStretch()

        #get versions
        katana_versions.reverse()
        self.katana_version_CB.addItems(katana_versions)
        self.renderer_CB.addItems(renderers)

    def launch(self):
        """Gather all environment variables, combine, and run a single .bat, launching Katana"""
        katana_version = self.katana_version_CB.currentText()
        os.environ['KATANA_VERSION'] = katana_version
        os.environ['KATANA_LINE'] = katana_version[:3]
        os.environ['KATANA_ROOT'] = self.config.get('Katana', "Path") + '\\Katana' + katana_version 
        os.environ['RENVER'] = self.renderer_version_CB.currentText()
        renderer = self.renderer_CB.currentText()
        optional_scripts = (
            self.scripts_layout.itemAt(i).widget() for i in range(self.scripts_layout.count()-1)
            if self.scripts_layout.itemAt(i).widget().isChecked())
        cmd = ''
        for script in optional_scripts:
            cmd += Path('scripts\\' + script.text() + '.bat').read_text(encoding="utf-8")
        cmd += Path('scripts\\Renderers\\' + renderer + '.bat').read_text(encoding="utf-8")
        cmd += "\n\"%KATANA_ROOT%\\bin\\katanaBin.exe\""
        # Temp bat file deletes itself when Katana closes
        cmd += "\ngoto 2>nul & del \"%~f0\""
        # Create temporary file with all commands
        with open("temp.bat", "w", encoding="utf-8") as f:
            f.write(cmd)

        os.system("start cmd /c temp.bat")

    def edit_scripts(self):
        """Open a notepad of user selected scripts to be edited"""
        optional_scripts = (
            self.scripts_layout.itemAt(i).widget() for i in range(self.scripts_layout.count()-1)
             if self.scripts_layout.itemAt(i).widget().isChecked())
        for script in optional_scripts:
            subprocess.Popen("notepad.exe scripts/" + script.text() + '.bat')


    def open_settings(self):
        """Open the settings config notepad"""
        subprocess.Popen("notepad.exe config.ini")

    def validate_paths(self):
        """Ensure all paths in config file exist"""
        for section in self.config.sections():
            path = self.config.get(section, 'Path')
            if not os.path.exists(path):
                return False
        return True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = KatanaLauncher()
    if ui.validate_paths():
        ui.center_on_screen()
        ui.show()
        app.exec_()
    else:
        QtWidgets.QMessageBox.critical(
            None,"Error",
            "One or more of your paths are not valid, please modify your config.ini file.",
            QtWidgets.QMessageBox.Ok)
        app.exit(0)
    