# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-11-07 17:32:31
# @LastEditTime: 2020-11-07 17:36:38
# @LastEditors: kcyln
# @Description: pyqt5控件--QComboBox

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")  

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()
 
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())