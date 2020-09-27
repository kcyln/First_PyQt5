# -*- coding: utf-8 -*-
# @Author: kcyln
# @Date: 2020-09-27 21:07:02
# @LastEditTime: 2020-09-27 21:31:06
# @LastEditors: kcyln
# @Description: pyqt5事件和信号--发出信号


import sys

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    # 创建信号closeApp
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 自定义closeApp信号连接到QMainWindow的close槽
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    
    def mousePressEvent(self, event):
        # 当在窗体上点击鼠标时会触发closeApp信号，使程序退出。
        self.c.closeApp.emit()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
