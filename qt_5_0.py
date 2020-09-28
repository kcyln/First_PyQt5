# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-27 21:31:21
# @LastEditTime: 2020-09-28 20:32:43
# @LastEditors: kcyln
# @Description: pyqt5对话框--输入文字对话框和颜色对话框

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtWidgets import QFrame, QColorDialog
from PyQt5.QtGui import QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 输入对话框，从用户获取一个值显示在窗口上
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        # 颜色对话框，用来选择颜色
        col = QColor(0,0,0)

        self.btn2 = QPushButton('Color Dialog', self)
        self.btn2.move(20, 50)
        self.btn2.clicked.connect(self.showColorDialog)
        
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 52, 100, 100)

        self.setGeometry(300, 300, 390, 350)
        self.setWindowTitle("Input Dialog")
        self.show()
    
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
    
    def showColorDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
