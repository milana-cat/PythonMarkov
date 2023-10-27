from MarkovLibrary import *
from PyQt5 import QtWidgets
from UiLayout import *
import sys


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.clearBtn.clicked.connect(self.clearOutput)
        self.resetBtn.clicked.connect(self.clearAll)
        self.runBtn.clicked.connect(self.run)

    def clearOutput(self):
        self.outputBox.setText("")

    def clearAll(self):
        self.inputBox.setText("")
        self.outputBox.setText("")
        self.cmdsBox.setText("")

    def run(self):
        text = self.inputBox.text()
        if len(text) == 0:
            self.outputBox.setText("Введите текст для обработки!")
            return

        cmds = self.cmdsBox.toPlainText()
        if len(cmds) == 0:
            self.outputBox.setText("Введите команды для выполнения!")
            return

        if (check_rules(cmds, "#")):
            res = start(cmds, text)
            self.outputBox.setText(res)
        else:
            self.outputBox.setText("В правилах есть ошибка.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
