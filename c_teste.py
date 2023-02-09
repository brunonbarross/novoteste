from PyQt6.QtWidgets import *
from ui_teste import *
from PyQt6.QtCore import *
from controle import *

import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uiTeste = Ui_MainWindow()

        self.uiTeste.setupUi(self)

        self.uiTeste.pushButton.setIcon(QtGui.QIcon("imagem/menu_rosa.png"))
        self.uiTeste.pushButton.setIconSize(QtCore.QSize(30,30))
        #self.uiTeste.pushButton.setStyleSheet("text-align:left;")

        self.uiTeste.pushButton_2.setIcon(QtGui.QIcon("imagem/cadastro.png"))
        #DEFINE O TAMANHO DA IMAGEM
        self.uiTeste.pushButton_2.setIconSize(QtCore.QSize(25,25))

        self.uiTeste.pushButton.clicked.connect(lambda: self.toggle(250,True))

        self.uiTeste.pushButton_2.clicked.connect(lambda: self.uiTeste.stackedWidget.setCurrentWidget(self.uiTeste.page_cadastro))
        self.uiTeste.pushButton_4.clicked.connect(lambda: self.uiTeste.stackedWidget.setCurrentWidget(self.uiTeste.page_2))

        self.uiTeste.rbNovoCliente.setChecked(True)

        self.uiTeste.rbNovoCliente.clicked.connect(lambda : self.uiTeste.frame_teste.setStyleSheet("background-color:#d12dbd;"))
        self.uiTeste.rbNovoProduto.clicked.connect(lambda : self.uiTeste.frame_teste.setStyleSheet("background-color:#d4accc;"))

        self.uiTeste.pushButton_3.clicked.connect(lambda: Controle.inic(self,self.x))
        self.uiTeste.leName.returnPressed.connect(lambda: Controle.inic(self,self.x))
        

    def toggle(self, maxWidth, enable):
        if enable:

            width = self.uiTeste.frame_buttons.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
                self.uiTeste.pushButton_2.setText("novo item")
            else:
                widthExtended = standard
                self.uiTeste.pushButton_2.setText("")

            self.animation = QPropertyAnimation(self.uiTeste.frame_buttons, b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def printar(self):
        self.nome = self.uiTeste.leName.text()

        print(self.nome)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec())

