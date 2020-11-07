# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-28 20:53:07
# @LastEditTime: 2020-10-01 12:18:08
# @LastEditors: kcyln
# @Description: pyqt5控件--复选框和开关按钮

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QPushButton, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 复选框
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        # 开关按钮 
        self.color = QColor(0,0,0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(40, 40)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(40, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(40, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.color.name())
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Qcheckbox')
        self.show()
    
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("123")
        else:
            self.setWindowTitle('')
    
    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        
        if source.text() == "Red":
            self.color.setRed(val)
        elif source.text() == "Green":
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)
        
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.color.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())