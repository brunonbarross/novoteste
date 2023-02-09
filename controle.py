from c_teste import *
from PyQt6.QtWidgets import *

class Controle(Main):

    def inic(self,x):
        x = self.uiTeste.leName.text()
        print(x)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText(x)
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()
