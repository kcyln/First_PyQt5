# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-10-01 12:18:27
# @LastEditTime: 2020-11-07 16:37:15
# @LastEditors: kcyln
# @Description: pyqt5控件--滑动条

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('./images/favicon.ico'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
    
    def changeValue(self, value):
        # 根据滑动条的值改变显示的图片
        if value == 0:
            self.label.setPixmap(QPixmap('./images/favicon.ico'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('favicon.ico'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('favicon.ico'))
        else:
            self.label.setPixmap(QPixmap('./images/favicon.ico'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())