from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from pathlib import Path
import os
import sys


BASEDIR = Path(__file__).parent

class KatanaLauncherEditor(QtWidgets.QMainWindow):
    """Class representing the script editor window"""
    def __init__(self):
        super(KatanaLauncherEditor, self).__init__()
        loadUi(BASEDIR.joinpath("assets", "KatanaLauncherEditor.ui"), self)
        self.setWindowIcon(QtGui.QIcon(str(BASEDIR.joinpath("assets\\Katana.ico"))))
        self.cancel_BTN.pressed.connect(self.close)
        self.save_BTN.pressed.connect(self.save)
        self.activeScript = ''

    def load_data(self, script):
        self.activeScript = script
        variables = self.convert_script(script)
        row = 0
        self.tableWidget.setRowCount(len(variables))
        for variable in variables:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(variable))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(variables[variable]))
            row = row + 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def convert_script(self, script):
        variables = {}
        with open(BASEDIR.joinpath("scripts", script, ".bat"),'r', encoding="utf-8") as script:
            for line in script.read().splitlines():
                if line.startswith("set"):
                    split = line.split("=")
                    variables[split[0].removeprefix("set \"")] = split[1].removesuffix("\"")

        return variables
    
    def save(self):
        lines = []
        for i in range(self.tableWidget.rowCount()):
            lines.append("set \"" + self.tableWidget.item(i,0).text() + "=" + self.tableWidget.item(i,1).text() + "\" \n")
        with open(BASEDIR.joinpath("scripts", self.activeScript, ".bat"), 'w', encoding="utf-8") as script:
            script.writelines(lines)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = KatanaLauncherEditor()
    ui.load_data('maya')
    ui.show()
    app.exec_()